import sys 

from PyQt5.QtCore import Qt 
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class Asset:
    # Image file
    otje = "otje.jpg"

class MainWindow(QMainWindow, Asset):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        widget = QLabel("Hello")
        widget.setPixmap(QPixmap(self.otje))
        
        # stretch and scale to fit the window completely
        widget.setScaledContents(True)
        
        self.setCentralWidget(widget)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()