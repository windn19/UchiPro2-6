import sys

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import uic


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('../files/newform1.ui', self)
        # self.nameEdit.setText('Hello!!!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
