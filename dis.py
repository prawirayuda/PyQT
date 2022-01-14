from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


# class MyWind(QMainWindow):
#     def __init__(self):
#         super(MyWind,self).__init__()
#         self.setGeometry(200,200,300,300)
#         self.setWindowTitle("Kmon")
#         self.initUI()

        
#     def initUI(self):
#         self.label = QtWidgets.QLabel(self)
#         self.label.setText("label bro")
#         self.label.move(50,50)
        
#         self.b1 = QtWidgets.QPushButton(self)
#         self.b1.setText("Cloek")
#         self.b1.clicked.connect(self.clicked)
        
#     def clicked(self):
#         self.label.setText("u press me")
        
        
# def Window():
#     app = QApplication(sys.argv)
#     win = MyWind()
#     win.show()
#     sys.exit(app.exec_())
    
# Window()


def tekan():
    print("clikced")

def window():
    app = QApplication(sys.argv)
    wind = QMainWindow()
    wind.setGeometry(200,200,200,200)
    wind.setWindowTitle("it")
    
    label = QtWidgets.QLabel(wind)
    label.setText("this label")
    label.move(50,50)
    b1 = QtWidgets.QPushButton(wind)
    b1.setText("clikc me")
    b1.clicked.connect(tekan)
    wind.show()
    sys.exit(app.exec_())
    
window()
    

