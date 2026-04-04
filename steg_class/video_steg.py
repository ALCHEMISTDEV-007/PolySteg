import os
import subprocess
import cv2
import numpy as np

def convert_message_to_binary_list(message):
    binary_list = []
    for character in message:
        binary_list.append(format(ord(character), '08b'))
    return binary_list


class VideoSteganography:
    @staticmethod
    def encrypt(input_file, message, output_file):
        binary_list = convert_message_to_binary_list(message)
        VideoSteganography._perform_video_steg(input_file, binary_list, output_file)

    @staticmethod
    def encrypt_file(input_file, hidden_file, output_file):
        binary_list = []
        with open(hidden_file, 'rb') as hf:
            file_bytes = hf.read()
            for byte in file_bytes:
                binary_list.append(format(byte, '08b'))
        VideoSteganography._perform_video_steg(input_file, binary_list, output_file)

    @staticmethod
    def _perform_video_steg(input_file, binary_list, output_file):
        if output_file.lower().endswith('.mp4'):
            print("Warning: .mp4 uses lossy compression which destroys hidden data. Automatically changing output extension to .avi")
            output_file = output_file[:-4] + '.avi'
        elif not output_file.lower().endswith('.avi'):
            print("Warning: We recommend using .avi for Video Steganography to preserve lossless data.")
            output_file += '.avi'

        has_audio = False
        try:
            from moviepy.editor import VideoFileClip
            clip = VideoFileClip(input_file)
            if clip.audio is not None:
                has_audio = True
            clip.close()
        except Exception:
            pass

        temp_video = output_file + ".temp.avi" if has_audio else output_file

        cap = cv2.VideoCapture(input_file)
        if not cap.isOpened():
            raise Exception("Cannot open the input video file. Please ensure it is a valid video.")

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Uses FFV1 Lossless codec to ensure frames remain bit-perfect
        fourcc = cv2.VideoWriter_fourcc(*'FFV1')
        out = cv2.VideoWriter(temp_video, fourcc, fps, (width, height))

        # Flattened list of ALL bits to hide
        # format: 8 bits data + 1 continue bit
        all_bits = []
        for i, byte_str in enumerate(binary_list):
            for bit in byte_str:
                all_bits.append(int(bit))
            if i == len(binary_list) - 1:
                all_bits.append(1)  # continue
            else:
                all_bits.append(0)

        total_bits = len(all_bits)
        bits_written = 0
        total_capacity = 0
        print(f"Hiding {total_bits} bits of data into the video...")

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            capacity = frame.size
            total_capacity += capacity

            if bits_written < total_bits:
                frame_flat = frame.flatten()
                bits_to_write = total_bits - bits_written
                chunk_size = min(bits_to_write, capacity)

                # Extract chunk
                bit_chunk = all_bits[bits_written : bits_written + chunk_size]

                # Numpy fast bitwise ops to set LSB
                bit_chunk_np = np.array(bit_chunk, dtype=np.uint8)
                frame_flat[:chunk_size] = (frame_flat[:chunk_size] & 254) | bit_chunk_np

                frame = frame_flat.reshape((height, width, 3))
                bits_written += chunk_size

            out.write(frame)

        cap.release()
        out.release()
        
        if total_bits > total_capacity:
            print("ERROR: Video is too short/small to hold all the hidden data!")
            if os.path.exists(temp_video):
                os.remove(temp_video)
            return

        if has_audio:
            print("Multiplexing original audio onto the new lossless video...")
            try:
                import imageio_ffmpeg
                ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
                # Run ffmpeg to merge video + audio
                # -c:v copy copies the lossless video stream without re-encoding
                # -c:a aac encodes the audio to AAC
                subprocess.run(
                    [
                        ffmpeg_exe, "-y", "-i", temp_video, "-i", input_file,
                        "-c:v", "copy", "-c:a", "aac", "-map", "0:v:0", "-map", "1:a:0", output_file
                    ],
                    check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
                )
                os.remove(temp_video)
                print(f"Successfully saved to {output_file} with audio reserved!")
            except Exception as e:
                print(f"Failed to merge audio: {e}. The silent video is kept at {temp_video}")
                os.rename(temp_video, output_file)
        else:
            print(f"Successfully saved silent video to {output_file}")


    @staticmethod
    def decrypt(input_file):
        full_binary_string = VideoSteganography._decrypt_video(input_file)

        message = ''
        for i in range(0, len(full_binary_string), 8):
            byte_chunk = full_binary_string[i:i + 8]
            if len(byte_chunk) == 8:
                message += chr(int(byte_chunk, 2))
        print(f"Decrypted message: {message}")

    @staticmethod
    def decrypt_file(input_file, output_file):
        full_binary_string = VideoSteganography._decrypt_video(input_file)
        try:
            if len(full_binary_string) % 8 != 0:
                full_binary_string = full_binary_string[:-(len(full_binary_string) % 8)]

            byte_chunks = []
            for i in range(0, len(full_binary_string), 8):
                byte_chunks.append(full_binary_string[i:i + 8])

            byte_list = []
            for byte_chunk in byte_chunks:
                byte_value = int(byte_chunk, 2)
                byte_list.append(byte_value)

            file_bytes = bytes(byte_list)

            with open(output_file, 'wb') as file:
                file.write(file_bytes)
            print(f"Successfully extracted hidden file to {output_file}")
                
        except Exception as e:
            print(f"An error occured: {e}")

    @staticmethod
    def _decrypt_video(input_file):
        cap = cv2.VideoCapture(input_file)
        if not cap.isOpened():
            raise Exception("Cannot open the input video file.")
            
        full_binary_string = ''
        current_data = []

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_flat = frame.flatten()
            lsbs = frame_flat & 1

            done = False
            for bit in lsbs:
                if len(current_data) < 8:
                    current_data.append(str(bit))
                else:
                    full_binary_string += "".join(current_data)
                    current_data = []
                    if bit == 1:
                        done = True
                        break
            if done:
                break

        cap.release()
        return full_binary_string
