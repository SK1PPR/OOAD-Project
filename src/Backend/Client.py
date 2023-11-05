import socket, struct
from PyQt5 import QtCore


class chat_client(QtCore.QObject):

	receiveMessageTrigger = QtCore.pyqtSignal(str)
	timeStampTrigger = QtCore.pyqtSignal(str)

	def __init__(self, addr, port, is_host):
		QtCore.QThread.__init__(self)
		self.clientSocket = None
		self.addr = addr
		self.port = port
		self.is_host = is_host
		self.intializeSocket()

	def intializeSocket(self):
		try:
			self.clientSocket = socket.socket()
			self.clientSocket.connect((self.addr, self.port))
			return True
		except:
			return None
	
	def receiveMessage(self):
		try:
			binmessage_size = self.clientSocket.recv(2)
			if not binmessage_size:
				return None
			message_size = struct.unpack('h', binmessage_size)[0]
			message = self.clientSocket.recv(message_size)
			if not message:
				return None
			return message.decode('utf-8')
		except struct.error:
			return None

	def listenForIncomingMessages(self):
		while True:
			message = self.receiveMessage()
			if not message:
				return None
			if message.startswith('1234joined'):
				user = message.split(':')[1]
				message = user + " has joined the chat."
			if message.startswith('2345TimeStamp'):
				if not self.is_host:
					self.timeStampTrigger.emit(message)
				continue
			self.receiveMessageTrigger.emit(message)

	def sendMessage(self, message):
		message_size = struct.pack('h', len(message))
		if not self.clientSocket.send(message_size) or not self.clientSocket.send(message.encode('utf-8')):
			return None
		return True

	def __del__(self):
		self.clientSocket.close()