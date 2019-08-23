import sys
import PyQt5.sip
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QDialog
from start import Ui_Form


class MainWin(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWin, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWin()
    win.show()
    sys.exit(app.exec_())