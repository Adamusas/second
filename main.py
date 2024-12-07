import sys
import random
from PyQt6 import QtCore, QtGui, QtWidgets, uic


class CircleWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        diameter = random.randint(20, 100)
        painter = QtGui.QPainter(self)
        painter.setBrush(QtGui.QColor(255, 255, 0))
        painter.drawEllipse(0, 0, diameter, diameter)

    def add_circle(self):
        self.update()


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)

        self.circle_widget = CircleWidget()

        layout = self.findChild(QtWidgets.QVBoxLayout,
                                "verticalLayout")
        if layout is not None:
            layout.addWidget(self.circle_widget)
        else:
            print("Компоновщик не найден")

        if hasattr(self, 'pushButton'):
            self.pushButton.clicked.connect(self.circle_widget.add_circle)
        else:
            print("Кнопка pushButton не найдена в UI")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Circle Drawer")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
