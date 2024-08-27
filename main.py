from ultralytics import YOLO

# Carregar modelo
model = YOLO('model/activeModel_v1.0.pt')

# Inferencia do modelo
results = model(source='inference/img02.png', conf=0.75, save=True)