import sys 
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QListWidget, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        
        widget = QListWidget()
        widget.addItems(["One", "Two", "Three"])
        
        # In QListWidget ther are two separate signals for the item, and the str 
        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget) 
        
    def index_changed(self, i):
        print(i.text())
        
    def text_changed(self, s):       # s is a str
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()