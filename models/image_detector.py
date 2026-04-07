import torch
import timm
from torchvision import transforms
from PIL import Image

model = timm.create_model('efficientnet_b0', pretrained=True, num_classes=2)
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5],[0.5])
])

def detect_image(image_path):
    img = Image.open(image_path).convert('RGB')
    tensor = transform(img).unsqueeze(0)
    with torch.no_grad():
        output = torch.softmax(model(tensor), dim=1)
    fake_prob = output[0][1].item()
    label = "FAKE" if fake_prob > 0.5 else "REAL"
    confidence = fake_prob if fake_prob > 0.5 else 1 - fake_prob
    return label, round(confidence * 100, 1)