import re
from pathlib import Path

import torch
from rospkg import RosPack

model = torch.hub.load('ultralytics/yolov5', 'custom', Path(RosPack().get_path('ass2'))/'weights'/'yolov5l-face.pt')

# img = 'https://ultralytics.com/images/zidane.jpg'
img = './nekopara-pajama-chocola-and-vanilla.jpg'

results = model(img)

results.save()
