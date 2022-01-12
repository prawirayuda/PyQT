import sys
from PyQt5.QtWidgets import QApplication, QWidget


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialUi()
        
    def initialUi(self):
        self.setGeometry(100,100,400,100)
        self.setWindowTitle("testing")
        self.show()

if __name__ == '__main__':
     app = QApplication(sys.argv)
     window = EmptyWindow()
     sys.exit(app.exec_())      
     
