#slider.py

#!/usr/bin/python3
#-*- coding:utf-8 -*-

import sys
from PyQt5.QtWidgets import(QWidget, QSlider, QLabel, QApplication, QMainWindow)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #가로 슬라이더 생성
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMaximum(1000)
        self.slider.setMinimum(0)

        #위치와 크기
        self.slider.setGeometry(30, 40, 100, 30)

        #시그널 연결
        self.slider.valueChanged[int].connect(self.changeValue)

        #레이블 생성
        self.label = QLabel("Current : 0", self)
        self.label.setGeometry(30, 70, 100, 30)

        #윈도우 위치
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider Example')
        self.show()

    def changeValue(self, value):
        "슬라이더 값 출력"
        self.label.setText("Current : {}".format(value))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())

        
