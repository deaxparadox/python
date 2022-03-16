import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QCheckBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        widget = QCheckBox("This is a checkbox")
        
        # you can specify a paritally checked state 
        # widget.setCheckState(Qt.Checked)
        widget.setCheckState(Qt.Unchecked)
        
        
        # set checked state programmaticlly
        # widget.setChecked(False)
        
        # For tristate: widget.setCheckState(Qt.PartaillyChecked)
        # Or: widget.setTriState(True)
        widget.stateChanged.connect(self.show_state)
        self.setCentralWidget(widget)
    
    def show_state(self, s):
        print(s == Qt.Checked)
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()