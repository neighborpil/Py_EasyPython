#Signal & Slot
# - 이벤트와 이벤트 핸들러이다

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyWindow(QMainWindow):
    #시그널 하나를 만든다 데이터는 없다
    closeApp = pyqtSignal()

    def __init__(self):
        super().__init__()
        #이벤트에 핸들러 등록
        #앱을 종료
        self.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    #마우스를 누르면 closeApp 이벤트 발생
    def mousePressEvent(self, event):
        self.closeApp.emit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWindow()
    sys.exit(app.exec())
