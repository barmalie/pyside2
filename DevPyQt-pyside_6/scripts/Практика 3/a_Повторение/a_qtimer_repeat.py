"""
Файл для повторения темы QThread

Напомнить про работу с QThread.

Предлагается создать небольшое приложение, которое будет с помощью модуля request
получать доступность того или иного сайта (возвращать из потока status_code сайта).

Поработать с сигналами, которые возникают при запуске/остановке потока,
передать данные в поток (в данном случае url),
получить данные из потока (статус код сайта),
попробовать управлять потоком (запуск, остановка).

Опционально поработать с валидацией url
"""

from PySide6 import QtWidgets


class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
"""
Использование потока через класс наследованный от QThread
"""

import time

from PySide6 import QtCore, QtWidgets
import requests

class Worker(QtCore.QThread):
    progress = QtCore.Signal(int)
    url = None

    def start(self, *args, url=None, **kwargs) -> None:
        self.url = url
        return super().start(*args, **kwargs)

    def run(self) -> None:


        data = requests.get(self.url)
        self.progress.emit(data.status_code)
        self.finished.emit()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.gen = None
        self.initUi()
        self.initTimer(1000)

    def initUi(self) -> None:

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

    def initTreads(self):
        self.thread = Worker()

    def initSignals(self) -> None:
        self.b1.clicked.connect(self.startProcess)
        self.b2.clicked.connect(self.text_p.clear)

        self.thread.progress.connect(self.reportProgress)
        self.thread.finished.connect(lambda : self.b1.setEnabled(True))

    @QtCore.Slot()
    def startProcess(self) -> None:
        self.b1.setEnabled(False)
        self.thread.start(url=self.text.text()) #считали данные и пердали в наш поток


        self.pushButton.setEnabled(False)
        self.thread.start()
    @QtCore.Slot()
    def reportProgress(self, progress) -> None:
       self.text_1.appendPlainText(str(progress))




if __name__ == '__main__':
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
