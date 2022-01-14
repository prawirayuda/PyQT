import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QComboBox,QSpinBox,QHBoxLayout,QVBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class SelectItems(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(300,300,300,300)
        self.setWindowTitle("Form")
        self.ItemandPrice()
        self.show()
        
    def ItemandPrice(self):
        info_label = QLabel("select one of your problem")
        info_label.setFont(QFont("arial",16))
        info_label.setAlignment(Qt.AlignCenter)
        
        self.display_total_label = QLabel("Total Price: Rp.")
        self.display_total_label.setFont(QFont("arial",16))
        self.display_total_label.setAlignment(Qt.AlignRight)
        
        daftar_menu =["ayam","telur","asas","awer","jfhdu"]
        
        lunch_cb1 = QComboBox()
        lunch_cb1.addItems(daftar_menu)
        lunch_cb2 = QComboBox()
        lunch_cb2.addItems(daftar_menu)
        
        self.price_sb1 = QSpinBox()
        self.price_sb1.setRange(0,100)
        self.price_sb1.setPrefix("Rp")
        self.price_sb1.valueChanged.connect(self.calculateTotal)
        
        self.price_sb2 = QSpinBox()
        self.price_sb2.setRange(0,100)
        self.price_sb2.setPrefix("Rp")
        self.price_sb2.valueChanged.connect(self.calculateTotal)
        
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()
        
        h_box1.addWidget(lunch_cb1)
        h_box1.addWidget(self.price_sb1)
        
        h_box2.addWidget(lunch_cb2)
        h_box2.addWidget(self.price_sb2)
        
        v_box = QVBoxLayout()
        v_box.addWidget(info_label)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        v_box.addWidget(self.display_total_label)
        self.setLayout(v_box)
        
    def calculateTotal(self):
        total = self.price_sb1.value() + self.price_sb2.value()
        self.display_total_label.setText(f"Total Spent: Rp {str(total)}")
        
        
        

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectItems()
    sys.exit(app.exec_())