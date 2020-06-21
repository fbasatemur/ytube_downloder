# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:33:59 2020

@author: fbasatemur
"""


from PyQt5.QtWidgets import QMainWindow, QLineEdit, QLabel, QComboBox, QRadioButton, QPushButton, QProgressBar
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt

from YTube_downloader import Downloader

class Window(QMainWindow):
      
      def __init__(self):
            super().__init__()
            
            # main window
            self.width = 640
            self.height = 480
            
            self.setWindowTitle("YTube Downloader")
            self.setGeometry(200, 200, self.width, self.height)
            self.setWindowIcon(QIcon("YTube_image.jpg"))           
                         
            self.entry()                  
            self.labelURL()
            self.radioButton()      
            self.infoButton()
            self.downloadButton()
            self.imageShow()
            self.labelInfo()
            self.labelInfoResult()
            self.comboBoxShow()
            self.downloadBar()
            
            self.show()
      
            
      def entry(self):
            self.textbox = QLineEdit(self)
            self.textbox.move(50, 65)
            self.textbox.resize(300,25)
      
      def labelURL(self):
            self.labelURLText = QLabel("URL Address: ", self)
            self.labelURLText.move(50,35)
            self.labelURLText.setFont(QFont("Arial", 9, QFont.Bold))
                        
            
      def labelInfo(self):
            self.labelTitle = QLabel("Title: ", self)
            self.labelTitle.move(50,270)
            self.labelTitle.setFont(QFont("Arial", 9, QFont.Bold))
            
            self.labelAuthor = QLabel("Author: ", self)
            self.labelAuthor.move(50,290)
            self.labelAuthor.setFont(QFont("Arial", 9, QFont.Bold))
            
      
      def labelInfoResult(self):
            self.labelTitleResult = QLabel(" __ ", self)
            self.labelTitleResult.move(110,270)
            self.labelTitleResult.resize(500,30)
            
            self.labelAuthorResult = QLabel(" __ ", self)
            self.labelAuthorResult.move(110,290)
            self.labelAuthorResult.resize(500,30)
            

      def imageShow(self):
            self.image = QLabel(self)
            self.image.resize(240, 240)
            self.image.move(370, 20)
            
      def comboBoxShow(self):
            self.combo = QComboBox(self)
            self.combo.move(140,120)
      
      def radioButton(self):
            self.radioBtnVideo = QRadioButton("Video", self)
            self.radioBtnAudio = QRadioButton("Audio", self)
      
            self.radioBtnVideo.move(50,120)
            self.radioBtnAudio.move(50,145)
            
            self.radioBtnVideo.setChecked(True)
      
      def infoButton(self):
            self.infoBtn = QPushButton("info", self)
            self.infoBtn.move(250,120)
            
            self.infoBtn.clicked.connect(self.infoBtnFunc)

      def downloadButton(self):
            self.downloadBtn = QPushButton("Download", self)
            self.downloadBtn.move(250,160)
            
            self.downloadBtn.clicked.connect(self.downloadBtnFunction)
            
            
      def infoBtnFunc(self):
            self.pbar.setValue(0)
            self.down = Downloader(self.textbox.text())
            self.down.dataInfo()
            
            if(self.radioBtnVideo.isChecked()):
                  self.down.downloadInfoVideo()
            else:
                  self.down.downloadInfoAudio()
                    
            self.down.downloadThumbImage()
            self.setPixmap()
            self.infoShow()
            self.comboBoxAddItems()
            
      def infoShow(self):
            self.labelTitleResult.setText(self.down.title)
            self.labelAuthorResult.setText(self.down.author)
            
          
      def setPixmap(self):   
            pixmap = QPixmap('thumbnail.jpg')
            smaller_pixmap = pixmap.scaled(240, 240, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.image.setPixmap(smaller_pixmap)

      def comboBoxAddItems(self):
            self.combo.clear()
            self.combo.addItems(self.down.resList)

      def downloadBtnFunction(self):
            resIndex = self.down.resList.index(self.combo.currentText())
            self.down.download(self.down.itagList[resIndex])
            self.pbar.setValue(100)
            
      def downloadBar(self):
            self.pbar = QProgressBar(self)
            self.pbar.setGeometry(50, 340, 300, 28)
            self.pbar.setValue(0)
            

      
        
        
        
            
            
            
      
      
      
      

