import sys

from PyQt6.QtWidgets import QWidget, QApplication
from design import Ui_Form


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.progressBar.hide()
        self.pushButton.clicked.connect(self.solve)

    def solve(self):
        k = int(self.spinBox.text())
        self.progressBar.setMaximum(k)
        self.progressBar.show()
        self.listWidget.clear()
        count = 0
        number = 1
        while count < k:
            d = 2
            number += 1
            while d ** 2 <= number:
                if number % d == 0:
                    break
                d += 1
            else:
                self.listWidget.addItem(str(number))
                count += 1
            self.progressBar.setValue(count)
        self.progressBar.hide()


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    auth = Window()
    auth.show()
    sys.exit(app.exec())
