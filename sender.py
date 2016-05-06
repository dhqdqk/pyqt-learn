#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
示范sender获取信号发送者
'''

import sys
from PyQt4 import QtGui, QtCore


class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
    
    def initUI(self):
        button1 = QtGui.QPushButton('button 1', self)
        button1.move(30, 50)
        
        button2 = QtGui.QPushButton('button 2', self)
        button2.move(150, 50)
        
        # 当发出clicked信号时调用buttonClicked
        self.connect(button1, QtCore.SIGNAL('clicked()'), 
                     self.buttonClicked)
        self.connect(button2, QtCore.SIGNAL('clicked()'),
                     self.buttonClicked)
                         
        self.statusBar().showMessage('Ready')
        # 注意只有QMainWindow才有statusBar元素
        
        self.setWindowTitle('Event sender')
        self.resize(290, 150)
    
    def buttonClicked(self):
        sender = self.sender() # 获取sender对象
        self.statusBar().showMessage(sender.text() + 'was pressed')


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())