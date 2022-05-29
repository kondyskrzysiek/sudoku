import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit
import sudoku


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'SUDOKU SOLVED'
        self.left = 100  # odległośc od lewej krawędzi ekranu w pixelach
        self.top = 100  # odległośc od górnej krawędzi ekranu w pixelach
        self.width = 500  # szerokośc okna
        self.height = 400  # wysokość okna
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tab = [[QLineEdit(self) for _ in range(9)] for _ in range(9)]
        for row_index, row_value in enumerate(self.tab):
            for i, v in enumerate(row_value):
                v.move(i * 40 + 10, row_index * 40 + 10)
                v.resize(30, 30)

        self.button = QPushButton('Solve', self)
        self.button.move(380, 40)

        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        result = [[0 for _ in range(9)] for _ in range(9)]
        for row_index, row_value in enumerate(self.tab):
            for i, v in enumerate(row_value):
                a = str(v.displayText())
                if a != '':
                    result[row_index][i] = int(a)

        sudoku.write_list(result)

        for row_index, row_value in enumerate(self.tab):
            for i, v in enumerate(row_value):
                v.setText(str(result[row_index][i]))


app = QApplication(sys.argv)
ex = App()
app.exec_()
