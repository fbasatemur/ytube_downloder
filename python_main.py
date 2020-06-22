# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:21:17 2020

@author: fbasatemur
"""

if __name__ == '__main__':
      import sys
      from YTube_GUI import Window
      from PyQt5.QtWidgets import QApplication
      
      app = QApplication(sys.argv)
    
      windowObject = Window()
    
      sys.exit(app.exec_())