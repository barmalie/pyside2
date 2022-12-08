import sys

from PySide6 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.gen = None
        self.initUi()
        self.initTimer()

se
    def unitUi(self):
        self.b1 = QtWidgets.QPushButton("push")
        self.b2 = QtWidgets.QPushButton("clean")
        self.text = QtWidgets.QLineEdit()
        self.text_1 = QtWidgets.QPlainTextEdit()
        hor_layout = QtWidgets.QHBoxLayout
        hor_layout.addWidget(self.text)
        hor_layout.addWidget(self.b1)
        hor_layout.addWidget(self.b2)
        main_layout =QtWidgets.QVBoxLayout()
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
        self.gen = (val for in self.text.text())
    def setTextEdit(self):
        try:
            self.text_1.appendPlainText(next(self.gen))
        except(StopIteration):
            pass


        self.setFixedSize(300, 100)

        self.label = QtWidgets.QLabel("<H1>Нажми</H1> на меня")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.installEventFilter(self)  # Установка фильтра событий на конкретный виджет

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        self.setLayout(layout)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        """
        Настройка дополнительного поведения виджетов

        :param watched: QtCore.QObject
        :param event: QtCore.QEvent
        :return: bool
        """

        if watched == self.label and event.type() == QtCore.QEvent.Type.MouseButtonPress:
            print("mouse pressed")

        if watched == self.label and event.type() == QtCore.QEvent.Type.Wheel:
            print("wheel changed")
            print(event.angleDelta())

        return super(Window, self).eventFilter(watched, event)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = Window()
    window.show()

    app.exec()
