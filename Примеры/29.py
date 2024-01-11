import sys

from PyQt6.QtWidgets import QWidget, QApplication
from files.reg1 import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
