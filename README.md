# 🕵️‍♂️ PolySteg: The Alchemist Steganography Suite

A professional-grade, multi-format Python CLI utility designed for **stealthy data exfiltration, Red Team simulations, and covert communications**.

**PolySteg** allows security researchers to conceal both **text payloads** and **raw files** inside standard **PDFs, Images, Audio, and Video files**, with **built-in compression and password-based encryption**.

---

# 🚀 What's New (v1.2)

### 🔐 Encryption + Compression Added

PolySteg now supports:

* Password-based encryption (`-p`)
* Automatic compression (zlib)
* Secure key derivation (PBKDF2)
* AES-based encryption (Fernet)

### Encryption Pipeline

```
Payload → Compress → Encrypt → Encode → Hide
```

This significantly improves:

* Stealth
* Security
* Payload efficiency

---

# 🎬 Previous Update (v1.1) — Video Steganography

PolySteg now supports **Video Steganography**:

* Frame-by-frame LSB embedding
* Lossless AVI output
* Audio preservation via FFmpeg
* Large payload support
* NumPy-based pixel manipulation

---

# 🎯 Multi-Domain Concealment

PolySteg now supports **4 Steganography Domains**

---

## 🖼️ Image Steganography

* LSB pixel manipulation
* PNG / BMP support
* 3-pixel (9-bit grouping)
* Terminator flag detection

---

## 🎵 Audio Steganography

* WAV amplitude manipulation
* Binary payload embedding
* No audible distortion
* File & message payload support

---

## 📄 PDF Steganography

* Custom metadata injection
* Persistent hidden payload
* Clean extraction
* Custom metadata keys

---

## 🎬 Video Steganography

* Frame-level embedding
* Lossless AVI output
* Audio preserved
* Large payload capacity

---

# 🔐 Encryption Features

* Password-based encryption (`-p`)
* PBKDF2 key derivation
* AES-based Fernet encryption
* Automatic compression
* Secure payload handling

Example:

```bash
polysteg -e -t image -f cover.png -hf payload.zip -p mypassword -o secret.png
```

Extract:

```bash
polysteg -d -t image -f secret.png -p mypassword
```

---

# 🌍 Global CLI Execution

PolySteg installs globally using `setup.py`

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

Core Dependencies:

```bash
pip install cryptography numpy
```

Video Dependencies:

```bash
pip install opencv-python moviepy imageio_ffmpeg
```

---

# 💻 Usage

PolySteg requires:

* Operation flag (`-e` / `-d`)
* Type flag (`-t`)

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
polysteg -e -t image -f cover.png -m "Hidden message" -o output.png
```

Hide file with encryption:

```bash
polysteg -e -t image -f cover.png -hf payload.zip -p password -o output.png
```

Extract:

```bash
polysteg -d -t image -f output.png -p password
```

---

# 🎵 Audio Example

```bash
polysteg -e -t audio -f input.wav -hf payload.zip -o output.wav
```

Extract:

```bash
polysteg -d -t audio -f output.wav
```

---

# 📄 PDF Example

```bash
polysteg -e -t pdf -f report.pdf -mn /HiddenKey -m "Secret" -o output.pdf
```

Extract:

```bash
polysteg -d -t pdf -f output.pdf -mn /HiddenKey
```

---

# 🎬 Video Example

```bash
polysteg -e -t video -f input.mp4 -m "Hidden message" -o output.avi
```

Hide file:

```bash
polysteg -e -t video -f input.mp4 -hf payload.zip -o output.avi
```

Extract:

```bash
polysteg -d -t video -f output.avi
```

---

# 🛠️ CLI Options

```
-h, --help   Show help
-d           Decrypt / Extract
-e           Encrypt / Hide
-t           File type (pdf, image, audio, video)
-f           Input file
-o           Output file
-m           Message to hide
-mn          Metadata key (PDF only)
-hf          Hidden file
-p           Password encryption
```

---

# 🧠 Architecture

Modular Object-Oriented Design:

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
│
├── setup.py
├── README.md
```

---

# 🔥 Use Cases

* Red Team Operations
* Covert Communication
* Data Exfiltration Simulation
* CTF Challenges
* Malware Analysis
* Digital Forensics

---

# ⚠️ Disclaimer

This tool is intended for:

* Educational purposes
* Ethical hacking
* Authorized testing

The author is not responsible for misuse.

---

# 👨‍💻 Author

**ALCHEMISTDEV-007**
B.Tech Cybersecurity
Red Teaming • Exploit Development • Offensive Security

---

# ⭐ Support

If you like the project:

* ⭐ Star
* 🍴 Fork
* 🧠 Contribute

---

# 🕶️ PolySteg

**Hide in Plain Sight**
