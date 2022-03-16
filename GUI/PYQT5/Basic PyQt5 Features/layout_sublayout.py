from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow, 
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QCheckBox
)
from PyQt5.QtGui import (
    QPalette,
    QColor,
)

# Color class 
class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)
        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Subvertical')
        # self.setMinimumSize(600,450)
        # self.adjustSize()
        widget = QWidget()
        
        # hoirzontal layout
        vlayout1 = QHBoxLayout()
        
        # vertical layout
        vlayout2 = QVBoxLayout()
        vlayout3 = QVBoxLayout()
        vlayout4 = QVBoxLayout()
        
        # vlayout3 row1,2,3 in india flag
        hlayout1 = QHBoxLayout()
        vlayout3.addWidget(Color("Orange"))            
        vlayout3.addWidget(Color("white"))      
        vlayout3.addWidget(Color("green"))
        vlayout3.setContentsMargins(0, 0, 10, 0)
        
        # check box in column 2, block 1
        widget_check = QCheckBox("This is a Checkbox")
        widget_check.setCheckState(Qt.Checked)
        widget_check.stateChanged.connect(self.check_box_state)
        widget_check.setCheckable(False)
        vlayout2.addWidget(widget_check)
        
        #  column 2, block 2
        vlayout2.addWidget(Color('grey'))
        #  column 2, block 3
        vlayout2.addWidget(Color('brown'))
        #  column 2, block 4
        vlayout2.addWidget(Color("purple"))     
        vlayout2.setContentsMargins(0, 0, 10, 0)
        
        
        # add layout3 as sub layout to vlayout1
        vlayout1.addLayout(vlayout3)
        # add layout2 as sub layout to vlayout1
        vlayout1.addLayout(vlayout2)
        
        # set widget in vlayout4
        widget_test = QLabel("Hello")
        font = widget.font()
        font.setPointSize(30)
        widget_test.setFont(font)
        widget_test.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        # widget_test.setFixedWidth(400)
        # widget_test.setMinimumSize(400,200)
        vlayout4.addWidget(widget_test)
        vlayout1.addLayout(vlayout4)
        
        vlayout1.setSpacing(0)
        vlayout1.setContentsMargins(0, 0, 0, 0)
        
        
        widget.setLayout(vlayout1)
        self.setCentralWidget(widget)
    
    def check_box_state(self, s):
        print(s == Qt.Checked)
        print(s)
        
app = QApplication([])
window = MainWindow()
window.show()
app.exec_()

        