import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap,QColor


class ButtonBro(QWidget):
    def __init__(self):
        super().__init__()
        self.initialUI()
    
    def initialUI(self):
        self.setGeometry(1200,100,250,250)
        self.setWindowTitle('Hell')
        self.displayButton()
        # self.displayUserInfo()
        self.show()

    def displayButton(self):
        name_label = QLabel(self)
        name_label.setText("dont Push me")
        name_label.move(60,30)
        
        button = QPushButton('Push Me',self)
        button.clicked.connect(self.buttonClicked)
        button.move(60,70)
        
    def buttonClicked(self):
        print("window has been closed.")
        self.close()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ButtonBro()
    sys.exit(app.exec_())       
        
        