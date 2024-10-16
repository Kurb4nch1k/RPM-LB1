from PyQt6.QtWidgets import QWidget, QVBoxLayout, QApplication, QMainWindow, QPushButton, QLabel
from PyQt6.QtCore import Qt


class ClickerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 150)
        self.setWindowTitle("Кликер")
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        layout = QVBoxLayout()
        self.centralWidget.setLayout(layout)

        self.clicksLabel = QLabel("Кликните здесь!")
        layout.addWidget(self.clicksLabel)

        self.buttonClick = QPushButton("Нажмите!")
        self.buttonClick.clicked.connect(self.onButtonClick)
        layout.addWidget(self.buttonClick)

        self.counter = 0

    def onButtonClick(self):
        self.counter += 1
        self.clicksLabel.setText(f"Вы нажали {self.counter} раз!")


def main():
    app = QApplication([])
    window = ClickerApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
