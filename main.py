from PyQt5 import QtWidgets
import sys



# <---- Testing elements using this code ---->

# This is an example of how to test elements
#import the widget you want to test on the screen
from src.PyQtFrames.MenuBar import menu_bar
from src.PyQtFrames.ToolBar import tool_bar
from src.PyQtFrames.StatusBar import status_bar
from src.Video.VideoFrame import video_frame

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    window = QtWidgets.QMainWindow()
    window.setGeometry(350,100,700,500)
    
    menu_bar_widget = menu_bar(window)
    stats = status_bar(window)
    window.setMenuWidget(menu_bar_widget)
    window.setStatusBar(stats)
    frame = video_frame(window)
    window.setCentralWidget(frame)
    
    window.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()