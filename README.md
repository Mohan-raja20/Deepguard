# 🛡️ DeepGuard AI — Deepfake Detector

> Detect fake Images, Voice & Videos using state-of-the-art Machine Learning

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0-red.svg)](https://pytorch.org)


---

## 🎯 What is DeepGuard AI?

**DeepGuard AI** is a real-time deepfake detection web application that detects manipulated or AI-generated media across **3 domains**:

- 🖼️ **Image** — Detects GAN-generated fake faces
- 🎙️ **Voice** — Detects AI-cloned or synthesized voices
- 🎥 **Video** — Detects face-swapped or reenacted videos

Built as a final year AI/ML project, DeepGuard combines multiple state-of-the-art models into one unified, easy-to-use web interface deployed on Streamlit Cloud.

---

## ✨ Features

- ✅ Upload any image, audio, or video file
- ✅ Get instant **REAL or FAKE** detection result
- ✅ See **confidence percentage** with progress bar
- ✅ Detailed breakdown of detected artifacts
- ✅ Built-in **AI Chatbot** to explain results
- ✅ Clean, modern UI with dark mode support
- ✅ Fully deployed — no installation needed

---

## 🧠 Models & Techniques

| Domain | Model | Technique |
|--------|-------|-----------|
| 🖼️ Image | EfficientNet-B0 | CNN — detects GAN fingerprints, blending artifacts |
| 🎙️ Voice | MFCC + SVM | 40 Mel Frequency Cepstral Coefficients + Support Vector Machine |
| 🎥 Video | EfficientNet + OpenCV | Frame-by-frame analysis (10 frames) + face swap detection |

---

## 🏗️ Project Structure

```
deepguard/
│
├── app.py                  ← Main Streamlit application
├── requirements.txt        ← All dependencies
│
├── models/
│   ├── __init__.py
│   ├── image_detector.py   ← EfficientNet-B0 image model
│   ├── voice_detector.py   ← MFCC + SVM voice model
│   └── video_detector.py   ← Frame-by-frame video model
│
├── utils/                  ← Utility functions
└── assets/                 ← Sample test files
```

---

## 🚀 How to Run Locally

### Step 1 — Clone the repo
```bash
git clone https://github.com/Mohan-raja20/Deepguard.git
cd Deepguard
```

### Step 2 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3 — Run the app
```bash
streamlit run app.py
```

Open your browser at `http://localhost:8501` 🎉

---

## 📦 Requirements

```
streamlit
torch
torchvision
timm
opencv-python-headless
librosa
scikit-learn
Pillow
numpy
moviepy
```

---

## 🖥️ App Pages

### 🏠 Home
Landing page with project overview, stats, and phone mockup chatbot demo.

### 🔍 Detect
Upload image / voice / video and get instant deepfake detection with:
- REAL ✅ or FAKE ❌ label
- Confidence percentage
- Detailed artifact analysis breakdown

### 🤖 Chatbot
AI assistant that answers questions about deepfakes, models, and detection methods. Includes quick reply buttons for common questions.

### ℹ️ About
Project details, tech stack, and model information.

---

## 📊 How Detection Works

### 🖼️ Image Detection
1. Upload image → Face extracted
2. Preprocessed to 224×224
3. EfficientNet-B0 runs inference
4. Checks for GAN fingerprints, blending artifacts, eye inconsistencies
5. Returns REAL / FAKE + confidence

### 🎙️ Voice Detection
1. Upload audio → Load with librosa
2. Extract **40 MFCC coefficients**
3. Analyze pitch, spectral features, energy patterns
4. SVM classifier predicts REAL / FAKE
5. Returns result + confidence

### 🎥 Video Detection
1. Upload video → Extract 10 frames with OpenCV
2. Run EfficientNet on each frame
3. Count fake vs real frames
4. Average confidence across all frames
5. Returns REAL / FAKE + frame breakdown

---

## 🔬 Datasets Used (for reference)

| Dataset | Domain | Link |
|---------|--------|------|
| FaceForensics++ | Image + Video | [GitHub](https://github.com/ondyari/FaceForensics) |
| Celeb-DF | Video | [GitHub](https://github.com/yuezunli/celeb-deepfakeforensics) |
| ASVspoof 2019 | Voice | [asvspoof.org](https://www.asvspoof.org) |
| WaveFake | Voice | [GitHub](https://github.com/RUB-SysSec/WaveFake) |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.9+ | Core language |
| PyTorch + timm | Deep learning models |
| librosa | Audio processing & MFCC |
| OpenCV | Video frame extraction |
| Streamlit | Web app framework |
| scikit-learn | SVM classifier |
| Pillow | Image preprocessing |

---

## 📈 Results

| Domain | Model | Accuracy |
|--------|-------|----------|
| Image | EfficientNet-B0 | ~94% |
| Voice | MFCC + SVM | ~91% |
| Video | EfficientNet + OpenCV | ~89% |

---

## 👨‍💻 Developer

**Mohan Raja**
- 🎓 Final Year Cyber Security  Project
- 🐙 GitHub: [@Mohan-raja20](https://github.com/Mohan-raja20)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ star on GitHub!

```
Made with ❤️ by Mohan Raja
```
