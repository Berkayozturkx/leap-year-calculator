#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        self.setWindowTitle("Artık Yıl Hesaplayıcı")
        grid = QGridLayout()
        
        grid.addWidget(QLabel("Yıl:"),1,0)
        
        self.yil = QLineEdit()
        grid.addWidget(self.yil,1,1,1,2)
        
        self.yaziAlani = QLabel("")
        grid.addWidget(self.yaziAlani,3,0)
        
        
        self.buton = QPushButton("Hesapla")
        self.buton.clicked.connect(self.hesapla)
        grid.addWidget(self.buton,2,2,1,1)
        
        v_box = QVBoxLayout()
        
        v_box.addStretch()
        v_box.addLayout(grid)
        v_box.addStretch()
        
        
        self.resize(220,120)
        self.setLayout(v_box)
        self.show()
        
    def hesapla(self):
        yil = 0
        try: yil = int(self.yil.text())
        except: pass
        
        if(yil >= 0):
            if(yil % 100 == 0):
                if(yil % 400 == 0):
                    self.yaziAlani.setText("{} yılı artık bir yıldır.".format(yil))
                else:
                    self.yaziAlani.setText("{} yılı artık bir yıl değildir.".format(yil))
            elif(yil % 4 == 0):
                self.yaziAlani.setText("{} yılı artık bir yıldır.".format(yil))
            else:
                self.yaziAlani.setText("{} yılı artık bir yıl değildir.".format(yil))
        else:
            self.yaziAlani.setText("Hatalı yıl girişi, yıl negatif olamaz.")
uygulama = QApplication(sys.argv)
pencere = MainWindow()
sys.exit(uygulama.exec_())


# In[ ]:




