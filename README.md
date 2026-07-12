# Object Detection and Tracking System

A real-time Object Detection and Tracking System built using YOLOv8 and DeepSORT. The project supports both video files and live camera input through a simple graphical user interface (GUI).

## Features

- Real-time Object Detection using YOLOv8
- Multi-Object Tracking using DeepSORT
- Unique ID assignment for tracked objects
- Object class labeling
- Person counting
- Car counting
- Video file support
- Live camera support
- Output video saving
- Simple GUI using Tkinter

## Technologies Used

- Python
- YOLOv8 (Ultralytics)
- DeepSORT
- OpenCV
- Tkinter

## Project Structure

```text
CodeAlpha_Object_Detection_Tracking

├── main.py
├── tracking.py
├── requirements.txt
├── videos/
├── outputs/
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Project

```bash
python main.py
```

## How It Works

1. Select a video file or camera input.
2. YOLOv8 detects objects in each frame.
3. DeepSORT tracks detected objects across frames.
4. Each object receives a unique tracking ID.
5. Person and car counts are displayed.
6. The processed video is saved automatically.
