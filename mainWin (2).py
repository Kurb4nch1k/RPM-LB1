import sys, os
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QTextEdit, QLabel, QFileDialog, QMessageBox
from collections import Counter

class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.selected_file = None
        self.initUI()

    def initUI(self):
        self.resize(600, 400)
        self.setWindowTitle('Текстовый редактор')


        self.input_file = QLineEdit()
        new_file_button = QPushButton('Создать новый')
        save_button = QPushButton('Сохранить файл')
        open_button = QPushButton('Открыть файл')
        self.text = QTextEdit()


        self.num_symbols = QLabel('Количество символов: 0')
        self.num_words = QLabel('Количество слов: 0')
        self.largest_word = QLabel('Самое длинное слово: None')
        self.shortest_word = QLabel('Самое короткое слово: None')
        self.often_word = QLabel('Часто встречающееся слово: None')


        main_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.input_file)
        v_layout.addWidget(new_file_button)
        v_layout.addWidget(save_button)
        v_layout.addWidget(open_button)
        v_layout.addWidget(self.num_symbols)
        v_layout.addWidget(self.num_words)
        v_layout.addWidget(self.largest_word)
        v_layout.addWidget(self.shortest_word)
        v_layout.addWidget(self.often_word)

        main_layout.addLayout(v_layout)
        main_layout.addWidget(self.text)

        self.setLayout(main_layout)


        open_button.clicked.connect(self.select_file)
        save_button.clicked.connect(self.save_file)
        new_file_button.clicked.connect(self.new_file)

    def open_file(self):
        if self.selected_file:
            self.text.clear()
            try:
                with open(self.selected_file, 'r', encoding='utf-8') as file:
                    text = file.read()
                    self.text.setPlainText(text)
                    self.update_statistics(text)


                self.input_file.setText(os.path.basename(self.selected_file))
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось открыть файл: {e}")

    def update_statistics(self, text):
        words = text.split()
        num_words = len(words)
        length = len(text)

        if num_words > 0:
            max_word = max(words, key=len)
            min_word = min(words, key=len)
            word_counts = Counter(words)
            often_word = word_counts.most_common(1)[0][0]
        else:
            max_word = min_word = often_word = ""


        self.num_symbols.setText(f'Количество символов: {length}')
        self.num_words.setText(f'Количество слов: {num_words}')
        self.largest_word.setText(f'Самое длинное слово: {max_word}')
        self.shortest_word.setText(f'Самое короткое слово: {min_word}')
        self.often_word.setText(f'Часто встречающееся слово: {often_word}')

    def save_file(self):
        if self.input_file.text():
            try:
                with open(self.input_file.text(), 'w', encoding='utf-8') as file:
                    file.write(self.text.toPlainText())
                QMessageBox.information(self, "Сохранение", "Файл успешно сохранен!")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка", f"Не удалось сохранить файл: {e}")

    def new_file(self):
        self.text.clear()
        self.input_file.clear()
        self.selected_file = None
    def select_file(self):
        self.selected_file, _ = QFileDialog.getOpenFileName(self, 'Выберите текстовый файл', '',
                                                            'Text Files (*.txt);;All Files (*)')
        if self.selected_file:
            self.open_file()
def main():
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
