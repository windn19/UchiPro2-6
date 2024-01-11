import sys

from PyQt6.QtWidgets import QWidget, QApplication
from design import Ui_Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.checkText)

    def checkText(self):
        text = self.textEdit.toPlainText()
        length = len(text)
        letters = len(list(filter(str.isalpha, text)))
        words = text.count(' ')
        self.lineEdit.setText(str(length))
        self.lineEdit_2.setText(str(letters))
        self.lineEdit_3.setText(str(words))


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    auth = Window()
    auth.show()
    sys.exit(app.exec())
