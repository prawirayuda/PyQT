
from re import sub
import sys
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,QPushButton,QFormLayout,QLineEdit,QTextEdit,QSpinBox,QComboBox,QHBoxLayout)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class GetAppForm(QWidget):
    def __init__(self):
         super().__init__()
         self.initUI()
         
    def initUI(self):
        self.setGeometry(100,100,300,400)
        self.setWindowTitle("Form GUI") 
        self.formWidgets() 
        self.show()
        
    def formWidgets(self):
        title = QLabel("Appointment sub form") 
        title.setFont(QFont("arial",18))
        title.setAlignment(Qt.AlignCenter)
        
        name = QLineEdit()
        name.resize(100,100)
        
        alamat = QLineEdit()
        noHp = QLineEdit()
        noHp.setInputMask("000-000-0000;")
        umur_label = QLabel("Umur")
        umur = QSpinBox()
        umur.setRange(1,100)
        
        
        label_tinggi_badan = QLabel("Tinggi")
        tinggi_badan =QLineEdit()
        tinggi_badan.setPlaceholderText("cm")
        
        label_berat_badan = QLabel("Tinggi")
        berat_badan =QLineEdit()
        berat_badan.setPlaceholderText("kg")
                     
        gender = QComboBox()
        gender.addItems(["Laki","pr"])
        
        surgery = QTextEdit()
        surgery.setPlaceholderText("Seperate by ','")
        
        gol_darah = QComboBox()
        gol_darah.addItems(["A","B","O"])
        
        jam = QSpinBox()
        jam.setRange(1,12)
        menit = QComboBox()
        menit.addItems([":00", ":15", ":30", ":45"])
        am_pm =QComboBox()
        am_pm.addItems(["AM","PM"])
        
        submit_button = QPushButton("submit it")
        submit_button.clicked.connect(self.close)
        
        
        
        h_box = QHBoxLayout()
        h_box.addSpacing(10)
        h_box.addWidget(umur_label)
        h_box.addWidget(umur)
        h_box.addWidget(label_tinggi_badan)
        h_box.addWidget(tinggi_badan)
        h_box.addWidget(label_berat_badan)
        h_box.addWidget(berat_badan)
        
        
        desire_time_h_box = QHBoxLayout()
        desire_time_h_box.addSpacing(10)
        desire_time_h_box.addWidget(jam)
        desire_time_h_box.addWidget(menit)
        desire_time_h_box.addWidget(am_pm)
        
        app_form_layout = QFormLayout()
        app_form_layout.addRow(title)

        app_form_layout.addRow("Fullname", name)
        app_form_layout.addRow("alamat", alamat)
        app_form_layout.addRow("No Hp",noHp)
        app_form_layout.addRow(h_box)
        # app_form_layout.addRow("Gender",gender)
        app_form_layout.addRow("Past Surgery",surgery)
        app_form_layout.addRow("Gender",gender)
        app_form_layout.addRow("Gol.Darah",gol_darah)
        app_form_layout.addRow("Desired Time", desire_time_h_box)
        app_form_layout.addRow(submit_button)
        
        self.setLayout(app_form_layout)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GetAppForm()
    sys.exit(app.exec_())
             
         