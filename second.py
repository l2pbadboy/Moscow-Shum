import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt


class CircleWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Рисование круга")
        self.setGeometry(100, 100, 400, 400)

        self.button = QPushButton("Нарисовать круг", self)
        self.button.clicked.connect(self.draw_circle)
        self.button.setGeometry(10, 380, 380, 20)

        self.diameter = 0


    def draw_circle(self):
        self.diameter = random.randint(0, 390)
        self.update()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))
        x = (self.width() - self.diameter) // 2
        y = (self.height() - self.diameter) // 2
        painter.drawEllipse(x, y, self.diameter, self.diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircleWidget()
    window.show()
    sys.exit(app.exec())
