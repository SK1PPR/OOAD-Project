from PyQt5 import QtWidgets
import sys



# <---- Testing elements using this code ---->

# This is an example of how to test elements
#import the widget you want to test on the screen
from src.PyQtFrames.MenuBar import menu_bar 

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QMainWindow()
    window.setGeometry(350,100,700,500)
    window.show()

    #add widget here
    window.menuBar = menu_bar(window)
    
    
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()