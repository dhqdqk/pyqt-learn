#!/usr/bin/env python
#coding:utf-8

import sys
from PyQt4 import QtGui, QtCore


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        self.resize(640, 480)
        self.setWindowTitle('mennubar')
        self.center() # 居中
        
        # 添加退出
        self.exit = QtGui.QAction(QtGui.QIcon('icons/web.png'), 'Exit', self)
        self.exit.setShortcut('Ctrl+Q')
        self.exit.setStatusTip('Exit application')
        self.connect(self.exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('close()'))
        
        self.statusBar()
        
        # 添加文件栏
        self.menubar = self.menuBar()
        self.file = self.menubar.addMenu('&File')
        self.file.addAction(self.exit)
        
        # 添加工具栏
        self.toolBar = self.addToolBar('Exit')
        self.toolBar.addAction(self.exit)
        
        # 文本控件
        self.textEdit = QtGui.QTextEdit()
        self.setCentralWidget(self.textEdit)
        
    def center(self):
        'widget is in center'
        screen = QtGui.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
