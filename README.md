# 🔥 Fire Detection System using OpenCV + DroidCam

<p align="center">
  <img src="https://img.shields.io/badge/Project-Fire_Detection-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-blue?style=for-the-badge&logo=opencv" />
  <img src="https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

---

## 🧯 Project Overview

This project is a **Real-Time Fire Detection System** that uses:

- 📷 **DroidCam** (Mobile camera as IP webcam)  
- 🧠 **OpenCV** (Image processing)  
- 🔊 **Pygame** (Alarm system)  

It detects **fire-like colors in live video feed** and triggers an **alert sound automatically**.

---

# Fire Detection System using OpenCV + DroidCam

## Project Overview
This project is a real-time fire detection system using:
- DroidCam (mobile camera)
- OpenCV (image processing)
- Pygame (alarm sound)

It detects fire-like colors in a live video feed and triggers an alarm.

## Features
- Real-time fire detection
- Uses mobile camera over WiFi
- HSV color-based detection
- Automatic alarm system
- Lightweight and fast

## Working
Camera Feed → HSV Conversion → Color Masking → Contour Detection → Area Check → Fire Detection → Alarm

## Detection Logic
- HSV range:
  Lower: [10, 100, 100]
  Upper: [30, 255, 255]
- Contour area threshold: 1000
- If area exceeds threshold → Fire detected

## Installation
Run:
pip install opencv-python numpy pygame

## Setup
1. Install DroidCam on your phone
2. Connect phone and laptop to same WiFi
3. Update IP in code:
   DROIDCAM_URL = "http://192.168.1.8:4747/video"
4. Add alarm file:
   ooo.mp3

## Run
python fire_detection.py

Press Q to exit.

## Output
- "FIRE DETECTED!" message on screen
- Red bounding box on detected region
- Alarm sound plays

## Demo (LinkedIn)
https://www.linkedin.com/posts/nikhil-kushwah-664304218_fire-detector-activity-7359463770810658818-OxFC?utm_source=share&utm_medium=member_desktop&rcm=ACoAADbcwqwBmaWPICVZ41SWioXWKvjFBQHsI24

## Project Structure
Fire-Detection-System/
 ├── fire_detection.py
 ├── ooo.mp3
 └── README.txt

## Limitations
- May detect similar colors (false positives)
- Sensitive to lighting conditions
- Not suitable for industrial use

## Future Improvements
- AI-based detection (YOLO)
- Smoke detection
- IoT alerts
- Fire intensity analysis

## Author
Nikhil Kushwah
Electrical Engineering Student

## Support
- Star the repo
- Share the project
- Suggest improvements
