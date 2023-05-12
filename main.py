import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QPixmap
from home import Ui_MainWindow


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        self.uic.open_file.triggered.connect(self.open_file)

    def show(self):
        self.main_win.show()

    def open_file(self):
        file = QFileDialog.getOpenFileName(filter="*.jpg *.png *.jpeg")
        self.uic.label.setPixmap(QPixmap(file[0]))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
