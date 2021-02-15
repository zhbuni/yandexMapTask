import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit

from mapclass import *

SCREEN_SIZE = [600, 600]


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.app = YandexMap([55, 55], (1, 1))
        self.initUI()
        self.schemas = ['map', 'sat', 'sat,skl']
        self.index_of_schema = 0

    def getImage(self):
        self.map_file = self.app.get_map()
        self.pixmap.loadFromData(self.map_file)
        self.image.setPixmap(self.pixmap)

    def initUI(self):
        self.setGeometry(100, 100, *SCREEN_SIZE)
        self.setWindowTitle('Отображение карты')

        # Инициализация изображения
        self.pixmap = QPixmap()
        self.image = QLabel(self)
        self.getImage()
        self.pixmap.loadFromData(self.map_file)
        self.image.move(0, 40)
        self.image.resize(600, 450)
        self.image.setPixmap(self.pixmap)

        # Инициализация кнопки смены схемы
        self.change_schema_button = QPushButton(self)
        self.change_schema_button.move(10, 500)
        self.change_schema_button.resize(120, 20)
        self.change_schema_button.setText('Поменять схему')
        self.change_schema_button.clicked.connect(self.change_schema)

        # кнопки, отвечающие за смещение карты. Пришлось сделать кнопками, так как прекрасный qt не может адекватно
        # обрабатывать нажатия, если в окне есть поле для ввода.
        self.move_map_up_btn = QPushButton(self)
        self.move_map_up_btn.move(500, 500)
        self.move_map_up_btn.resize(40, 40)
        self.move_map_up_btn.setText('Up')
        self.move_map_up_btn.clicked.connect(self.move_map)

        self.move_map_down_btn = QPushButton(self)
        self.move_map_down_btn.move(500, 540)
        self.move_map_down_btn.resize(40, 40)
        self.move_map_down_btn.setText('Down')
        self.move_map_down_btn.clicked.connect(self.move_map)

        self.move_map_left_btn = QPushButton(self)
        self.move_map_left_btn.move(460, 540)
        self.move_map_left_btn.resize(40, 40)
        self.move_map_left_btn.setText('Left')
        self.move_map_left_btn.clicked.connect(self.move_map)

        self.move_map_right_btn = QPushButton(self)
        self.move_map_right_btn.move(540, 540)
        self.move_map_right_btn.resize(40, 40)
        self.move_map_right_btn.setText('Right')
        self.move_map_right_btn.clicked.connect(self.move_map)

        # Инициализация поля ввода
        self.toponym = QLineEdit(self)
        self.toponym.move(10, 10)
        self.toponym.resize(200, 20)

        # Инициализация кнопки поиска
        self.find_toponym_button = QPushButton(self)
        self.find_toponym_button.move(220, 10)
        self.find_toponym_button.resize(70, 20)
        self.find_toponym_button.setText('Искать')
        self.find_toponym_button.clicked.connect(self.find_toponym)

    # Метод поиска топонима и его вывода на экран
    def find_toponym(self):
        text = self.toponym.text()
        if text:
            coords = [float(el) for el in self.app.find_object(text).split()]
            self.app.set_centercoords(coords)
            self.app.add_point(coords)
            self.getImage()

    # Метод для смены схемы
    def change_schema(self):
        self.index_of_schema = (self.index_of_schema + 1) % len(self.schemas)
        self.app.change_type(self.schemas[self.index_of_schema])
        self.getImage()

    # метод для смещения карты
    def move_map(self):
        sender = self.sender().text()
        if sender == 'Left':
            lon = self.app.centercoords[0] - int(self.app.scale[0]) * 0.0051 * 600
            self.app.set_centercoords([lon, self.app.centercoords[1]])
            self.getImage()
        if sender == 'Up':
            lat = self.app.centercoords[1] + int(self.app.scale[0]) * 0.00286 * 450
            self.app.set_centercoords([self.app.centercoords[0], lat])
            self.getImage()
        if sender == 'Right':
            lon = self.app.centercoords[0] + int(self.app.scale[0]) * 0.0051 * 600
            self.app.set_centercoords([lon, self.app.centercoords[1]])
            self.getImage()
        if sender == 'Down':
            lat = self.app.centercoords[1] - int(self.app.scale[0]) * 0.00286 * 450
            self.app.set_centercoords([self.app.centercoords[0], lat])
            self.getImage()

    # Обработка кнопок
    def keyPressEvent(self, event):
        # масштабирование карты на нажатия pg up/pg down
        if event.key() == 16777238:
            self.app.set_scale((self.app.scale[0] + 1, self.app.scale[1] + 1))
            self.getImage()
        if event.key() == 16777239:
            self.app.set_scale((self.app.scale[0] - 1, self.app.scale[1] - 1))
            self.getImage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
