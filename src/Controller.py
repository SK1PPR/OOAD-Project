from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication
from .PyQtFrames.MenuBar import menu_bar
from .PyQtFrames.StatusBar import status_bar
from .Video.VideoFrame import video_frame
from .WPmainWindow import MainClass
import os

class controller(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.set_main_player()
        QCoreApplication.instance().aboutToQuit.connect(self.cleanup)
    
    def set_main_player(self):
        menu = menu_bar(self)
        status = status_bar(self)
        frame = video_frame(self)
        self.setMenuWidget(menu)
        self.setCentralWidget(frame)
        self.setStatusBar(status)
  
        self.setWindowTitle("MediaWave")
        self.setGeometry(350,100,700,500)
        self.setWindowIcon(QtGui.QIcon("PlayerIcon.ico"))
        self.show()
        
    def start_party(self):
        self.wp_window = MainClass()
        self.wp_window.show()
        
        
    def cleanup(self):
        try:
            os.remove(os.path.join(os.path.dirname(__file__),'Drive','token.pickle'))
        except:
            print('token not found')
    