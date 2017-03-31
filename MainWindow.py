# -*- coding: utf-8 -*-
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

def main(args):	
	app = QApplication(args)
	win = MainWindow()	
	app.exec_()

class MainWindow(QMainWindow):
	

	def __init__(self): #, QWidget = None, Qt.WindowFlags flags = 0):
		super(MainWindow,self).__init__()

		self.createMenu()

	
		
	def createMenu(self):

		self.edtImage = QPixmap('edt.jpg')
		self.mesNotesImage = QPixmap('mesnotes.png')
		self.mesCoursImage = QPixmap('mescours.png')
		self.mesEvaluationsImage = QPixmap('eval.svg')
		self.monForumImage = QPixmap('forum.png')

		self.resize(600,600)
		self.setWindowTitle("AIR NOTES")
		
		self.container = QLabel(" ",self)
		self.setCentralWidget(self.container)

		self.VBoxLayout = QVBoxLayout(self.container)
		self.myWidget = QWidget(self)
		self.myWidget.resize(600, 600)
		self.myWidget.show()
		self.VBoxLayout.addWidget(self.myWidget)

		self.HBoxLayout = QHBoxLayout()
		self.VBoxLayout.addLayout(self.HBoxLayout)
		icon = QPixmap('mesnotes.png')
		icon = icon.scaledToWidth(200)
		#print(icon.size())
		

		mesNotes = QPushButton(QIcon('mesnotes.png'), "Mes Notes")
		mesNotes.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(mesNotes)
		mesNotes.clicked.connect(self.mesNotesCliqued)	
		
		edt = QPushButton(QIcon('edt.png'), "EDT")
		edt.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(edt)
		edt.clicked.connect(self.edtCliqued)

		mesCours = QPushButton(QIcon('mescours.png'), "Mes Cours", self.myWidget)
		mesCours.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(mesCours)
		mesCours.clicked.connect(self.mesCoursCliqued)

		mesEvaluations = QPushButton(QIcon('eval.svg'), "Evaluations", self.myWidget)
		mesEvaluations.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(mesEvaluations)
		mesEvaluations.clicked.connect(self.mesEvaluationsCliqued)

		monForum = QPushButton(QIcon('forum.png'), "Forum", self.myWidget)
		monForum.setIconSize(QSize(60,60))
		self.HBoxLayout.addWidget(monForum)
		monForum.clicked.connect(self.monForumCliqued)

		mesNotes.setToolTip("Acceder a Mes notes")
		edt.setToolTip("Emploi Du Temps")
		mesCours.setToolTip("Acceder a Mes cours")
		mesEvaluations.setToolTip("Acceder aux Evaluations")
		monForum.setToolTip("Acceder au Forum")

		self.show()



	def edtCliqued(self):
		#print("button cliqued")
		self.container.setPixmap(self.edtImage)

	def mesNotesCliqued(self):
		self.container.setPixmap(self.mesNotesImage)

	def mesCoursCliqued(self):
		self.container.setPixmap(self.mesCoursImage)

	def monForumCliqued(self):
		self.container.setPixmap(self.monForumImage)

	def mesEvaluationsCliqued(self):
		self.container.setPixmap(self.mesEvaluationsImage)



if __name__ == '__main__':
	main(sys.argv)



