#menubar_toolbar_statusbar.py

#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication,
                             QFileDialog)
from PyQt5.QtGui import QIcon

class Example(QMainWindow):
    def __init__(self):
        """생성자"""
        super().__init__()

        self.click_count = 0

        #Menu
        self.init_menu()
        self.init_toolbar()

        self.print_on_statusbar('.')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Example')
        self.show()

    def init_menu(self):
        """메뉴바"""
        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.onShowDialog)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

    def init_toolbar(self):
        #툴바 아이템 생성
        exitAction = QAction(QIcon('close.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.triggered.connect(qApp.quit)

        printAction = QAction('Click', self)
        printAction.triggered.connect(self.onClickButton)

        #툴바Q
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(printAction)

    def print_on_statusbar(self, text):
        self.statusBar().showMessage(text)

    def onClickButton(self):
        self.click_count += 1
        self.statusBar().showMessage("Clicked : {}".format(self.click_count))

    def onShowDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', '/home')
        if fname[0]:
            f = open(fname[0], 'r')
            self.print_on_statusbar('Tryingfile : {}'.format(fname[0]))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
