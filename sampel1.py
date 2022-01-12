import sys

from PySide6.QtWidgets import QApplication, QGridLayout, QVBoxLayout
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtWidgets import QPushButton
from PySide6.QtWidgets import QWidget
# from PyQt5.QtWidgets import QApplication
# from PyQt5.QtWidgets import QHBoxLayout

# from PyQt5.QtWidgets import QPushButton
# from PyQt5.QtWidgets import QWidget


##### QH box show horizontal

# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('QHBoxLayout')
# layout = QHBoxLayout()
# layout.addWidget(QPushButton('Left'))
# layout.addWidget(QPushButton('Center'))
# layout.addWidget(QPushButton('Right'))
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())

##### Qv box show vertical

# app = QApplication(sys.argv)
# window = QWidget()
# window.setWindowTitle('QV_Box_layout')
# layout = QVBoxLayout()
# layout.addWidget(QPushButton('Top'))
# layout.addWidget(QPushButton('center'))
# layout.addWidget(QPushButton('bottom'))
# layout.addWidget(QPushButton('none'))
# window.setLayout(layout)
# window.show()
# sys.exit(app.exec_())

def handleClick():
    print("Clicked")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('QGridLayout')
layout = QGridLayout()
btnA = QPushButton('ButtonA')
btnA.setStyleSheet("background-color: red")
btnA.clicked.connect(handleClick)
layout.addWidget(btnA,0,0)
layout.addWidget(QPushButton('Button'),0,1)
layout.addWidget(QPushButton('Button'),0,2)
# layout.addWidget(QPushButton('Button'),1,0)
# layout.addWidget(QPushButton('Button'),1,1)
# layout.addWidget(QPushButton('why'),2,0,2,0)
# layout.addWidget(QPushButton('why'),3,0,2,0)



window.setLayout(layout)
window.show()
sys.exit(app.exec())