import sys
from PyQt5.QtCore import*
from PyQr5.QtWidgets import*

class MaWindow(QMainWindow):

    def __init__(self, parent = None):
        super(MaWindow, self).__init__(parent)
        self.show()

def main(args):
    print("main")
    app = QApplication(args)
    mainw = MaWindow()
    app.exec()

if __name__ == "__main__":
    print("__main__")
    main(sys.argv)
