from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtCore import Qt 
import sys 


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("My App")
        
        button = QPushButton("Press Me!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        
        # Set the central widget of the window
        self.setCentralWidget(button)
        
    def the_button_was_clicked(self):
        print("clicked!")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()