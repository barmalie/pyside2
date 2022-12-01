"""
Файл для повторения темы сигналов

Напомнить про работу с сигналами и изменением Ui.

Предлагается создать приложение, которое принимает в lineEditInput строку от пользователя,
и при нажатии на pushButtonMirror отображает в lineEditMirror введённую строку в обратном
порядке (задом наперед).
"""

from PySide6 import QtWidgets, QtCore

def revers(str_:str ) -> str:
    return str_[::-1]

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()



    def initUi(self):
        self.lineEditInput =QtWidgets.QLineEdit
        self.lineEditMirror = QtWidgets.QLineEdit
        self.pushbuttonMirror = QtWidgets.QPushButton("развернуть")
        layout_1 = QtWidgets.QHBoxLayout()
        layout_1.addWidget(lineEditInput)
        layout_1.addWidget(lineEditMirror)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.addLayout(layout_1)
        main_layout.addLayout(pushbuttonMirror)

        self.setLayout(main_layout)

        def initSignals(self) -> None:
            self.pushButtonMirrror.clicked.connect(lambda : reverse_(self.lineEditInput.text()))

        def set_lineEditMirror(self):
            self.lineEditMirror.setText(self.lineEditInput.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
