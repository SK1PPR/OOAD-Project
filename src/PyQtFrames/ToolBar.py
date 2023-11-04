from .MenuBar import menu_bar
from PyQt5 import QtCore, QtWidgets

class tool_bar():
    
    def __init__(self):
        super(tool_bar, self).__init__()
        self.signal_connect()
    
    def signal_connect(self):
        self.obj = menu_bar()
        self.obj.open_file_signal.connect(self.update)
        print("Signal connected")

    def update(self):
        print("Hello darkness my old friend!")