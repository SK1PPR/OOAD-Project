from PyQt5 import QtWidgets, QtGui
from src.Backend.playlist import playlist
from src.Layouts.mainPlayer import main_player


class controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_main_player(parent)
    
    def set_main_player(self, parent):
        self.window = main_player(parent)
        
    