import re

from PyQt5 import QtWidgets
import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import mainMeun
from PyQt5.QtCore import Qt
from PyQt5 import QtCore


class Window(QMainWindow):
    pathname = None

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('视频转换文本(一次只能上传一个文件)')
        self.resize(500, 350)
        Window.setWindowOpacity(self, 0.9)
        # Window.setWindowFlag(self, QtCore.Qt.FramelessWindowHint)

        log = QMainWindow(self)
        log.setGeometry(0, 10, 400, 300)
        hbox = QHBoxLayout()
        self.paths = "请将视频拖到此处/输入视频的本地地址"
        ico_file = "nm.ico"
        self.setWindowIcon(QIcon(ico_file))
        fmlayout = QFormLayout()
        self.textBrowser = QTextEdit()
        self.textBrowser.move(140, 140)
        self.textBrowser.setText(self.paths)
        self.setCentralWidget(self.textBrowser)
        # self.pushB = QPushButton("关闭", self)
        self.textBrowser.setFixedWidth(450)
        self.textBrowser.setFixedHeight(90)
        # self.pushB.setGeometry(0, 0, 50, 30)
        # self.pushB.clicked.connect(self.when_pushB_click)
        # fmlayout.addRow(self.pushB)

        fmlayout.addRow(self.textBrowser)
        fmlayout.setHorizontalSpacing(20)
        fmlayout.setVerticalSpacing(10)
        hbox.setAlignment(Qt.AlignCenter)
        hbox.addLayout(fmlayout, 2)
        log.setLayout(hbox)

        self.setAcceptDrops(True)

        self.btn = QPushButton("点击翻译", self)
        self.btn2 = QPushButton("清空", self)

        self.textBrowser.setGeometry(30, 30, 100, 30)
        self.btn2.setGeometry(150, 300, 100, 30)
        self.btn.setGeometry(250, 300, 100, 30)

        self.btn.clicked.connect(self.when_btn_click)
        self.btn2.clicked.connect(self.when_btn2_click)

    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     painter.setBrush(Qt.black)
    #     painter.drawRect(self.rect())
    # def paintEvent(self, event):
    #     painter = QPainter(self)
    #     pi = QPixmap("./img/001.jpg")
    #     Window.resize(1080, 608)
    #     painter.drawRect(self.rect(), pi)

    # def when_pushB_click(self):
    #     sys.exit()

    def when_btn_click(self):
        con = self.pathname
        if ".mp4" not in con:
            self.textBrowser.setText("格式不对\n文件难以转换")
        else:
            txtpath = mainMeun.main(self.pathname)
            if txtpath:
                self.textBrowser.setText("文件转换完成\n翻译文件存在于:{}".format(txtpath))
            else:
                self.textBrowser.setText("The video cannot be read")

    def when_btn2_click(self):
        self.textBrowser.setText("")
        self.paths = ""

    def dragEnterEvent(self, event):

        file = event.mimeData().urls()[0].toLocalFile()
        if file not in self.paths:
            self.paths = file + "\n"
            self.textBrowser.setText(self.paths)
            self.pathname = file


class CommonStyleSheet:

    def __init__(self):
        pass

    @staticmethod
    def loadqss(style):
        with open(style, "r", encoding="utf-8") as f:
            return f.read()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
