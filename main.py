from PyQt5 import QtWidgets
import sys



# <---- Testing elements using this code ---->

#import the widget you want to test on the screen
from .src.PyQtFrames.MenuBar import menu_bar

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QWidget()
    window.show()
    
    #add widget here
    
    
    print("Reached here")
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()