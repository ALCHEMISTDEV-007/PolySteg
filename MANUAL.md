# PolySteg Manual

**NAME**
`steg_program.py` - A multi-layered advanced steganography tool

**SYNOPSIS**
```bash
python steg_program.py [-e | -d] [-t TYPE] [-f INPUT_FILE] [-o OUTPUT_FILE] [OPTIONS]

python steg_program.py -e --nested-covers file1 file2 ... [OPTIONS]

python steg_program.py -d -f file --nested-dec type1 type2 ... [OPTIONS]
```

**DESCRIPTION**
PolySteg is a command-line steganography utility capable of concealing texts or arbitrary files within PDFs, Images, Audio, and Video files. Built with advanced red-teaming capabilities, PolySteg supports payload AES encryption/compression, metadata spoofing, and nested ("Russian Doll") multi-layer steganography.

### REQUIRED ARGUMENTS
*   `-e`, `--encrypt` - Encrypt and hide a payload into a cover file. Must be used with `-m` or `-hf`.
*   `-d`, `--decrypt` - Decrypt and extract a payload from a cover file.
*   `-t TYPE` - The type of steganography to be performed on the cover-file. Supported types are: `pdf`, `image`, `audio`, `video`. Required unless nested steganography is employed.
*   `-f INPUT_FILE` - The target cover file (for encryption) or stego file (for decryption). Required unless encryption is nested using `--nested-covers`.

### OPTIONAL ARGUMENTS / PAYLOADS
*   `-o OUTPUT_FILE` - Path to output the generated stego-object or standard extracted files.
*   `-m MESSAGE` - A raw text message to conceal. Do not use alongside `-hf`.
*   `-hf HIDDEN_FILE` - A path to a file you wish to conceal inside the cover file.
*   `-p PASSWORD` - Triggers AES encryption and ZLIB compression. When hiding, the payload is securely wrapped and encrypted using the provided password before being embedded. When decrypting, this password is required to reveal the hidden data.
*   `-mn METADATA_KEY` - Required primarily for PDF Steganography. The metadata key string where data is injected or retrieved. Automatically handled in nested steganography.
*   `--spoof SPOOF_HINT` - Applies misleading metadata tags to media files to distract forensic analysts. Supported spoof hints: `Canon`, `Nikon`, `Photoshop`, etc.

### NESTED STEGANOGRAPHY
Instead of manually piping one steganography operation into another, PolySteg automates Multi-Layer Steganography.
*   `--nested-covers file1 file2 file3 ...` - Pass an array of cover files from innermost to outermost. PolySteg routes the data through each format seamlessly.
*   `--nested-dec type1 type2 type3 ...` - Pass an array of string types mapping to the layers from outermost to innermost to seamlessly unwrap data. 

### EXAMPLES

**Basic Steganography**
Hide a text phrase inside an image:
```bash
python steg_program.py -e -t image -f my_photo.png -m "Secret Message" -o output.png
```

**Secure PDF Payload**
Hide an entire zip file inside a PDF, encrypted with AES:
```bash
python steg_program.py -e -t pdf -f doc.pdf -hf secret.zip -o clean.pdf -mn "/AuthorNotes" -p "MyStrongPassword"
```

**Extracting The Secure PDF**
```bash
python steg_program.py -d -t pdf -f clean.pdf -mn "/AuthorNotes" -p "MyStrongPassword" -o secret.zip
```

**Nested Steganography Workflow**
Hide "TOP SECRET" text inside a PDF, and then hide that PDF inside an Audio file, and then hide the audio inside a Video:
```bash
python steg_program.py -e --nested-covers inner.pdf middle.mp3 outer.avi -m "TOP SECRET" -o final.avi
```

**Decrypting The Nested Workflow**
```bash
python steg_program.py -d -f final.avi --nested-dec video audio pdf
```
