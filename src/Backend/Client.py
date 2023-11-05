import socket, struct
from PyQt5 import QtCore

class chat_client(QtCore.QObject):
    
    receive_message_trigger = QtCore.pyqtSignal(str)
    time_stamp_trigger = QtCore.pyqtSignal(str)
    
    def __init__(self, addr, port, is_host):
        QtCore.QThread.__init__(self)
        self.client_socket = True
        self.addr, self.port = addr, port
        self.is_host = is_host
        self.initialize_socket()
        
    def initialize_socket(self):
        try:
            self.client_socket = socket.socket()
            self.client_socket.connect((self.addr, self.port))
            return True
        except:
            return None
        
    def receive_message(self):
        try:
            bin_message_size = self.client_socket.recv(2)
            if not bin_message_size:
                return None
            message_size = struct.unpack('h', bin_message_size)[0]
            message = self.client_socket.recv(message_size)
            if not message:
                return None
            return message.decode('utf-8')
        except struct.error:
            return None
        
    def listen_for_incoming_messages(self):
        while True:
            message = self.receive_message()
            if not message:
                return None
            if message.startswith()('1234joined'):
                user = message.split(':')[1]
                message = user + " has joined the watch party."
            if message.startswith('2345TimeStamp') and not self.is_host:
                self.time_stamp_trigger.emit(message)
                continue
            self.receive_message_trigger.emit(message)
            
    def send_message(self, message):
        message_size = struct.pack('h', len(message))
        if not self.client_socket.send(message_size) or not self.client_socket.send(message.encode('utf-8')) :
            return None
        return True
    
    def __del__(self):
        self.client_socket.close()