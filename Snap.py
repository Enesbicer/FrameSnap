import sys
import cv2
from pathlib import Path
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel,
    QSlider, QFileDialog, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap


class FrameExtractor(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Video Frame Extractor with Preview")
        self.setGeometry(300, 200, 800, 600)

        self.cap = None
        self.total_frames = 0
        self.current_frame = None

        layout = QVBoxLayout()

        self.info_label = QLabel("Select a video file")
        layout.addWidget(self.info_label)

        self.preview_label = QLabel("Frame Preview")
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.preview_label.setFixedHeight(400)
        self.preview_label.setStyleSheet(
            "background-color: #222; color: white;"
        )
        layout.addWidget(self.preview_label)

        self.slider_label = QLabel("Selected frame: 0")
        layout.addWidget(self.slider_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setEnabled(False)
        self.slider.valueChanged.connect(self.slider_changed)
        layout.addWidget(self.slider)

        self.open_btn = QPushButton("Open Video")
        self.open_btn.clicked.connect(self.open_video)
        layout.addWidget(self.open_btn)

        self.save_btn = QPushButton("Save Frame")
        self.save_btn.setEnabled(False)
        self.save_btn.clicked.connect(self.save_frame)
        layout.addWidget(self.save_btn)

        self.setLayout(layout)

    def open_video(self):
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open Video",
            "",
            "Video Files (*.mp4 *.avi *.mkv *.mov)"
        )

        if not path:
            return

        self.cap = cv2.VideoCapture(path)
        if not self.cap.isOpened():
            self.info_label.setText("Failed to open video")
            return

        self.total_frames = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))

        self.slider.setEnabled(True)
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.total_frames - 1)
        self.save_btn.setEnabled(True)

        self.info_label.setText(f"Total frames: {self.total_frames}")

        self.show_frame(0)

    def slider_changed(self, value):
        self.slider_label.setText(f"Selected frame: {value}")
        self.show_frame(value)

    def show_frame(self, frame_no):
        if not self.cap:
            return

        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_no)
        ret, frame = self.cap.read()

        if not ret:
            return

        self.current_frame = frame

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w

        qt_image = QImage(
            rgb.data,
            w,
            h,
            bytes_per_line,
            QImage.Format_RGB888
        )

        pixmap = QPixmap.fromImage(qt_image)
        pixmap = pixmap.scaled(
            self.preview_label.width(),
            self.preview_label.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.preview_label.setPixmap(pixmap)

    def save_frame(self):
        if self.current_frame is None:
            return

        frame_no = self.slider.value()
        output = Path.home() / "Desktop" / f"frame_{frame_no}.jpg"
        cv2.imwrite(str(output), self.current_frame)

        self.info_label.setText(f"Frame saved: {output}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FrameExtractor()
    window.show()
    sys.exit(app.exec_())
