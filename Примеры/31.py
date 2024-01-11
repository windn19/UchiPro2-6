import sys

from PyQt6.QtWidgets import QWidget, QApplication, QListWidgetItem
from files.registration import Ui_Form


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addButton.clicked.connect(self.addItem)
        self.deleteButton.clicked.connect(self.deleteItem)
        self.gender.addItems(['муж', 'жен'])
        self.items = []

    def addItem(self):
        name = self.nameEdit.text()
        gender = self.gender.currentText()
        date = self.dateEdit.date().toString('dd.MM.yyyy')
        self.items.append((name, gender, date))
        self.updateList()

    def deleteItem(self):
        index = self.listWidget.currentRow()
        if index != -1:
            del self.items[index]
        self.updateList()

    def updateList(self):
        self.listWidget.clear()
        for item in self.items:
            self.listWidget.addItem(QListWidgetItem(', '.join(item)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
