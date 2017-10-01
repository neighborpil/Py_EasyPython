#Dialog.py

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import(QWidget, QPushButton, QTextEdit, QFileDialog,
                            QApplication)

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.btn = QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.textEdit = QTextEdit(self)
        self.textEdit.setGeometry(20, 60, 450, 180)

        self.setGeometry(300, 300, 500, 300)
        self.setWindowTitle('Dialog')
        self.show()

    def showDialog(self):

        #다이얼로그의 반환값 형태 : ('<filename>')
        fname = QFileDialog.getOpenFileName(self, 'Open file', '.')

        if fname[0]:
            with open(fname[0], 'r') as f:
                data = f.read()
                self.textEdit.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
