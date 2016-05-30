#!/usr/bin/env python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        hbox = QtGui.QHBoxLayout()
        
        button = QtGui.QPushButton('Dialgo', self)
        button.setFocusPOlicy(QtCore.Qt.NoFocus)
        button.move(20, 20)
        
        hbox.addWidget(button)
        
        self.connect(button, )
    
    def showDialog(self):
        pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    sys.exit(app.exec_())