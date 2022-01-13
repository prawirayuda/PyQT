import sys 
from PyQt5.QtWidgets import (QApplication, QWidget,QLabel,QMessageBox,QLineEdit,QPushButton)
from PyQt5.QtGui import QFont

class DisplayMessageBox(QWidget):
    def __init__(self):
        super().__init__()    
        self.UI()
    
    def UI(self):
        self.setGeometry(100,100,400,200)
        self.setWindowTitle('Q messageBox')
        self.displayWid()
        self.show()
        
    def displayWid(self):
        katalog_label = QLabel("The Dark maker",self)
        katalog_label.move(20,20)
        katalog_label.setFont(QFont('roboto',20))
        
        auth_label = QLabel("Enter what u search: ",self)
        auth_label.move(40,60)
        
        auth_name = QLabel("Name:",self)
        auth_name.move(50,90)
        
        self.authInput = QLineEdit(self)
        self.authInput.move(95,90)
        self.authInput.resize(240,20)
        self.authInput.setPlaceholderText("Firstname last name")
        
        button = QPushButton("search",self)
        button.move(125,130)
        button.resize(150,40)
        button.clicked.connect(self.displayMessagebox)
        
    def displayMessagebox(self):
                try:
                    with open("files/author.txt", "r") as f:
                        authors = [line.rstrip('\n')for line in f]
                
                except FileNotFoundError:
                    print("file nothing")
                    
                    
                    not_found_msg = QMessageBox()
                    
                    
                    if self.authInput.text() in authors:
                        QMessageBox().information(self,"Author found", "author found in catalouge",QMessageBox.Ok,QMessageBox.Ok)
                    else:
                        not_found_msg = QMessageBox.question(self,"Author not found\n continue? ",QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
                        
                    if not_found_msg == QMessageBox.No:
                        print("Closing Application.")
                        self.close()
                    else:
                        pass
                
if __name__ ==' __main__':
    app = QApplication(sys.argv) 
    window = DisplayMessageBox()
    sys.exit(app.exec_())       
    