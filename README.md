
# FrameSnap 🎥

A simple Python GUI tool to extract frames from video files using PyQt5 and OpenCV.

## 🚀 Features

* **GUI Interface:** Easy-to-use interface with a real-time preview.
* **Format Support:** Supports `.mp4`, `.avi`, `.mkv`, and `.mov` files.
* **Frame Navigation:** Precise frame selection using a slider.
* **Instant Save:** Saves the selected frame as a high-quality `.jpg` image.
* **Auto-Path:** Automatically saves images to your **Desktop**.

## 🛠️ Requirements

* Python 3.x
* PyQt5
* OpenCV (`opencv-python`)

## 📦 Installation

1.  **Clone the repository** (or download the script):
    ```bash
    git clone [https://github.com/Enesbicer/FrameSnap.git]
    cd FrameSnap
    ```

2.  **Install the required libraries:**
    You can install the dependencies using pip:
    ```bash
    pip install PyQt5 opencv-python
    ```

## ▶️ Usage

1.  Run the script:
    ```bash
    python main.py
    ```
    *(Note: Replace `main.py` with the actual name of your python file if it is different).*

2.  Click **"Open Video"** to select a video file.
3.  Use the **Slider** at the bottom to scroll through the video frames.
4.  When you find the frame you want, click **"Save Frame"**.
5.  The image will be saved to your **Desktop** as `frame_X.jpg`.

## 📝 License

This project is open-source and available for personal or educational use.
