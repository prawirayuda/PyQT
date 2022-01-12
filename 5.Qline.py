import sys 
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QLineEdit,QPushButton)
from PyQt5.QtCore import Qt 

class EntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialUI()
        
    def initialUI(self):
        self.setGeometry(100,100,400,200)
        self.setWindowTitle("Qline Edit")
        self.displayWidget()
        
        self.show()
    
    def displayWidget(self):
        QLabel("Masukan nama ", self).move(70,10)
        name_label = QLabel("Name:",self)
        name_label.move(70,50)

        
        self.name_entry = QLineEdit(self)
        self.name_entry.setAlignment(Qt.AlignCenter)
        self.name_entry.move(110,50)
        self.name_entry.resize(200,20)
        
        self.clear_button = QPushButton('clear',self)
        self.clear_button.clicked.connect(self.clearEntries)
        self.clear_button.move(160,110)
    

    def clearEntries(self):
        sender = self.sender()
        if sender.text() =='clear':
            self.name_entry.clear()
            
if __name__ =='__main__':
    app = QApplication(sys.argv)
    window = EntryWindow()
    sys.exit(app.exec_())        