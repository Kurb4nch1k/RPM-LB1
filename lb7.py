import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox


class RandomNumberGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Генератор случайных чисел")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.label_start = QLabel("Начало диапазона:")
        self.input_start = QLineEdit()
        layout.addWidget(self.label_start)
        layout.addWidget(self.input_start)

        self.label_end = QLabel("Конец диапазона:")
        self.input_end = QLineEdit()
        layout.addWidget(self.label_end)
        layout.addWidget(self.input_end)

        self.button_generate = QPushButton("Сгенерировать число")
        self.button_generate.clicked.connect(self.generate_random_number)
        layout.addWidget(self.button_generate)

        self.setLayout(layout)

    def generate_random_number(self):
        try:
            start = int(self.input_start.text())
            end = int(self.input_end.text())
            if start >= end:
                raise ValueError("Начало должно быть меньше конца.")

            random_number = random.randint(start, end)
            self.show_message(f"Сгенерированное число: {random_number}")

        except ValueError as e:
            self.show_message(f"Ошибка: {e}")

    def show_message(self, message):
        msg_box = QMessageBox()
        msg_box.setText(message)
        msg_box.setWindowTitle("Результат")
        msg_box.exec()


def main():
    app = QApplication(sys.argv)
    window = RandomNumberGenerator()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
