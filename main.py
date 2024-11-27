from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from random import randint
from PyQt6.QtGui import QPainter, QColor
import sys


class YellowCircle(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Программа Максима Алябьева')
        self.pushButton.clicked.connect(self.update)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circle(qp)
        qp.end()

    def draw_circle(self, qp):
        qp.setBrush(QColor("yellow"))
        r = randint(0, self.width() // 4)
        qp.drawEllipse(QPoint(randint(0, self.width()), randint(0, self.height())), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = YellowCircle()
    form.show()
    sys.exit(app.exec())
