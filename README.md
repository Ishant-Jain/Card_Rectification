# Card Rectification
A Python-based tool to automatically detect, crop, and rectify (deskew) ID cards from images, even when they are captured at an angle or with perspective distortion. Supports transparent background processing using rembg and OpenCV.

## 🚀 Features
1. Automatic background removal (supports transparent PNGs)
2. Crops ID cards precisely based on transparency
3. Corrects warped or tilted ID cards using perspective transformation
4. Easy to integrate into existing ID card processing pipelines


## ⚙️ Installation
pip install -r requirements.txt

python rectify.py <input_file_path> <filename>

**The output will be stored in a folder named cropped.


## 🔮 What's Coming Next
1. 📦 Batch processing for multiple images in one go
2. 🧠 Improved corner detection using deep learning (for complex cases)
3. 📂 GUI-based tool for easier manual adjustments (optional)

