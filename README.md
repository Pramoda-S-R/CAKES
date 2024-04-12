# Chromosomal Analysis Kit for Efficient Screening (CAKES)

## Introduction
Welcome to CAKES, a simple yet powerful tool designed to ease the process of genetic disorder identification, making it particularly useful for remote hospitals. By minimizing the labor involved in karyotype analysis, CAKES speeds up diagnostics, enhancing patient care through timely and precise genetic disorder detection.

## Features
- Utilizes YOLOv5 for advanced object detection in chromosome images.
- Identifies genome count and assesses potential genetic disorders.
- Logs each analysis in a database for future reference and continuous improvement.
- Tailored to support medical professionals, particularly in resource-limited settings.

## Dataset and Weights
[Link to Dataset and the weights (around 400MB)](https://mega.nz/folder/clUW1L6A#yDqIDsXTLVKPvUQKkzwp6g)

## How to Use
- Clone the yolov5 repository using the command
```bash
git clone https://github.com/ultralytics/yolov5  # clone
cd yolov5
pip install -r requirements.txt  # install
```
- Extract the dataset.zip file into a folder named dataset in the same directory as your workspace
- In ```genome_detection.py``` change the path in the line ```model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp6/weights/best.pt')``` to the weights provided
- Make directories in the workspace using command
```bash
mkdir static instance
cd static
mkdir detected_images
```
- Run ```app.py``` and open the localhost:port displayed in the terminal (NOTE: This is just a demo app and hence will boot in DEBUG mode)
- The login is currently set to Username:```admin``` and Password:```lovepython```
- From here you can select any image provided in test/images in dataset.zip
- You can also check the history by going to ```localhost:port/results``` and logout from your session using ```localhost:port/logout```


## Credits
- YOLOv5 for the object detection framework, allowing CAKES to provide fast and accurate chromosome analysis.
