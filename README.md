# 🕵️‍♂️ PolySteg: The Alchemist Steganography Suite

A professional-grade, multi-format Python CLI utility designed for **stealthy data exfiltration, Red Team simulations, and covert communications**.

**PolySteg** allows security researchers to conceal both **text payloads** and **raw files** inside standard **PDFs, Images, Audio, and Video files**.

---

# 🚀 New Update (v1.1) — Video Steganography Added 🎬

**NEW FEATURE (Added After 2 Days)**

PolySteg now supports **Video Steganography** using **Lossless Frame-Level LSB Encoding**.

### 🎬 Video Steganography Features

* Frame-by-frame **LSB embedding**
* Supports **large payloads**
* Converts output automatically to **lossless AVI**
* **Audio preservation** using FFmpeg
* Efficient **NumPy pixel manipulation**
* Handles **large videos safely** using OpenCV streaming

### 🔧 Technology Stack

* OpenCV (`cv2`)
* NumPy
* MoviePy
* imageio_ffmpeg
* FFmpeg (Audio Preservation)

---

# 🎯 Multi-Domain Concealment

PolySteg now supports **4 stealth domains**:

## 🖼️ Images (LSB)

* Uses **Least Significant Bit (LSB)** manipulation
* Supports **PNG / BMP** lossless formats
* **3-pixel (9-bit grouping)** strategy
* Terminator flag for precise extraction

---

## 🎵 Audio (LSB)

* Embeds payload inside **WAV audio samples**
* Modifies amplitude values
* Maintains **auditory transparency**
* Supports **text & full file payloads**

---

## 📄 PDF (Metadata Injection)

* Injects payloads into **custom metadata fields**
* Uses dictionary objects (example: `/LicenseCode`)
* Ensures **data persistence**
* Clean extraction workflow

---

## 🎬 Video (Frame LSB Encoding) — NEW

* Frame-by-frame pixel encoding
* Lossless AVI output
* Audio preserved automatically
* Large payload support
* Efficient NumPy processing

---

# 🔐 Payload Flexibility

PolySteg supports:

* Hide **Text Messages** (`-m`)
* Hide **Entire Files** (`-hf`)
* Extract payloads seamlessly

---

# 🌍 Global CLI Execution

Packaged using **setup.py** allowing:

* Global execution
* CLI-based workflow
* Red-team automation friendly

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/ALCHEMISTDEV-007/PolySteg.git
cd PolySteg
```

Install dependencies:

```bash
pip install -e .
```

Video dependencies:

```bash
pip install opencv-python moviepy numpy imageio_ffmpeg
```

Verify installation:

```bash
polysteg -h
```

---

# 💻 Usage & Syntax

PolySteg requires:

* Operation flag (`-e` encrypt / `-d` decrypt)
* Target type (`-t pdf | image | audio | video`)

---

# 🖼️ Image Steganography

Hide Text:

```bash
polysteg -e -t image -f cover.png -m "Target acquired." -o secret.png
```

Hide File:

```bash
polysteg -e -t image -f cover.png -hf keys.zip -o secret.png
```

Extract:

```bash
polysteg -d -t image -f secret.png
```

---

# 🎵 Audio Steganography

Hide File:

```bash
polysteg -e -t audio -f track.wav -hf payload.exe -o transmission.wav
```

Extract:

```bash
polysteg -d -t audio -f transmission.wav -o extracted_payload.exe
```

---

# 📄 PDF Steganography

Hide Text:

```bash
polysteg -e -t pdf -f report.pdf -mn /Classified -m "Server IPs enclosed" -o final_report.pdf
```

Extract:

```bash
polysteg -d -t pdf -f final_report.pdf -mn /Classified
```

---

# 🎬 Video Steganography (NEW)

Hide Text:

```bash
polysteg -e -t video -f input.mp4 -m "Hidden message" -o output.avi
```

Hide File:

```bash
polysteg -e -t video -f input.mp4 -hf payload.zip -o output.avi
```

Extract:

```bash
polysteg -d -t video -f output.avi
```

---

# 🛠️ Options Reference

```
-h, --help   Show help message
-d           Decrypt / Extract
-e           Encrypt / Hide
-t           File type (pdf, image, audio, video)
-f           Input file path
-o           Output file path
-m           Text message to hide
-mn          PDF metadata key (must start with '/')
-hf          Hidden file path
```

---

# 🧠 Architecture

PolySteg uses:

* Object-Oriented Design
* Modular Steg Classes
* CLI Orchestrator
* Multi-Format Handler

Project Structure:

```
polysteg/
│
├── steg_program.py
├── steg_class/
│   ├── image_steg.py
│   ├── audio_steg.py
│   ├── video_steg.py   ← NEW
│   ├── file_metadata.py
│
├── setup.py
├── README.md
```

---

# 🔥 Use Cases

* Red Team Operations
* Covert Communications
* Data Exfiltration Simulation
* CTF Challenges
* Malware Analysis Research
* Digital Forensics Practice

---

# ⚠️ Disclaimer

This tool is strictly for:

* Educational purposes
* Ethical hacking
* Authorized security auditing

The author is **not responsible** for misuse of this software.

---

# 👨‍💻 Author

**ALCHEMISTDEV-007**
B.Tech Cybersecurity
Red Teaming • Exploit Development • Offensive Security

---

# ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork the project
* 🧠 Contribute new techniques

---

# 🕶️ PolySteg

**Hide in Plain Sight**
