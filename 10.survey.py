import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
QCheckBox, QButtonGroup, QHBoxLayout, QVBoxLayout,QSizePolicy)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DisplaySurvey(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(100,100,400,230)
        self.setWindowTitle("survey GUI")
        self.displayWidget()
        self.show()
        
    def displayWidget(self):
        title = QLabel("Coffe pea")
        title.setFont(QFont('roboto',17))
        question =QLabel("how the day is ?")
        
        
        title_h_box = QHBoxLayout()
        # title_h_box.addStretch()
        title_h_box.addWidget(title)
        title.setStyleSheet("QLabel {border: 2px solid black; text-align: center}")
        title.setStyleSheet("QLabel")
        title.setAlignment(Qt.AlignCenter)

        title.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Ignored)
        # title_h_box.addStretch()
 
        
        ratings = ["bad","not good","so bad"]
        
        ratings_h_box = QHBoxLayout()
        ratings_h_box.setSpacing(60)
        
        ratings_h_box.addStretch()
        for rating in ratings:
            rate_label = QLabel(rating,self)
            ratings_h_box.addWidget(rate_label)
        ratings_h_box.addStretch()
            

        cb_h_box = QHBoxLayout()
        cb_h_box.setSpacing(100)
        scale_bg = QButtonGroup(self) 
        cb_h_box.addStretch()
        
        
        for cb in range(len(ratings)):
            scale_cb = QCheckBox(str(cb), self)
            cb_h_box.addWidget(scale_cb)
            scale_bg.addButton(scale_cb)
        cb_h_box.addStretch()
        scale_bg.buttonClicked.connect(self.checkboxClicked)
        
        close_button = QPushButton("Close",self)
        close_button.clicked.connect(self.close)
        
        v_box = QVBoxLayout()
        v_box.addLayout(title_h_box)
        v_box.addWidget(question)
        v_box.addStretch(1)
        v_box.addLayout(ratings_h_box)
        v_box.addLayout(cb_h_box)
        v_box.addStretch(2)
        v_box.addWidget(close_button)
        
        self.setLayout(v_box)
        
    def checkboxClicked(self,cb):
        print(f"{cb.text}selected..")
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DisplaySurvey()
    sys.exit(app.exec_())
        