# Indian Automatic Number Plate Recognition (ANPR) System

A real-time Automatic Number Plate Recognition (ANPR) pipeline tailored specifically for Indian vehicle license plates. This system utilizes a fast LBP (Local Binary Patterns) Cascade Classifier via OpenCV for plate detection and EasyOCR for alpha-numeric text extraction.

---

## Features

- Real-time Detection: High-speed rectangular bounding-box plotting around vehicle plates.
- High-Accuracy OCR: Leveraging EasyOCR models to accurately clean up and display Indian registration text (e.g., HR 98 AA 7777).
- Live Terminal Output: Instantly prints the detected registration plate alongside its confidence score.

---

## Tech Stack

- Python 3
- OpenCV (opencv-contrib-python) – Computer Vision & LBP Object Detection
- EasyOCR – Text Recognition Framework (PyTorch)

---

## Installation & Setup

1. Clone the Repository:
   git clone [https://github.com/Macro6969/realtime-number-plate-ocr.git](https://github.com/Macro6969/realtime-number-plate-ocr.git)
   cd realtime-number-plate-ocr

2. Set up a Virtual Environment:
   python -m venv env
   source env/bin/activate # On Windows use: env\Scripts\activate

3. Install Dependencies:
   pip install -r requirements.txt

4. Run the Application:
   python app.py

---

## Configuration Tips

- If the green box is flickering or missing your plate, adjust the minNeighbors and scaleFactor parameters inside detectMultiScale in app.py.
- Wireless Webcam Testing: You can stream a high-resolution feed from your smartphone (using apps like DroidCam/IP Webcam) directly into the script by updating the cv2.VideoCapture() source to your phone's network URL string.

---

## License & Credits

- The XML classifier uses Local Binary Patterns trained for community-driven Indian license plate tracking. Open-source for educational and non-commercial portfolios.
