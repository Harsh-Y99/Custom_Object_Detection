Custom Object Detection Using YOLOv8
Overview

This project implements a custom object detection system using the YOLOv8 framework. The objective was to design, train, and deploy a real-time object detection pipeline on a custom dataset, while ensuring compatibility with low-end, CPU-only hardware.

The project demonstrates a complete computer vision workflow — from dataset integration and model training to live webcam inference and performance evaluation — packaged in a clean, reproducible, and GitHub-ready structure.

Objectives

Train a YOLOv8 model on a custom dataset

Perform real-time object detection using a webcam

Ensure stable and usable performance on a CPU-only system

Analyze training quality and inference behavior

Deliver a clean, reproducible solution for evaluation

Dataset Description

The dataset was sourced from Roboflow and formatted in a YOLOv8-compatible structure.

Object Classes

Car

Cat

Dog

Person

The dataset includes training and validation splits with bounding box annotations provided in YOLO format.
All labels were verified during training using YOLO’s built-in label scanning and visualization tools.

Model and Training Approach

Framework: Ultralytics YOLOv8

Model Variant: YOLOv8 Nano (yolov8n)

Training Device: CPU only

Image Resolution: 640 × 640

Epochs: Initially 20, later increased to improve stability

YOLOv8 Nano was selected to balance speed, model size, and accuracy, making it suitable for low-resource systems.

Challenges Faced and Solutions
1. Training Feedback Not Visible

Problem:
Initial training runs did not display clear logs or progress information.

Cause:
Incorrect YOLO CLI argument formatting.

Solution:
Correct training commands were applied, enabling detailed epoch-wise logs, loss values, and validation metrics.

2. Unstable and Laggy Webcam Inference

Problem:
Live webcam inference suffered from lag, delayed bounding boxes, and unstable detections.

Identified Causes:

CPU-only inference

Limited dataset size

Low confidence threshold

Unoptimized inference loop

Solutions Implemented:

Switched to YOLOv8 Nano

Increased training epochs

Adjusted confidence threshold

Reduced unnecessary frame processing

Result:
Detection became smoother and more stable for real-time usage.

3. Low Initial Accuracy Metrics

Problem:
Early training runs showed low mAP scores and inconsistent predictions.

Cause:
Small dataset size and insufficient training epochs.

Solution:
Training duration was increased and dataset labels were rechecked.
Although absolute accuracy is constrained by dataset size, detection reliability improved significantly.

Performance on Low-End Hardware

This project was executed entirely on a low-end laptop, demonstrating real-world feasibility.

System Configuration:

Intel i3 (7th Gen) CPU

12 GB RAM

No dedicated GPU

Ubuntu Linux

Despite these limitations, the model was successfully trained and deployed for real-time webcam inference.

Results and Outputs

YOLOv8 automatically generated the following training artifacts:

Training and validation loss curves

mAP evaluation graphs

Label distribution visualizations

Best and last model weights

These artifacts are included in the repository for training verification and analysis.

Sample Results and Visualizations

Images are stored in the assets/ directory.

## Training Visualizations

<p align="center">
  <img src="Outputs/train_batch2.jpg" width="700">
</p>

<p align="center">
  <img src="Outputs/labels.jpg" width="700">
</p>

---

## Real-Time Detection Results

<p align="center">
  <img src="Outputs/Screenshot from 2026-01-11 14-49-34.png" width="700">
</p>

<p align="center">
  <img src="Outputs/Screenshot from 2026-01-11 14-51-30.png" width="700">
</p>

<p align="center">
  <img src="Outputs/Screenshot from 2026-01-11 14-51-53.png" width="700">
</p>

Project Status

Custom dataset successfully trained

Real-time webcam detection operational

Model performance stabilized through tuning

Repository structured for reproducibility

Ready for review and evaluation

Notes for Reviewers

This project prioritizes practical deployment on constrained hardware rather than maximum accuracy.
All design choices reflect real-world trade-offs between performance, stability, and computational resources.

Video sample link to Google drive 
https://drive.google.com/file/d/1rdWkXazXfkJLKpfUbgYL5JBNbViZUNPx/view?usp=drive_link
