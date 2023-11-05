import sys
from PyQt5 import QtCore, QtWidgets

class join_tab(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Join WatchParty")
        self.setGeometry(350,250,400,300)
        
        layout = QtWidgets.QVBoxLayout()
        id_input = QtWidgets.QLineEdit()
        id_input.setPlaceholderText("Enter session ID...")
        passkey_input = QtWidgets.QLineEdit()
        passkey_input.setPlaceholderText("Enter session passkey...")
        connect_button = QtWidgets.QPushButton("Join")
        connect_button.clicked.connect(call_server)
        layout.addWidget(id_input)
        layout.addWidget(passkey_input)
        layout.addWidget(connect_button)
        
        self.setLayout(layout)
   
def call_server():
    #connect to server
    pass     
        
class host_tab(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Host WatchParty")
        self.setGeometry(350,250,400,300)
        
        self.label = QtWidgets.QLabel("Your selected media")
        
        #change session id according to ports and all
        self.session_id_label = QtWidgets.QLabel("session id")
        select_button = QtWidgets.QPushButton("Select file")
        passkey_set_input = QtWidgets.QLineEdit()
        passkey_set_input.setPlaceholderText("Set your session PassKey")
        passkey_set_input.setMaxLength(20)
        start_button = QtWidgets.QPushButton("Start Hosting")

        # Signals for buttons
        select_button.clicked.connect(self.select_file)
        start_button.clicked.connect(self.start_hosting)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(select_button)
        layout.addWidget(self.session_id_label)
        layout.addWidget(passkey_set_input)
        layout.addWidget(start_button)
        self.setLayout(layout)
    
    def select_file(self):
        global MEDIA_EXTENSIONS
        
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video", '', 'Video (*mp4 *avi *mkv *flv *mov);;Audio (*mp3)')
        self.label.setText(filename)

    def start_hosting(self):
        #change session id
        #start hosting logic from here
        pass
    