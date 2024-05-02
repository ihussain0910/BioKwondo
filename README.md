# BioKwondo: Biomechanical Feedback System for Taekwondo

## Overview
BioKwondo leverages advanced pose estimation and deep learning technologies to provide real-time biomechanical feedback for Taekwondo practitioners. By analysing techniques and offering corrections, BioKwondo enhances the precision and accuracy of Taekwondo forms, making it a valuable tool for athletes of all levels.

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
Ensure you have Python installed, and then install the required packages from requirements.txt:


## Usage
To use BioKwondo, run the main script from the command line:
python biokwondo.py

Ensure your webcam is connected and properly configured for real-time pose estimation.
