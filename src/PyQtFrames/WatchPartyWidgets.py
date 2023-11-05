import sys, socket
from PyQt5 import QtCore, QtWidgets
from ..Backend.Server import chat_server

IP = '127.0.0.1'
PORT = 5586

def get_session_id():
    global IP
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    IP = s.getsockname()[0]
    s.close()

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
        global IP, PORT
        
        super().__init__()
        self.setWindowTitle("Host WatchParty")
        self.setGeometry(350,250,400,300)
        
        self.label = QtWidgets.QLabel("Your selected media")
        
        #change session id according to ports and all
        self.session_id_label = QtWidgets.QLabel("session id")
        self.session_id_label.setText(IP + ":" + str(PORT))
        select_button = QtWidgets.QPushButton("Select file")
        self.passkey_set_input = QtWidgets.QLineEdit()
        self.passkey_set_input.setPlaceholderText("Set your session PassKey")
        self.passkey_set_input.setMaxLength(20)
        start_button = QtWidgets.QPushButton("Start Hosting")

        # Signals for buttons
        select_button.clicked.connect(self.select_file)
        start_button.clicked.connect(self.start_hosting)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(select_button)
        layout.addWidget(self.session_id_label)
        layout.addWidget(self.passkey_set_input)
        layout.addWidget(start_button)
        self.setLayout(layout)
    
    def select_file(self):        
        self.server_filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video", '', 'Video (*mp4 *avi *mkv *flv *mov);;Audio (*mp3)')
        self.label.setText(self.server_filename)

    def start_hosting(self):
        global IP, PORT
        
        if self.server_filename == '' or self.server_filename is None:
            return
        if self.passkey_set_input.text() == ' ' or self.passkey_set_input.text() is None:
            return
        
        self.server = chat_server(IP, PORT, 4)
    