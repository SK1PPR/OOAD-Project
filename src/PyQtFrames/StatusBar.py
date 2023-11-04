from PyQt5 import QtWidgets

class status_bar(QtWidgets.QStatusBar):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setGeometry(0,470,700,30)
        self.showMessage("Ready", 3000)
        