#!/usr/bin/env python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class QuitButton(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setGeometry(400, 400, 250, 150)
        self.setWindowTitle('Quit Button')
        
        toquit = QtGui.QPushButton('closed', self)
        toquit.setGeometry(10, 10, 64, 35)
        self.connect(toquit, QtCore.SIGNAL('clicked()'),
                     QtGui.qApp, QtCore.SLOT('quit()'))


app = QtGui.QApplication(sys.argv)
qb = QuitButton()
qb.show()
sys.exit(app.exec_())