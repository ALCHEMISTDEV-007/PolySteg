# 🕵️‍♂️ PolySteg: The Alchemist Steganography Suite

A professional-grade, multi-format Python CLI utility designed for **stealthy data exfiltration, Red Team simulations, and covert communications**.

**PolySteg** allows security researchers to conceal **text, files, and nested payloads** inside **PDFs, Images, Audio, and Video files** with **AES encryption, compression, metadata spoofing, and nested steganography**.

---

# 🚀 What's New (v1.4)

## 🪆 Nested Steganography (NEW)

PolySteg now supports **Nested Steganography** — hiding data **within multiple layers of cover files**.

Example Workflow:

```text
Payload → Image → Audio → Video
```

This creates **multi-layer covert payload chains**.

### Features

* Multi-layer embedding
* Inner-to-outer concealment
* Multi-format nesting
* Compatible with encryption & spoofing

---

# 🪆 Nested Steganography Usage

### Hide Using Nested Covers

```bash
polysteg -e --nested-covers image.png audio.wav video.mp4 -hf payload.zip -o output.avi
```

Inner → Outer Order:

```
image.png → audio.wav → video.mp4
```

---

### Extract Nested Payload

```bash
polysteg -d --nested-dec video audio image -f output.avi
```

Outer → Inner Order:

```
video → audio → image
```

---

# 🧬 Metadata Spoofing (v1.3)

PolySteg supports **metadata spoofing**:

* Camera model spoofing
* Author spoofing
* Software signature spoofing
* Timestamp spoofing
* Origin metadata spoofing

Example:

```bash
polysteg -e -t image -f cover.png -hf payload.zip --spoof
```

---

# 🔐 Encryption & Compression (v1.2)

PolySteg supports:

* AES Encryption (Fernet)
* PBKDF2 Key Derivation
* Password Protection (`-p`)
* Automatic Compression

Pipeline:

```
Payload → Compress → Encrypt → Hide
```

---

# 🎬 Video Steganography (v1.1)

* Frame-level embedding
* Lossless AVI output
* Audio preservation
* Large payload support

---

# 🎯 Multi-Domain Steganography

PolySteg supports:

* 🖼️ Image
* 🎵 Audio
* 📄 PDF
* 🎬 Video

---

# 🌍 Installation

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

# 💻 Basic Usage

### Hide Message

```bash
polysteg -e -t image -f cover.png -m "Secret message" -o output.png
```

---

### Hide File With Encryption

```bash
polysteg -e -t image -f cover.png -hf payload.zip -p password -o output.png
```

---

### Apply Metadata Spoofing

```bash
polysteg -e -t image -f cover.png -hf payload.zip --spoof
```

---

# 🛠️ CLI Options

```
-h, --help
-d
-e
-t
-f
-o
-m
-mn
-hf
-p
--spoof
--nested-covers
--nested-dec
```

---

# 🧠 Architecture

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
│   ├── nested_steg.py
│
├── setup.py
├── README.md
```

---

# 🔥 Use Cases

* Red Team Operations
* Covert Communication
* Multi-Layer Data Exfiltration
* Malware Simulation
* Digital Forensics Research
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
