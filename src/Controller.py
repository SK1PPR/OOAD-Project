from PyQt5 import QtWidgets, QtGui
from src.Backend.playlist import playlist
from src.Layouts.mainPlayer import main_player
from PyQt5.QtCore import QCoreApplication
import os

class controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_main_player(parent)
        QCoreApplication.instance().aboutToQuit.connect(self.cleanup)
    
    def set_main_player(self, parent):
        self.window = main_player(parent)
        
    def cleanup(self):
        try:
            os.remove(os.path.join(os.path.dirname(__file__),'Drive','token.pickle'))
        except:
            print('token not found')
    