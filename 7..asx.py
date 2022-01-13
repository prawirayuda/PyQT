
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
 QMessageBox, QLineEdit, QPushButton)
from PyQt5.QtGui import QFont



authors = ""
class DisplayMessageBox(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI() # Call our function used to set up window
    def initializeUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('QMessageBox Example')
        self.displayWidgets()
        self.show()
    
    
    def displayWidgets(self):
        catalogue_label = QLabel("Author Catalogue", self)
        catalogue_label.move(20, 20)
        catalogue_label.setFont(QFont('Arial', 20))
        auth_label = QLabel("Enter the name of the author you are searching for:", self)
        auth_label.move(20, 60)
        # Create author label and line edit widgets
        author_name = QLabel("Name:", self)
        author_name.move(50, 90)
        self.auth_entry = QLineEdit(self)
        self.auth_entry.move(95, 90)
        self.auth_entry.resize(240, 20)
        self.auth_entry.setPlaceholderText("firstname lastname")
 # Create search button
        search_button = QPushButton("Search", self)
        search_button.move(125, 130)
        search_button.resize(150, 40)
        search_button.clicked.connect(self.displayMessageBox)
    
    
    def displayMessageBox(self):
        try:
            with open("D:\\testEnv\\src\\files\\authors.txt", "r") as f:
                # print("abc")
 # read each line into a list
                global authors
                authors = [line.rstrip() for line in f]
        except FileNotFoundError:
                print("The file cannot be found.")
 # Check for name in list
        not_found_msg = QMessageBox() 
        
        
        if self.auth_entry.text() in authors: QMessageBox().information(self, "Author Found", "Author found in catalogue!", QMessageBox.Ok, QMessageBox.Ok)
        else:
            not_found_msg = QMessageBox.question(self, "Author Not Found","Author not found in catalogue.\nDo you wish to continue?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if not_found_msg == QMessageBox.No:
                print("Closing application.")
                self.close()
        else:
            pass
    


if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = DisplayMessageBox()
        sys.exit(app.exec_())