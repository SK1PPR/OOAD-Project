from PyQt5 import QtWidgets
from src.Backend.Playlist import playlist
from src.Layouts.mainPlayer import main_player


class controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_main_player(parent)
        self.window.setGeometry(350,100,700,500)

    
    def set_main_player(self, parent):
        self.window = main_player(parent)
        
    