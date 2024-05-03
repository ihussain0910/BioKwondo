# BioKwondo: Biomechanical Feedback System for Taekwondo

## Overview
BioKwondo leverages advanced pose estimation and deep learning technologies to provide real-time biomechanical feedback for Taekwondo practitioners. By analysing techniques and offering corrections, BioKwondo enhances the precision and accuracy of Taekwondo forms, making it a valuable tool for athletes of all levels.

![BioKwondo GIF](https://github.com/ihussain0910/BioKwondo/blob/main/BioKwondo%20Demo%20GIF.gif)

To see BioKwondo in action, watch the demonstration video here:
![BioKwondo Demo](https://github.com/ihussain0910/BioKwondo/blob/main/BioKwondo%20Demo.mp4)

Please note once the feedback is being said to the user the live feed freezes until the feedback is completed. The video demonstrates good starting position and chambering but incorrect arm placement at the end of the block.
## Features
- **Real-time Feedback**: Immediate analysis and feedback on Taekwondo techniques.
- **Pose Estimation**: Utilises single-view markerless 3D pose estimation to track movements.
- **Custom LSTM Models**: Deep learning models that provide detailed feedback for technique improvement.

## Repository Structure
```
BioKwondo/
│
├── biokwondo.py # Main script for running the BioKwondo application
├── feedback_generation.py # Handles the generation of feedback based on model predictions
├── mp_helpers.py # Helper functions for MediaPipe operations
└── Models/ # Trained models for action recognition and feedback generation
```

## Installation
To get started with BioKwondo, follow these steps:

1. **Clone the Repository**
2. **Navigate to the BioKwondo Directory**
3. **Install Dependencies**
Ensure you have Python installed, and then install the required packages
```pip install -r requirements.txt```


## Usage
To use BioKwondo, run the main script from the command line:
```python biokwondo.py```

Ensure your webcam is connected and properly configured for real-time pose estimation.

## MediaPipe

This project uses MediaPipe for Pose estimation and follows the functions and pre-processing outlined in https://developers.google.com/mediapipe

```
Camillo Lugaresi, Jiuqiang Tang, Hadon Nash, Chris McClanahan, Esha Uboweja,
Michael Hays, Fan Zhang, Chuo-Ling Chang, Ming Guang Yong, Juhyun Lee,
et al . 2019. Mediapipe: A framework for building perception pipelines. arXiv
preprint arXiv:1906.08172 (2019)
```
