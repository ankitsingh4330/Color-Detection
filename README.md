🎨 Multi Color Detection using OpenCV
📌 Overview

This project is a real-time multi-color detection system built using Python and OpenCV. It captures video from a webcam and detects different colors by converting the image into HSV format and applying color masks.

🚀 Features
Real-time webcam color detection
Detects multiple colors (Red, Yellow, Blue)
Easy to extend for more colors (Green, Black, White, etc.)
Draws bounding boxes around detected objects
Displays color names on screen
🛠️ Technologies Used
Python
OpenCV (cv2)
NumPy
📂 Project Structure
colordetection.py    # Main script for color detection
README.md            # Project documentation
▶️ How It Works
Captures video from the webcam
Converts frame from BGR to HSV color space
Defines HSV ranges for different colors
Creates masks for each color
Detects contours in each mask
Draws bounding boxes and labels for detected colors
⚙️ Installation
1. Install Dependencies
pip install opencv-python numpy
2. Run the Program
python colordetection.py
🎮 Controls
Press ESC key to exit the application
🎯 Supported Colors

Currently enabled:

Red
Yellow
Blue

Additional colors (can be enabled in code):

Green
Black
White
Gray
Orange
⚠️ Limitations
Lighting conditions affect accuracy
Similar shades may cause incorrect detection
Requires proper HSV tuning for better results
💡 Future Improvements
Add trackbars to adjust HSV values dynamically
Detect more precise shades
Integrate object tracking with color detection
Save detected color data
