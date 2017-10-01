#Widgets.py

#!/usr/bin/python3
#-*- coding:utf-8

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QMessageBox, QMainWindow
from PyQt5.QtCore import Qt

class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        button = QPushButton('Push Me', self) #버튼 생성
        button.move(10, 10)
        button.clicked.connect(self.message) # clicked이벤트시 처리할 메소드 연결
                                             #qt에서는 이벤트를 시그널이라 한다
        button.clicked.connect(message2) #이벤트 핸들러로는 함수, 메소드 다 사용 가능

        self.show()

    def message(self):
        """
        메세지
        """
        msg = QMessageBox(self)
        msg.setText("You Pushed Me")
        msg.show()

def message2():
    print("push me")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()

    sys.exit(app.exec())
    
