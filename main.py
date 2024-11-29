import sys
import random
from PyQt5 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Окружности")
        self.setGeometry(100, 100, 600, 400)

        # Центральный виджет
        self.centralwidget = QtWidgets.QWidget(self)
        self.setCentralWidget(self.centralwidget)

        # Кнопка "Добавить круг"
        self.pushButton = QtWidgets.QPushButton("Добавить круг", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(250, 350, 100, 30))
        self.pushButton.clicked.connect(self.add_circle)

        # Список для хранения окружностей
        self.circles = []

    def add_circle(self):
        """Добавляет окружность случайного размера и позиции"""
        diameter = random.randint(20, 100)
        x = random.randint(50, 550)
        y = random.randint(50, 300)
        self.circles.append((diameter, x, y))
        self.update()

    def paintEvent(self, event):
        """Рисует окружности на форме"""
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtGui.QColor(255, 255, 0))  # Желтый цвет

        for diameter, x, y in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
