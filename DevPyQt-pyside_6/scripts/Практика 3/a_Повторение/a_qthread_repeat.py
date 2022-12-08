"""
Файл для повторения темы QTimer

Напомнить про работу с QTimer.

Предлагается создать приложение-которое будет
с некоторой периодичностью вызывать определённую функцию.
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gen = None
        self.initUi()
        self.initTimer(1000)






def unitUi(self):
    self.b1 = QtWidgets.QPushButton("push")
    self.b2 = QtWidgets.QPushButton("clean")
    self.text = QtWidgets.QLineEdit()
    self.text_1 = QtWidgets.QPlainTextEdit()
    hor_layout = QtWidgets.QHBoxLayout
    hor_layout.addWidget(self.text)
    hor_layout.addWidget(self.b1)
    hor_layout.addWidget(self.b2)
    main_layout = QtWidgets.QVBoxLayout()
    main_layout.addLayout(hor_layout)
    main_layout.addWidget(self.text_1)

    self.setLayout(main_layout)


def initTimers(self, param):
    self.timer = QtCore.QTimer()
    self.timer.setInterval(param)
    self.timer.start()


def initSignals(self):
    self.b2.clicked.connect(self.text_p.clear)
    self.b1.clicked.connect(self.startGen)
    self.timer.timeout.connect(self.setTextEdit)


def startGen(self):
    self.gen = (val for i in self.text.text())


def setTextEdit(self):
    try:
        self.text_1.appendPlainText(next(self.gen))
    except(StopIteration):
        pass

