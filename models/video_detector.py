import cv2
import torch
import timm
from torchvision import transforms
from PIL import Image
import numpy as np

model = timm.create_model('efficientnet_b0', pretrained=True, num_classes=2)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5],[0.5])
])

def detect_video(video_path, num_frames=10):
    cap = cv2.VideoCapture(video_path)
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    step = max(total // num_frames, 1)
    scores = []
    for i in range(num_frames):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i * step)
        ret, frame = cap.read()
        if not ret:
            break
        img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        tensor = transform(img).unsqueeze(0)
        with torch.no_grad():
            out = torch.softmax(model(tensor), dim=1)
        scores.append(out[0][1].item())
    cap.release()
    avg = np.mean(scores)
    label = "FAKE" if avg > 0.5 else "REAL"
    confidence = avg if avg > 0.5 else 1 - avg
    fake_count = sum(1 for s in scores if s > 0.5)
    return label, round(confidence * 100, 1), fake_count, len(scores)