# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from EditorWidget import EditorWidget
from a import MenuBar
from en_tete import HeaderWidget

def main(args):	
	app = QApplication(args)
	win = MainWindow()	
	app.exec_()

class MainWindow(QWidget):
	

	def __init__(self): #, QWidget = None, Qt.WindowFlags flags = 0):
		super().__init__()

		self.initUi()

	def initUi(self):

		self.menuBar = MenuBar(self)
		self.header = HeaderWidget()
		self.layout = QGridLayout()
		self.layout.addWidget(self.header, 0, 0)
		self.layout.addWidget(QWidget(), 1, 0)
		self.layout.addWidget(self.menuBar, 2, 0)

		self.setLayout(self.layout)

		self.show()

	def seen(self, option):
		if option == "mesNotes":
			self.layout.addWidget(EditorWidget(), 1, 0)



if __name__ == '__main__':
	main(sys.argv)



