from PyQt5 import QtWidgets
from ..PyQtFrames.MenuBar import menu_bar
from ..PyQtFrames.StatusBar import status_bar
from ..Video.VideoFrame import video_frame

class main_player(QtWidgets.QMainWindow):
    def __init__(self, parent):
        super().__init__(parent)
        
        menu = menu_bar(self)
        status = status_bar(self)
        frame = video_frame(self)
        self.setMenuWidget(menu)
        self.setCentralWidget(frame)
        self.setStatusBar(status)
        
        