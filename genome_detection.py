import torch
from collections import OrderedDict
import os
from PIL import Image

def detect(img_path, save_dir='static/detected_images'):
    os.makedirs(save_dir, exist_ok=True)

    model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp6/weights/best.pt')
    results = model(img_path)

    detections = results.pandas().xyxy[0]
    filtered_detections = detections[detections['confidence'] > 0.72]
    object_counts_unsorted = filtered_detections['name'].value_counts().to_dict()
    object_counts = OrderedDict(sorted(object_counts_unsorted.items()))

    gender = 'unidentifyable'

    disorder = 'No Predictions'

    try:
        if object_counts['X'] == object_counts['Y']:
            gender = 'Male'
    except:
        if object_counts['X'] == 2:
            gender = 'Female'

    if object_counts['G21'] != 2:
        disorder = 'Potentially Down Syndrome'
    elif object_counts['D13'] != 2:
        disorder = 'Potentially Patau Syndrome'
    elif object_counts['E18'] != 2:
        disorder = 'Potentially Edward\'s Syndrome'
    elif gender == 'unidentifyable' and object_counts['X'] == 2:
        disorder = 'Potentially Klinefelter\'s Syndrome'
        gender = 'Male'
    elif gender == 'unidentifyable' and object_counts['X'] == 3:
        disorder = 'Potentially XXX Syndrome'
        gender = 'Female'
    elif gender == 'unidentifyable' and object_counts['Y'] == 2:
        disorder = 'Potentially XYY Syndrome'
        gender = 'Male'
    elif gender == 'unidentifyable' and object_counts['X'] < 2:
        disorder = 'Potentially Turner\'s Syndrome'
        gender = 'Female'

    save_path = os.path.join(save_dir, os.path.basename(img_path))

    annotated_images = results.render()
    for img in annotated_images:
        Image.fromarray(img).save(save_path)

    return object_counts, gender, disorder
