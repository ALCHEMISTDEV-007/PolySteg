import argparse
import os
from steg_class.file_metadata import PDFFileMetadata
from steg_class.image_steg import ImageSteganography
from steg_class.audio_steg import AudioSteganography
from steg_class.video_steg import VideoSteganography
from steg_class.crypto import CryptoHelpers


def encrypt(type,input_file,metadata_name,message,output_file,parser,hidden_file,password=None):
    temp_hidden_file = None
    if password:
        try:
            if hidden_file:
                with open(hidden_file, 'rb') as f:
                    data = f.read()
            elif message:
                data = message.encode('utf-8')
            else:
                parser.error("A message or hidden file is required for encryption")

            encrypted_data = CryptoHelpers.secure_encrypt(data, password)
            
            temp_hidden_file = ".temp_encrypted_payload.tmp"
            with open(temp_hidden_file, 'wb') as f:
                f.write(encrypted_data)
                
            hidden_file = temp_hidden_file
            message = None # Disable message path to force file path
        except Exception as e:
            parser.error(f"Encryption failed: {e}")

    try:
        if type=="pdf":
            if metadata_name and message:
                PDFFileMetadata.encrypt(file_path=input_file,metadata_key_name=metadata_name,output_file_path=output_file,message=message)
            elif metadata_name and hidden_file:
                PDFFileMetadata.encryptfile(file_path=input_file,metadata_key_name=metadata_name,hidden_file=hidden_file,output_file_path=output_file)
            else:
                print("PDF requires a mn flag for encrypting")
        
        elif type=='image':
            
            if hidden_file:
                ImageSteganography.encrypt_file(input_file=input_file,hidden_file=hidden_file,output_file=output_file)
            else: 
                ImageSteganography.encrypt(input_file=input_file,message=message,output_file=output_file)
        elif type=='audio':
            if hidden_file:
                AudioSteganography.encrypt_file(input_file=input_file, hidden_file=hidden_file, output_file=output_file)
            else:
                AudioSteganography.encrypt(input_file=input_file, message=message, output_file=output_file)
        elif type=='video':
            if hidden_file:
                VideoSteganography.encrypt_file(input_file=input_file, hidden_file=hidden_file, output_file=output_file)
            else:
                VideoSteganography.encrypt(input_file=input_file, message=message, output_file=output_file)
        else:
            parser.error("Supports only pdf,image,audio,video")
    finally:
        if temp_hidden_file and os.path.exists(temp_hidden_file):
            os.remove(temp_hidden_file)

def decrypt(type,input_file,parser,output_file,metadata_name,password=None):
    temp_output_file = None
    target_output_file = output_file
    
    if password:
        temp_output_file = ".temp_extracted_payload.tmp"
        output_file = temp_output_file

    try:
        if type=="pdf":
            if output_file:
              PDFFileMetadata.decryptfile(input_file_path=input_file,output_file_path=output_file,metadata_key_name=metadata_name)  
            else:    
                PDFFileMetadata.decrypt(file_path=input_file)
        elif type=='image':
            if output_file:
                ImageSteganography.decrypt_file(input_file=input_file,output_file=output_file)
            else:
                ImageSteganography.decrypt(input_file=input_file)
        elif type=='audio':
            if output_file:
                AudioSteganography.decrypt_file(input_file=input_file, output_file=output_file)
            else:
                AudioSteganography.decrypt(input_file=input_file)
        elif type=='video':
            if output_file:
                VideoSteganography.decrypt_file(input_file=input_file, output_file=output_file)
            else:
                VideoSteganography.decrypt(input_file=input_file)
        else:
            parser.error("Supports only pdf,image,audio,video")
            
        if password:
            if not os.path.exists(temp_output_file):
                print("Failed to extract data or no data found.")
                return
            
            with open(temp_output_file, 'rb') as f:
                encrypted_data = f.read()
                
            try:
                decrypted_bytes = CryptoHelpers.secure_decrypt(encrypted_data, password)
            except Exception as e:
                parser.error(f"Decryption failed at password validation: {e}")
                
            if target_output_file:
                with open(target_output_file, 'wb') as f:
                    f.write(decrypted_bytes)
                print(f"Successfully decrypted and saved to {target_output_file}")
            else:
                print(f"Decrypted message: {decrypted_bytes.decode('utf-8', errors='replace')}")
                
    finally:
        if temp_output_file and os.path.exists(temp_output_file):
            os.remove(temp_output_file)


def print_banner():
    os.system("")
    banner = (
        "\033[1;32m"
        r"""
      ____       _        ____  _             
     |  _ \ ___ | |_   _ / ___|| |_ ___  __ _ 
     | |_) / _ \| | | | |\___ \| __/ _ \/ _` |
     |  __/ (_) | | |_| | ___) | ||  __/ (_| |
     |_|   \___/|_|\__, ||____/ \__\___|\__, |
                   |___/                |___/ """
        "\n"
        "\033[2;32m"
        r"""      .pdf   \      .png        |    .mp3   /    .avi
        |       .txt       /       \     .gif"""
        "\n\n"
        "\033[1;37m"
        r"""     Status: Hidden | Author: Alchemist"""
        "\033[0m\n"
    )
    print(banner)

def main():
    print_banner()
    parser=argparse.ArgumentParser(description="The script which does steganography on given files such as pdf,images,audio & video files")

    parser.add_argument('-d',action='store_true',help='option decrypt')
    parser.add_argument('-e',action='store_true',help='option encrypt')
    parser.add_argument('-t',required=True,type=str,help='The type of file that steganography will be performed on')
    parser.add_argument('-f',required=True,type=str,help='The input file path')
    parser.add_argument('-o',required=False,type=str,help='The output file path')
    parser.add_argument('-m',required=False,type=str,help='The Message you want to hide (compressed and encrypted if -p used)')
    parser.add_argument('-mn',required=False,type=str,help='The Metadata key name, must start with /')
    parser.add_argument('-hf',required=False,type=str,help='The file that you want to hide (compressed and encrypted if -p used)')
    parser.add_argument('-p',required=False,type=str,help='The password to securely encrypt and compress the payload')
    

    args=parser.parse_args()

    if not (args.d or args.e):
        parser.error("The script requires a encrypt or decrypt method")
    
    if args.d:
        decrypt(type=args.t,input_file=args.f,parser=parser,output_file=args.o,metadata_name=args.mn,password=args.p)
    elif args.e:
        if args.e and (args.m or args.hf):
            encrypt(type=args.t,input_file=args.f,metadata_name=args.mn,message=args.m,output_file=args.o,parser=parser,hidden_file=args.hf,password=args.p)
        else:
            parser.error('The script requires a output file and message/hidden file for encryption')

if __name__== "__main__":
    main()