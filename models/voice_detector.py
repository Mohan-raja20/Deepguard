import librosa
import numpy as np

def extract_mfcc(path):
    y, sr = librosa.load(path, sr=16000, duration=5)
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return np.mean(mfcc.T, axis=0)

def detect_voice(audio_path):
    features = extract_mfcc(audio_path)
    energy = np.mean(np.abs(features))
    fake_prob = min(max(energy / 20.0, 0.1), 0.95)
    label = "FAKE" if fake_prob > 0.5 else "REAL"
    confidence = fake_prob if fake_prob > 0.5 else 1 - fake_prob
    return label, round(confidence * 100, 1)