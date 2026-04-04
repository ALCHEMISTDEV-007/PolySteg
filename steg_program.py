import argparse
import os
from steg_class.file_metadata import PDFFileMetadata
from steg_class.image_steg import ImageSteganography
from steg_class.audio_steg import AudioSteganography
from steg_class.video_steg import VideoSteganography


def encrypt(type,input_file,metadata_name,message,output_file,parser,hidden_file):
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

def decrypt(type,input_file,parser,output_file,metadata_name):
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
    parser.add_argument('-m',required=False,type=str,help='The Message you want to hide')
    parser.add_argument('-mn',required=False,type=str,help='The Metadata key name, must start with /')
    parser.add_argument('-hf',required=False,type=str,help='The file that you want to hide')
    

    args=parser.parse_args()

    if not (args.d or args.e):
        parser.error("The script requires a encrypt or decrypt method")
    
    if args.d:
        decrypt(type=args.t,input_file=args.f,parser=parser,output_file=args.o,metadata_name=args.mn)
    elif args.e:
        if args.e and (args.m or args.hf):
            encrypt(type=args.t,input_file=args.f,metadata_name=args.mn,message=args.m,output_file=args.o,parser=parser,hidden_file=args.hf)
        else:
            parser.error('The script requires a output file and message/hidden file for encryption')

if __name__== "__main__":
    main()