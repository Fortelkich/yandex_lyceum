from PyQt5.QtWidgets import QMainWindow
import random
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
import sys
from Git_and_yellow_circles1 import Ui_Dialog


class show_receipt(QMainWindow, Ui_Dialog):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
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
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        col = QColor(0, 0, 0)
        col.setNamedColor('#d4d4d4')
        qp.setPen(col)

        qp.setBrush(QColor(r, g, b))
        qp.drawEllipse(mesto, mesto, razmer, razmer)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = show_receipt()
    calc.show()
    sys.exit(app.exec())