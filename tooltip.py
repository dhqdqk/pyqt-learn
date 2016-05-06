#!/usr/bin/env python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore

class Tooltip(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltip')
        
        self.setToolTip('This is a <b>QWidget</b> widget')
        # QtGui.QToolTip.setFont(QtGui.QFont('OldEnglish', 10))
        # 当鼠标移到窗口时会弹出提示
    

app = QtGui.QApplication(sys.argv)
tooltip = Tooltip()
tooltip.show()
sys.exit(app.exec_())

