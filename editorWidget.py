import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class noteWidget(QWidget):
    def __init__(self, title, texte):

        self.title = title
        self.texte = texte

        self.initUI(self)

    def initUI(self):

        self.label = QLabel(self)
        self.label.setText(self.title)
        self.show()


    def mousePressEvent(self, event):

        drag = QDrag()
        pix_map = QPixmap()
        mime_data = QMimeData()
        mime_data.setHtml(self.texte)
        drag.setMimeData(mime_data)
        drag.exec_()


class plainTextEdit(QPlainTextEdit):

    def __init__(self):

        super().__init__()
        self.initUi()

    def initUI(self):
         self.setAcceptDrops(True)

    def dragMoveEvent(self, event):
        pass

    def dragEnterEvent(self, event):
        if event.mimeData().hasHtml():
            event.accept()
        else:
            event.ignore()