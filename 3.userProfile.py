import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QFont, QPixmap,QColor


class UserProfile(QWidget):
    def __init__(self):
        super().__init__()
        self.initialUI()
    
    def initialUI(self):
        self.setGeometry(1200,100,250,250)
        self.setWindowTitle('Hell')
        self.displayImage()
        self.displayUserInfo()
        self.show()
        
            
    def displayImage(self):
        background_image = "image.png"
        profile_image = "images.png"
        try:
            with open(background_image):
                background = QLabel(self)
                pixmap = QPixmap(background_image)
                background.setPixmap(pixmap)
        except FileNotFoundError:
            print("image not found")
            
        try: 
            with open(profile_image):
                user_image = QLabel(self)
                pixmap = QPixmap(profile_image)
                user_image.setPixmap(pixmap)
                user_image.move(80,20)
        except FileNotFoundError:
            print("no file")
            
    
    def displayUserInfo(self):
        user_name = QLabel(self)
        user_name.setText("Yud")
        user_name.move(85,140)
        user_name.setFont(QFont('Roboto',17))
        about = QLabel(self)
        about.setText("about anythningsa dsadkshdksjd.")
        about.setWordWrap(True)
        about.move(85,190)
        # about.QColor(200,0,0)
        
        
        skill_title = QLabel(self)
        
        skill_title.setText("Skills")
        skill_title.move(85,240)
        skill_title.setFont(QFont('Roboto',17))
        
        skill = QLabel(self)
        skill.setText("Python |sql")
        skill.move(85,280) 


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = UserProfile()
    sys.exit(app.exec_())                

