import numpy as np
from scipy.io import wavfile

def turn_message_to_binary_string_list(message):
    binary_list = []
    for character in message:
        binary_list.append(format(ord(character), '08b'))
    return binary_list

def turn_int_to_binary(value):
    if value < 0:
        value = value + (2**16)
    return format(value, '016b')

def change_lsb(binary_string, bit):
    binary_list = list(binary_string)
    binary_list[-1] = bit
    return ''.join(binary_list)

def turn_binary_to_int(value):
    if value[0] == '1':
        unsigned = int(value, 2)
        signed = unsigned - (2**16)
        return signed
    else:
        return int(value, 2)

def turn_unsigned_binary_to_int(value):
    return int(value, 2)

def read_group(group_list, character_length):
    binary_string = ''
    for index in range(character_length):
        binary = turn_int_to_binary(group_list[index])
        binary_string += binary[-1]
        
    binary = turn_int_to_binary(group_list[-1])
    continue_bit = binary[-1]
    return chr(turn_unsigned_binary_to_int(value=binary_string)), continue_bit

def read_group_binary_string(group_list, character_length):
    binary_string = ''
    for index in range(character_length):
        binary = turn_int_to_binary(group_list[index])
        binary_string += binary[-1]
        
    binary = turn_int_to_binary(group_list[-1])
    continue_bit = binary[-1]
    return binary_string, continue_bit

def savefile(binary_string, output_file):
    try:
        if len(binary_string) % 8 != 0:
            raise ValueError("Binary string value must be a multiple of 8")
    
        byte_chunks = []
        for i in range(0, len(binary_string), 8):
            byte_chunks.append(binary_string[i:i+8])
            
        byte_list = []
        for byte_chunk in byte_chunks:
            byte_value = int(byte_chunk, 2)
            byte_list.append(byte_value)
            
        file_bytes = bytes(byte_list)
        
        with open(output_file, 'wb') as file:
            file.write(file_bytes)
            
    except Exception as e:
        print(f"An error occured: {e}")

class AudioSteganography:

    @staticmethod
    def encrypt(input_file, message, output_file):
        sample_rate, data = wavfile.read(input_file)
        
        copy_of_data = data.copy().flatten()
        binary_list = turn_message_to_binary_string_list(message)
        audio_index = 0
        
        for index, binary_character in enumerate(binary_list):
            for bit in binary_character:
                binary = turn_int_to_binary(copy_of_data[audio_index])
                binary = change_lsb(binary_string=binary, bit=bit)
                copy_of_data[audio_index] = turn_binary_to_int(binary)
                audio_index = audio_index + 1
                
            binary = turn_int_to_binary(copy_of_data[audio_index])
            
            if index != len(binary_list) - 1:
                binary = change_lsb(binary_string=binary, bit='0')
            else:
                binary = change_lsb(binary_string=binary, bit='1')
                
            copy_of_data[audio_index] = turn_binary_to_int(binary)
            audio_index = audio_index + 1
            
        copy_of_data = copy_of_data.reshape(data.shape)
        wavfile.write(output_file, sample_rate, copy_of_data)

    @staticmethod
    def decrypt(input_file):
        sample_rate, data = wavfile.read(input_file)
        data = data.flatten()
        
        GROUP_SIZE = 9
        CHARACTER_SIZE = 8
        message = ''
        
        for index in range(0, len(data), GROUP_SIZE):
            character, continue_bit = read_group(group_list=data[index:index+GROUP_SIZE], character_length=CHARACTER_SIZE)
            message += character
            if continue_bit == '1':
                break
                
        print(f"Decrypted Message: {message}")

    @staticmethod
    def encrypt_file(input_file, hidden_file, output_file):
        sample_rate, data = wavfile.read(input_file)
        
        copy_of_data = data.copy().flatten()
        
        binary_list = []
        with open(hidden_file, 'rb') as hf:
            file_bytes = hf.read()
            for byte in file_bytes:
                binary_list.append(format(byte, '08b'))
                
        audio_index = 0
        
        for index, binary_character in enumerate(binary_list):
            for bit in binary_character:
                binary = turn_int_to_binary(copy_of_data[audio_index])
                binary = change_lsb(binary_string=binary, bit=bit)
                copy_of_data[audio_index] = turn_binary_to_int(binary)
                audio_index = audio_index + 1
                
            binary = turn_int_to_binary(copy_of_data[audio_index])
            
            if index != len(binary_list) - 1:
                binary = change_lsb(binary_string=binary, bit='0')
            else:
                binary = change_lsb(binary_string=binary, bit='1')
                
            copy_of_data[audio_index] = turn_binary_to_int(binary)
            audio_index = audio_index + 1
            
        copy_of_data = copy_of_data.reshape(data.shape)
        wavfile.write(output_file, sample_rate, copy_of_data)

    @staticmethod
    def decrypt_file(input_file, output_file):
        sample_rate, data = wavfile.read(input_file)
        data = data.flatten()
        
        GROUP_SIZE = 9
        CHARACTER_SIZE = 8
        full_binary_string = ''
        
        for index in range(0, len(data), GROUP_SIZE):
            binary_string, continue_bit = read_group_binary_string(group_list=data[index:index+GROUP_SIZE], character_length=CHARACTER_SIZE)
            full_binary_string += binary_string
            if continue_bit == '1':
                break
                
        savefile(binary_string=full_binary_string, output_file=output_file)