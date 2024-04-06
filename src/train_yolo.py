from ultralytics import YOLO
import torch

yaml_file = 'video1_content/dataset.yaml'

# Load a model
model = YOLO('yolov8n.pt')  # load a pretrained model (recommended for training)

device = None
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

model.to(device)

if __name__ == '__main__':
    # Train the model
    results = model.train(data=yaml_file, epochs=100, imgsz=640, batch=8, device=0)