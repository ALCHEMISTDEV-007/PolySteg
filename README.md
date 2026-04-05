# 🕵️‍♂️ PolySteg: The Alchemist Steganography Suite

A professional-grade, multi-format Python CLI utility designed for **stealthy data exfiltration, Red Team simulations, and covert communications**.

**PolySteg** allows security researchers to conceal both **text payloads** and **raw files** inside **PDFs, Images, Audio, and Video files**, with **compression, AES encryption, and metadata spoofing** for enhanced stealth.

---

# 🚀 What's New (v1.3)

## 🧬 Metadata Spoofing (NEW)

PolySteg now supports **Metadata Spoofing** for enhanced stealth and anti-forensics.

You can now:

* Spoof file metadata
* Modify creation timestamps
* Change author information
* Spoof software signatures
* Hide tool fingerprints

This makes PolySteg **more stealthy and red-team ready**.

Example:

```bash
polysteg -e -t image -f cover.png -hf payload.zip --spoof
```

---

# 🔐 Encryption & Compression (v1.2)

PolySteg includes:

* AES-based encryption (Fernet)
* PBKDF2 key derivation
* Password protection (`-p`)
* Automatic compression (zlib)

Pipeline:

```
Payload → Compress → Encrypt → Hide
```

Example:

```bash
polysteg -e -t image -f cover.png -hf payload.zip -p strongpass -o output.png
```

Extract:

```bash
polysteg -d -t image -f output.png -p strongpass
```

---

# 🎬 Video Steganography (v1.1)

PolySteg supports:

* Frame-level LSB encoding
* Lossless AVI output
* Audio preservation
* Large payload embedding
* NumPy optimization

---

# 🎯 Multi-Domain Steganography

PolySteg supports **4 domains**

---

## 🖼️ Image Steganography

* LSB encoding
* PNG / BMP support
* Pixel-level embedding
* Terminator flags

---

## 🎵 Audio Steganography

* WAV amplitude embedding
* Lossless payload storage
* File & message support

---

## 📄 PDF Steganography

* Metadata injection
* Custom dictionary keys
* Persistent payload storage

---

## 🎬 Video Steganography

* Frame-by-frame encoding
* Lossless AVI output
* Audio preservation
* Large payload capacity

---

# 🧬 Metadata Spoofing Features

PolySteg can spoof:

* Author metadata
* Creation timestamps
* Software signature
* Camera/device metadata
* File origin information

Helps with:

* Anti-forensics
* Red-team stealth
* Malware simulation
* Research testing

---

# 🌍 Global CLI Execution

Install globally:

```bash
git clone https://github.com/ALCHEMISTDEV-007/PolySteg.git
cd PolySteg
pip install -e .
```

Verify:

```bash
polysteg -h
```

---

# ⚙️ Dependencies

Core:

```bash
pip install cryptography numpy
```

Video:

```bash
pip install opencv-python moviepy imageio_ffmpeg
```

---

# 💻 Usage

Supported Types:

```
image
audio
pdf
video
```

---

# 🖼️ Image Example

Hide message:

```bash
polysteg -e -t image -f cover.png -m "Secret message" -o output.png
```

Hide encrypted file:

```bash
polysteg -e -t image -f cover.png -hf payload.zip -p password -o output.png
```

---

# 🎵 Audio Example

```bash
polysteg -e -t audio -f input.wav -hf payload.zip -o output.wav
```

---

# 📄 PDF Example

```bash
polysteg -e -t pdf -f report.pdf -mn /Hidden -m "Secret" -o output.pdf
```

---

# 🎬 Video Example

```bash
polysteg -e -t video -f input.mp4 -hf payload.zip -o output.avi
```

---

# 🛠️ CLI Options

```
-h, --help   Show help
-d           Decrypt / Extract
-e           Encrypt / Hide
-t           File type
-f           Input file
-o           Output file
-m           Message
-mn          Metadata key
-hf          Hidden file
-p           Password encryption
--spoof      Metadata spoofing
```

---

# 🧠 Architecture

Modular Object-Oriented Design

```
polysteg/
│
├── steg_program.py
├── steg_class/
│   ├── crypto.py
│   ├── image_steg.py
│   ├── audio_steg.py
│   ├── video_steg.py
│   ├── file_metadata.py
│   ├── metadata_spoof.py
│
├── setup.py
├── README.md
```

---

# 🔥 Use Cases

* Red Team Operations
* Covert Communications
* Data Exfiltration Simulation
* Malware Research
* Digital Forensics
* CTF Challenges

---

# ⚠️ Disclaimer

This tool is intended for:

* Educational purposes
* Ethical hacking
* Authorized testing only

The author is not responsible for misuse.

---

# 👨‍💻 Author

**ALCHEMISTDEV-007**
B.Tech Cybersecurity
Red Teaming • Exploit Development • Offensive Security

---

# ⭐ Support

* ⭐ Star the repo
* 🍴 Fork
* 🧠 Contribute

---

# 🕶️ PolySteg

**Hide in Plain Sight**
