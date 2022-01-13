from cmath import log
from decimal import setcontext
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QMessageBox,QLineEdit,QPushButton,QCheckBox)

from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from Registration import CreateNewUser


class LoginUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(100,100,400,300)
        self.setWindowTitle("UI Login")
        self.loginUserInterface()
        self.show()
        
    def loginUserInterface(self):
        login_label = QLabel(self)
        login_label.setText("Login")
        login_label.move(180,10)
        login_label.setFont(QFont('roboto',20))
        
        name_label = QLabel("username:",self)
        name_label.move(30,60)
        
        self.name_input = QLineEdit(self)
        self.name_input.move(110,60)
        self.name_input.resize(220,20)
        
        
        password_label = QLabel("Password:",self)
        password_label.move(30,90)
        self.password = QLineEdit(self)
        self.password.move(110,90)
        self.password.resize(220,20)
        
        
        sign_button = QPushButton("login",self)
        sign_button.move(100,140)
        sign_button.resize(200,40)
        sign_button.clicked.connect(self.clickLogin) #buat fungsi ini dude
        
        show_Pass = QCheckBox("show password",self)
        show_Pass.move(110,115)
        show_Pass.stateChanged.connect(self.showPassword) #buat fungsi ini dude
        show_Pass.toggle()
        show_Pass.setChecked(False)
        
        not_Member = QLabel("Not a member",self)
        not_Member.move(70,200)
        
        sign_Up = QPushButton("sign up", self)
        sign_Up.move(160,195)
        sign_Up.clicked.connect(self.createNewUser) #buat fungsi ini dude
        
    def clickLogin(self):
        users = {}
        try:
            with open("D:\\testEnv\\src\\files\\users.txt", "r") as f:
                for line in f:
                    user_fields = line.split(" ")
                    username = user_fields[0]
                    password = user_fields[1].strip("\n")
                    users[username] = password
        except FileNotFoundError:
            print("no file create new.")
            f = open ("files/users.txt", "w")
            
            
        username = self.name_input.text()
        password = self.password.text()
        
        if (username,password)in users.items(): 
            QMessageBox.information(self, "Login success", "Login success", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            self.close()
            
        else:
            QMessageBox.warning(self, "error message", "user / pass wrong", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            
    
    def showPassword(self,state):
        if state == Qt.Checked:
            self.password.setEchoMode(QLineEdit.Normal)
        else:
            self.password.setEchoMode(QLineEdit.Password)
            
    def createNewUser(self):
        self.create_new_user_dialog = CreateNewUser()
        self.create_new_user_dialog.show()
        
    def closeEvent(self,event):
        Quit = QMessageBox.question(self,"Quit ??","keluar??",QMessageBox.No | QMessageBox.Yes,QMessageBox.Yes)
        if Quit == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginUI()
    sys.exit(app.exec_())
            
                        
        