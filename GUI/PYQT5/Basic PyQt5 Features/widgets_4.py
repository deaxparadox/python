import sys 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QComboBox, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        
        widget = QComboBox()
        widget.addItems(['One', 'Two', 'Three', 'Four', "Five", "Six", 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven'])
        
        # Insert Policy
        widget.setInsertPolicy(QComboBox.InsertAlphabetically)
        
        # Limit the number of items allowed in the box 
        widget.setMaxCount(10)
        
        widget.currentIndexChanged.connect(self.index_changed)
        widget.currentIndexChanged.connect(self.text_changed)
        
        self.setCentralWidget(widget)
        
    def index_changed(self, i):         # i is an int
        print(i)
        
    def text_changed(self, s):          # s is str
        print(s)
        
app=QApplication(sys.argv)
window=MainWindow()
window.show()
app.exec_()