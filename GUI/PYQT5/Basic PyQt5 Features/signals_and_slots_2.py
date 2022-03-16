from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
from PyQt5.QtCore import Qt 
import sys 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)
        
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
        
    def the_button_was_clicked(self):
        self.button.setText('You already clicked me.')
        self.button.setEnabled(False)
        
        # Alse change the window title
        self.setWindowTitle("My OneShot App")

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()