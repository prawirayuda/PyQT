import sys 
from PyQt5.QtWidgets import (QApplication,QWidget,QMessageBox,QPushButton,QLabel,QLineEdit)

from PyQt5.QtGui import QFont,QPixmap

class CreateNewUser(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100,100,400,400)
        self.setWindowTitle("create new user")
        self.displayWidgetsToCollectInfo()
        self.show()
        
        
    def displayWidgetsToCollectInfo(self):
        new_image_profile = "D:\\testEnv\\src\\img\\img.png"
        
        try:
            with open(new_image_profile):
                new_user = QLabel(self)
                pixmap = QPixmap(new_image_profile)
                new_user.setPixmap(pixmap)
                new_user.move(150,60)
        except FileNotFoundError:
            print("Img nothing")
        
        login_label = QLabel(self)
        login_label.setText("create new")
        login_label.move(110,20)
        login_label.setFont(QFont('roboto',20))
        
        
        name_label = QLabel("username:",self)
        name_label.move(50,180)
        
        self.name_input = QLineEdit(self)
        self.name_input.move(130,180)
        self.name_input.resize(200,20)
        
        name_label = QLabel("full name:",self)
        name_label.move(50,210)
        
        name_input = QLineEdit(self)
        name_input.move(130,210)
        name_input.resize(200,20)
        
        
        pswd_label = QLabel("password:", self)
        pswd_label.move(50, 240)
        self.pswd_entry = QLineEdit(self)
        self.pswd_entry.setEchoMode(QLineEdit.Password)
        self.pswd_entry.move(130, 240)
        self.pswd_entry.resize(200, 20)
        confirm_label = QLabel("confirm:", self)
        confirm_label.move(50, 270)
        self.confirm_entry = QLineEdit(self)
        self.confirm_entry.setEchoMode(QLineEdit.Password)
        self.confirm_entry.move(130, 270)
        self.confirm_entry.resize(200, 20)
        
        sign_up_button = QPushButton("sign up", self)
        sign_up_button.move(100, 310)
        sign_up_button.resize(200, 40)
        sign_up_button.clicked.connect(self.confirmSignUp) 
        
        
    def confirmSignUp(self):
        pswd_text = self.pswd_entry.text()
        confirm_text = self.confirm_entry.text()
        
        if pswd_text != confirm_text:
            QMessageBox.warning(self,"Error Message","the pass doesnt match",QMessageBox.Close)
        else:
            with open("D:\\testEnv\\src\\files\\users.txt", 'a+') as f:
                f.write(self.name_input.text()+ " ")
                f.write(pswd_text + "\n")
            self.close()
            
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateNewUser()
    sys.exit(app.exec_())