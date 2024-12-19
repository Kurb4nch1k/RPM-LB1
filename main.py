import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QFileDialog
from PyQt6.QtGui import QImage, QPixmap, QColor, QTransform
from PyQt6.QtCore import Qt


class ImageEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image, self.display_image_copy = None, None
        self.current_color_channel = None

        self.setup_ui()

    def setup_ui(self):
        main_layout = QHBoxLayout()
        left_layout = QVBoxLayout()
        left_layout.addWidget(self.image_label)

        load_button = QPushButton("Загрузить изображение", self)
        load_button.clicked.connect(self.load_image)
        left_layout.addWidget(load_button)

        self.transparency_slider = QSlider(Qt.Orientation.Horizontal, self)
        self.transparency_slider.setRange(0, 100)
        self.transparency_slider.setValue(100)
        self.transparency_slider.valueChanged.connect(self.update_transparency)
        left_layout.addWidget(self.transparency_slider)

        rotate_layout = QHBoxLayout()
        for label, action in [("Повернуть влево", self.rotate_left), ("Повернуть вправо", self.rotate_right)]:
            button = QPushButton(label, self)
            button.clicked.connect(action)
            rotate_layout.addWidget(button)
        left_layout.addLayout(rotate_layout)

        right_layout = QVBoxLayout()
        for label, channel in [("Все каналы", None), ("Красный", "red"), ("Зеленый", "green"), ("Синий", "blue")]:
            button = QPushButton(label, self)
            button.clicked.connect(lambda checked, ch=channel: self.set_color_channel(ch))
            right_layout.addWidget(button)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)
        self.setLayout(main_layout)

        self.setWindowTitle('Image Editor')
        self.resize(800, 600)

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Загрузить изображение", "", "Images (*.png *.xpm *.jpg *.bmp)")
        if file_name:
            self.image = QImage(file_name)
            self.display_image_copy = self.image.copy()
            self.update_image()

    def update_image(self):
        if self.image:
            pixmap = QPixmap.fromImage(self.image)
            self.image_label.setPixmap(pixmap)

    def update_transparency(self):
        if self.image:
            alpha = self.transparency_slider.value() / 100
            img = self.image.copy()
            for x in range(img.width()):
                for y in range(img.height()):
                    color = QColor(img.pixel(x, y))
                    color.setAlpha(int(color.alpha() * alpha))
                    img.setPixel(x, y, color.rgba())
            self.image_label.setPixmap(QPixmap.fromImage(img))

    def rotate_image(self, angle):
        if self.image:
            self.image = self.image.transformed(QTransform().rotate(angle))
            self.apply_color_channel()

    def rotate_left(self):
        self.rotate_image(-90)

    def rotate_right(self):
        self.rotate_image(90)

    def apply_color_channel(self):
        if self.current_color_channel == "red":
            self.show_color_channel(lambda color: QColor(color.red(), 0, 0, color.alpha()))
        elif self.current_color_channel == "green":
            self.show_color_channel(lambda color: QColor(0, color.green(), 0, color.alpha()))
        elif self.current_color_channel == "blue":
            self.show_color_channel(lambda color: QColor(0, 0, color.blue(), color.alpha()))
        else:
            self.update_image()

    def show_color_channel(self, color_func):
        img = self.image.copy()
        for x in range(img.width()):
            for y in range(img.height()):
                color = QColor(img.pixel(x, y))
                img.setPixel(x, y, color_func(color).rgba())
        self.image_label.setPixmap(QPixmap.fromImage(img))

    def set_color_channel(self, channel):
        self.current_color_channel = channel
        self.apply_color_channel()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    editor = ImageEditor()
    editor.show()
    sys.exit(app.exec())

