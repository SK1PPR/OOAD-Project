from PyQt5 import QtWidgets

class menu_bar(QtWidgets.QMenuBar):
    
    def __init__(self):
        #Create the menu bar
        super().__init__()
        self.setEnabled(False)
        self.setNativeMenuBar(False)
        print(self)
        
        #File menu
        file_menu = QtWidgets.QMenu("&File")
        self.addMenu(file_menu)
        file_menu.add
        
    
    
if __name__ == "__main__":
    menu = menu_bar()
    