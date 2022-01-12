import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap


class Hell(QWidget):
    def __init__(self):
        super().__init__()
        self.initialUI()
    
    def initialUI(self):
        self.setGeometry(1200,100,250,250)
        self.setWindowTitle('Hell')
        self.displaylabels()
        self.show()
        
    def displaylabels(self):
        text = QLabel(self)
        text.setText("hell")
        text.move(105, 2)
        image = "image.png"
        try:
            with open(image):
                world_image = QLabel(self)
                pixmap = QPixmap(image)
                world_image.setPixmap(pixmap)
                world_image.move(25,40)
                print("find it")
        except FileNotFoundError:
            print("image not found")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Hell()
    sys.exit(app.exec_())                

