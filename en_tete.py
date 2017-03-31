# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:25:11 2017

creat a main window with only heading
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QPainter, QColor, QBrush
import sys


class HeaderWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(1080, 720) #optional
        self.SIZE_Y = self.size().height()
        self.SIZE_X = self.size().width()
        self.intTopSide()
        self.show()

    def intTopSide(self):
        """
        top side of web page
        """
        # from dataBase:
        nb_cours = 10
        nb_notes = 12
            
        # init WebTopSide
        
        self.resize(self.SIZE_X, self.SIZE_Y/5)

        headingMenu = QHBoxLayout()
        self.setLayout(headingMenu)
        
        # profileIcon:
        profilButton = QPushButton(QIcon("profil1.png"), "")
        profilButton.setIconSize(QSize(self.SIZE_Y/6, self.SIZE_Y/6))
        headingMenu.addWidget(profilButton)

        headingMenu.addSpacing(self.SIZE_Y/20)
        
        # nbCours/nbNotes
        labelCours = QLabel("nb cours :" + str(nb_cours))
        labelNotes = QLabel("nb notes :" + str(nb_notes))
        miniStat = QVBoxLayout()
        miniStat.addWidget(labelCours)
        miniStat.addWidget(labelNotes)
        headingMenu.addLayout(miniStat)

        headingMenu.addSpacing(self.SIZE_Y/20)
        
        # AddANote
        addNoteButton = QPushButton(QIcon("plusIcon.png"), "Add a Note")
        addNoteButton.setIconSize(QSize(self.SIZE_Y/15, self.SIZE_Y/20))
        headingMenu.addWidget(addNoteButton)

        headingMenu.addStretch()
        
        # SearchBar
        """# set QAction: searchAction
        searchAction = QAction(QIcon("searchIcon.png"),"searchAction",self) 
        searchAction.triggered.connect(open_file = QFileDialog.getOpenFileName(self, "Open a file", "./"))"""
        searchBar = QLineEdit(None)
        searchBar.setPlaceholderText("Search Tool")
        searchBar.addAction(QIcon("searchIcon.png"), searchBar.ActionPosition(1))
        searchBar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        headingMenu.addWidget(searchBar)
        
        
        """
        labelCours = QLabel("nb cours :")
        labelNotes = QLabel("nb notes :")
        miniStat = QVBoxLayout()
        miniStat.addWidget(labelCours)
        miniStat.addWidget(labelNotes)
        self.headingMenu.addLayout(miniStat)
        """
        # addNote
        #
        # searchBar
        
        
def main(args):
    app = QApplication(args)
    window = HeaderWidget()
    
    app.exec_()

if __name__ == "__main__":
    main(sys.argv)
