import sys

from data.designs.main_window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication


morze_alphabet = {
    'а': '.-',
    'б': '-...',
    'в': '.--',
    'г': '--.',
    'д': '-..',
    'е': '.',
    'ё': '.',
    'ж': '...-',
    'з': '--..',
    'и': '..',
    'й': '.---',
    'к': '-.-',
    'л': '.-..',
    'м': '--',
    'н': '-.',
    'о': '---',
    'п': '.--.',
    'р': '.-.',
    'с': '...',
    'т': '-',
    'у': '..-',
    'ф': '..-.',
    'х': '....',
    'ц': '-.-.',
    'ч': '---.',
    'ш': '----',
    'щ': '--.-',
    'ъ': '.--.-.',
    'ы': '-.--',
    'ь': '-..-',
    'э': '...-...',
    'ю': '..--',
    'я': '.-.-'
}


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        msg = ''
        for i in self.input_text.toPlainText():
            if i.lower() in morze_alphabet:
                msg += morze_alphabet[i.lower()] + ' '
            elif i == ' ':
                msg += '  '
            else:
                msg += i
        msg.strip()
        self.output_text.setPlainText(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
