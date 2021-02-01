import os
import sys
from mapclass import *


from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

SCREEN_SIZE = [600, 450]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.app = YandexMap((55, 55), (1, 1))
        self.getImage()
        self.initUI()

    def getImage(self):
        self.map_file = self.app.get_map()

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        self.pixmap = QPixmap()
        self.pixmap.loadFromData(self.map_file)
        self.image = QLabel(self)
        self.image.move(0, 0)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

    def keyPressEvent(self, event):
        if event.key() == 16777238:
            self.app.set_scale((self.app.scale[0] + 1, self.app.scale[1] + 1))
            self.getImage()
            self.pixmap.loadFromData(self.map_file)
            self.image.setPixmap(self.pixmap)
        if event.key() == 16777239:
            self.getImage()
            self.pixmap.loadFromData(self.map_file)
            self.app.set_scale((self.app.scale[0] - 1, self.app.scale[1] - 1))
            self.image.setPixmap(self.pixmap)
        print(self.app.scale)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())