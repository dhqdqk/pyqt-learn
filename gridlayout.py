#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
此节运用grid布局按钮

'''
import sys
from PyQt4 import QtGui

class Example(QtGui.QWidget):
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('grid layout')
        
        # 十进制计算器
        names = ['cls', 'bck', '', 'close', '7', '8', '9', '/',
                 '4', '5', '6', '*', '1', '2', '3', '-',
                 '0', '.', '=', '+']
        
        # 创建grid对象
        grid = QtGui.QGridLayout()
        grid.setSpacing(10) # 行距
        
        j = 0
        pos = [(0, 0), (0, 1), (0, 2), (0, 3),
                (1, 0), (1, 1), (1, 2), (1, 3),
                (2, 0), (2, 1), (2, 2), (2, 3),
                (3, 0), (3, 1), (3, 2), (3, 3 ),
                (4, 0), (4, 1), (4, 2), (4, 3)]
        
        for i in names:
            button = QtGui.QPushButton(i)
            if j == 2:
                grid.addWidget(QtGui.QLabel(''), 0, 2)
            else:
                grid.addWidget(button, pos[j][0], pos[j][1])
                # grid会自动处理间隔
            j = j + 1
        
        # 文本框
        title = QtGui.QLabel('Title')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')
        
        titleEdit = QtGui.QLineEdit() # 单行文本框
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit() # 多行文本框
        
        # addWidget(obj, pos_x, pos_y, row_number, col_number)
        grid.addWidget(title, 5, 0)
        grid.addWidget(titleEdit, 5, 1, 1, 4)
        
        grid.addWidget(author, 6, 0)
        grid.addWidget(authorEdit, 6, 1, 1, 4)
        
        grid.addWidget(review, 7, 0)
        grid.addWidget(reviewEdit, 7, 1, 6, 4)
        
        
        
        self.setLayout(grid)
        self.resize(640, 480)


app = QtGui.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())
