from PyQt5 import QtWidgets, QtGui
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
  
        self.setWindowTitle("Media Player")
        self.setGeometry(350,100,700,500)
        self.setWindowIcon(QtGui.QIcon("../PlayerIcon.ico"))
        
        