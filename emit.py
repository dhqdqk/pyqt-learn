#!/usr/bin/env python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Emit(QtGui.QWidget):
    def __init__(self):
        super(Emit, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        self.connect(self, QtCore.SIGNAL('closeEmitApp'),
                     QtCore.SLOT('close()'))
        self.setWindowTitle('emti')
        self.resize(250, 150)
        
    def mousePressEvent(self, event):
        self.emit(QtCore.SIGNAL('closeEmitApp()'))

app = QtGui.QApplication(sys.argv)
ex = Emit()
ex.show()
sys.exit(app.exec_())