# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 18:29:15 2022

@author: POUYA-AMIRI
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QMainWindow,QMessageBox,QLineEdit


class F(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()
        
    def setUI(self):
        self.setGeometry(60,260,900,500)
        self.setWindowTitle("New York City")
        
        btn = QPushButton("copy",self)
        btn.move(200,130)
        btn.clicked.connect(self.close1)
        
        
        btn = QPushButton("say hello",self)
        btn.move(500,50)
        btn.clicked.connect(self.click)
        
        
        
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(100,50)
        self.textbox1.resize(300,30)
        
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(100,90)
        self.textbox2.resize(300,30)
        
        
        self.statusBar().showMessage("this is my first program. made by pouya")
        self.show()
        
    
        
    def close1(self):
        t1 = self.textbox1.text()
        self.textbox2.setText(t1)
      
    def click(self):
        print("hello new york city")
        
if __name__ == "__main__":
    print(__name__)
    app=QApplication(sys.argv)
    ex = F()
    
    sys.exit(app.exec_())
        