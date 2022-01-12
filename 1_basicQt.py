import sys
from PyQt5.QtWidgets import  QApplication, QWidget

class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__() # create default constructor for qwidget
        self.initializeUI()
    
    def initializeUI(self):
        self.setGeometry(100,100,100,100)
        self.setWindowTitle('Empty Window in pyQt')
        self.show()
            
    #run the program 
if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = EmptyWindow()
        sys.exit(app.exec_())
        
        