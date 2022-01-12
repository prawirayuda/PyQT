import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QCheckBox,QLabel)
from PyQt5.QtCore import Qt

class Checkbox(QWidget):
    def __init__(self):
        super().__init__()
        self.UI()
    
    def UI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('Qcheckbox')
        self.displayCheckbox()
        self.show()
        
    def displayCheckbox(self):
        header_label = QLabel(self)
        header_label.setText("Blabla bla bala??")
        header_label.setWordWrap(True)
        header_label.move(10,10)
        header_label.resize(230,60)
        
        opsi1 = QCheckBox("1",self)
        opsi1.move(20,80)
        opsi1.stateChanged.connect(self.printToTerminal)
        opsi1.toggle()
        
        opsi2 = QCheckBox("2",self)
        opsi2.move(20,100)
        opsi2.stateChanged.connect(self.printToTerminal)
        
        opsi3 = QCheckBox("3",self)
        opsi3.move(20,120)
        opsi3.stateChanged.connect(self.printToTerminal)
        
        
    def printToTerminal(self,state):
        sender = self.sender()
        if state == Qt.Checked:
            print(f"{sender.text} Selected")
        else:
            print(f"{sender.text} diselected")
            
            
if __name__== '__main__':
    app = QApplication(sys.argv)
    window = Checkbox()
    sys.exit(app.exec_())    