import sys 

from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow 
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout 

from layout_colorwidget import Color 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        # Minimum size of widget
        self.setMinimumSize(650,300)
        
        # HLayout
        hlayout = QHBoxLayout()                 # horizontal layout 1
        hlayout2 = QHBoxLayout()                # horizontal layout 2
        hlayout.addWidget(Color("red"))
        hlayout.addWidget(Color('green'))
        
        # VLayout 
        vlayout = QVBoxLayout()
        vlayout.addWidget(Color("Blue"))
        
        # Setting horizontal layout in between
        # add hlayout
        vlayout.addLayout(hlayout)              
        vlayout.addWidget(Color("yellow"))
        
        hlayout2.addWidget(Color("brown"))
        hlayout2.addWidget(Color('orange'))
        hlayout2.addWidget(Color("puple"))
        # add hlayout2
        vlayout.addLayout(hlayout2)             
        
        widget = QWidget()
        widget.setLayout(vlayout)
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()