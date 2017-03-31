# -*- coding: utf-8 -*-
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

def main(args):	
	app = QApplication(args)
	win = MenuBar(None)	
	app.exec_()

class MenuBar(QWidget):
	

	def __init__(self, parent): #, QWidget = None, Qt.WindowFlags flags = 0):
		super().__init__()

		self.parent = parent

		self.edtImage = QPixmap('edt.jpg')
		self.mesNotesImage = QPixmap('mesnotes.png')
		self.mesCoursImage = QPixmap('mescours.png')
		self.mesEvaluationsImage = QPixmap('eval.svg')
		self.monForumImage = QPixmap('forum.png')

		self.resize(600,600)
		self.setWindowTitle("AIR NOTES")

		self.VBoxLayout = QVBoxLayout(self)
		self.myWidget = QWidget(self)
		self.myWidget.setMinimumSize(200, 50)
		self.label = QLabel(" ",self.myWidget)
		self.label.resize(300,300)
		self.myWidget.show()
		self.VBoxLayout.addWidget(self.myWidget)

		self.HBoxLayout = QHBoxLayout()
		self.VBoxLayout.addLayout(self.HBoxLayout)

		self.createMenu()

	
		
	def createMenu(self):
		icon = QPixmap('mesnotes.png')
		icon = icon.scaledToWidth(200)
		#print(icon.size())
		

		mesNotes = QPushButton(QIcon('mesnotes.png'), "Mes Notes")
		mesNotes.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(mesNotes)
		mesNotes.clicked.connect(lambda: self.parent.seen("mesNotes"))	
		
		edt = QPushButton(QIcon('edt.png'), "EDT")
		edt.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(edt)
		edt.clicked.connect(lambda: self.parent.seen("edt"))

		mesCours = QPushButton(QIcon('mescours.png'), "Mes Cours", self.myWidget)
		mesCours.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(mesCours)
		mesCours.clicked.connect(lambda: self.parent.seen("mesCours"))

		mesEvaluations = QPushButton(QIcon('eval.svg'), "Evaluations", self.myWidget)
		mesEvaluations.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(mesEvaluations)
		mesEvaluations.clicked.connect(lambda: self.parent.seen("mesEvaluations"))

		monForum = QPushButton(QIcon('forum.png'), "Forum", self.myWidget)
		monForum.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(monForum)
		monForum.clicked.connect(lambda: self.parent.seen("monForum"))

		mesNotes.setToolTip("Acceder a Mes notes")
		edt.setToolTip("Emploi Du Temps")
		mesCours.setToolTip("Acceder a Mes cours")
		mesEvaluations.setToolTip("Acceder aux Evaluations")
		monForum.setToolTip("Acceder au Forum")

		self.show()





if __name__ == '__main__':
	main(sys.argv)



