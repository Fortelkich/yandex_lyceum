from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QLabel, QGridLayout
import random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
from tkinter import Tk, Canvas, Frame, BOTH
import sys


class show_receipt(QMainWindow, QDialog):
    def __init__(self, parent=None):
        super().__init__()
        uic.loadUi('Git_and_yellow_circles.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, e):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawRectangles(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def drawRectangles(self, qp):
        razmer = random.randint(1, 500)
        mesto = random.randint(1, 50)

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(mesto, mesto, razmer, razmer)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = show_receipt()
    calc.show()
    sys.exit(app.exec())