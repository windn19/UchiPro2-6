import sys

from PyQt6.QtWidgets import QWidget, QApplication
from design import Ui_Form

EXCHANGE_RATE = 90


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.rubToDol)
        self.pushButton_2.clicked.connect(self.dolToRub)

    def rubToDol(self):
        value = self.rubEdit.value()
        self.dollars.setText(str(value / EXCHANGE_RATE))

    def dolToRub(self):
        value = self.dolEdit.value()
        self.rubles.setText(str(value * EXCHANGE_RATE))


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    auth = Window()
    auth.show()
    sys.exit(app.exec())
