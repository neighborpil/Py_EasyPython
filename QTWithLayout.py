#QTWithLayout.py
#레이아웃을 사용한 QT
#QHBoxLayout, QVBoxLayout

#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QLabel, QApplication, QWidget,
                             QPushButton, QHBoxLayout, QVBoxLayout)
                             
class LayoutExample2(QMainWindow):
    def __init__(self):
        super().__init__()

        #사용할 위젯 생성
        lbl1 = QLabel("This is")
        lbl2 = QLabel("Layout Example")

        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")

        hbox = QHBoxLayout() #가로 박스
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout() #세로 박스
        vbox.addWidget(lbl1) #박스1
        vbox.addWidget(lbl2) #박스2
        vbox.addLayout(hbox) #박스3 : 여기에 가로박스를 담는다

        window = QWidget()
        window.setLayout(vbox)
        self.setCentralWidget(window)

        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Layout Example')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LayoutExample2()
    sys.exit(app.exec())

                      
                      
