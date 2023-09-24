from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app = QApplication([])
win = QWidget()
win.setWindowTitle("Визначник переможця")
win.resize(400, 200)
win.move(100, 100)

text = QLabel(win)
text.setText("Натисніть, щоб дізнатися переможця")
text.move(70, 10)

text1 = QLabel(win)
text1.setText("?")
text1.move(190, 70)

text2 = QLabel(win)
text2.setText("?")
text2.move(190, 100)

button = QPushButton(win)
button.setText("Нажмі")
button.move(140, 130)

def show_win():
    number = randint(1, 100)
    text2.setText(str(number))
    text.setText("Ура победа:")

    number1 = randint(1, 100)
    text1.setText(str(number1))
    text.setText("Ура победа:")
    text.setText("Ура победа:")
button.clicked.connect(show_win)

win.show()
app.exec_()
