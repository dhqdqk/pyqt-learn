#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        lcd = QtGui.QLCDNumber(self) # 液晶数字对象
        slider = QtGui.QSlider(QtCore.Qt.Horizontal, self) # 滑块，用于改变液晶数字
        
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)
        
        self.setLayout(vbox)
        self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd,
                     QtCore.SLOT('display(int)'))
        # connect(sender, signal, reciever, slot)
        # 连接滑块的 valueChanged() 信号到LCD数字的 display() 槽。
        
        self.setWindowTitle('Signal & slot')
        self.resize(450, 200)

app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
