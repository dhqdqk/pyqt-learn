#!/usr/bin/env python
#coding:utf-8

import sys
from PyQt4 import QtGui

class Center(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('center')
        self.resize(640, 480) # 主窗口尺寸
        self.center()
    
    def center(self):
        screen = QtGui.QDesktopWidget().screenGeometry()
        # 计算屏幕分辨率率
        size = self.geometry()
        # 窗口居中
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)


app = QtGui.QApplication(sys.argv)
qb = Center()
qb.show()
sys.exit(app.exec_())