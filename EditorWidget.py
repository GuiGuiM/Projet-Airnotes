import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class NoteLabel(QLabel):
    def __init__(self, title, texte):

        super().__init__()

        self.title = title
        self.texte = texte

        self.initUI()

    def initUI(self):

        self.setText(self.title)
        self.show()


    def mousePressEvent(self, event):

        drag = QDrag(self)
        pix_map = QPixmap()
        mime_data = QMimeData()
        mime_data.setHtml(self.texte)
        drag.setMimeData(mime_data)
        drag.exec_()


class PlainTextEdit(QPlainTextEdit):

    def __init__(self):

        super().__init__()
        self.initUI()

    def initUI(self):
         self.setAcceptDrops(True)

    def dragMoveEvent(self, event):
        pass

    def dragEnterEvent(self, event):
        if event.mimeData().hasHtml():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.textCursor().insertHtml(event.mimeData().html())


class EditorWidget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUi()

    def initUi(self):

        grid = QGridLayout()
        self.setLayout(grid)

        plainTextEdit = PlainTextEdit()
        grid.addWidget(plainTextEdit, 0, 0)

        vlayout = QVBoxLayout()
        grid.addLayout(vlayout, 0, 1)
        note1 = NoteLabel("Title1", "blabla")
        note2 = NoteLabel("Title2", "<b>blabla</b>")
        vlayout.addWidget(note1)
        vlayout.addWidget(note2)

        self.show()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    editor = EditorWidget()
app.exec_()