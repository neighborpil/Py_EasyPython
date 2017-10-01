#메인 윈도우 표시하기
#QApplication : GUI 프로그램 전체를 관리, 한어플에는 하나의 QApplication이 있다
#HelloWindow는 QMainWindow를 상속받아서 메인윈도의 속성을 변경

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication

class HelloWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #UI 초기화
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("HelloWindow")
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = HelloWindow()
    sys.exit(app.exec())
