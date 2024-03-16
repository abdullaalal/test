from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app=QApplication([]) #объект приложение

win=QWidget()#окно
win.show()#чтобы оно показалось
win.setWindowTitle('hello')#название окна
win.resize(600,600)#Размер окна




button1= QPushButton("1")
button2= QPushButton("2")
button2= QPushButton("3")
button2= QPushButton("4")
button2= QPushButton("5")



line= QHBoxLayout()
lineV1= QVBoxLayout()
lineH1= QHBoxLayout()
lineH2= QHBoxLayout()
lineH3= QHBoxLayout()
text = QLabel

button.clicked.connect(text)
win.setLayout(line)
lineH1.addWidget(button1, alignment = Qt.AlignLeft)
lineH1.addWidget(button2, alignment = Qt.AlignRight)
lineH2.addWidget(button3, alignment = Qt.AlignCenter)
lineH3.addWidget(button4, alignment = Qt.AlignLeft)
lineH4.addWidget(button5, alignment = Qt.AlignRight)


app.exec_() #чтобы не закрывалось без нажатия крестика