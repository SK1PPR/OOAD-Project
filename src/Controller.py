from PyQt5 import QtWidgets
from src.PyQtFrames.MenuBar import menu_bar
from src.PyQtFrames.ToolBar import tool_bar
from src.PyQtFrames.StatusBar import status_bar
from src.Video.VideoFrame import video_frame

class controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setGeometry(350,100,700,500)
        menu_bar_widget = menu_bar(self)
        stats = status_bar(self)
        self.setMenuWidget(menu_bar_widget)
        self.setStatusBar(stats)
        frame = video_frame(self)
        self.setCentralWidget(frame)
        
    