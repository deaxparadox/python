import sys 
from PyQt5.QtCore import QSize, Qt 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton

# subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('My App')
        button = QPushButton("Press Me!")
        
        self.setFixedSize(400, 300)
        
        # Set the cnetral widget of the Window.
        self.setCentralWidget(button)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()