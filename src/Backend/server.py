import socket, threading, select, struct

class chat_server:
	
	def __init__(self, ip, port, auth, max_num_of_connections=5):
		self.client_lists = set()
		self.server_socket = None
		self.auth = auth
		self.auth_timeout = 5
		self.ip, self.port = ip, port
		self.max_num_of_connections = max_num_of_connections
		self.create_listening_server()
	
	def create_listening_server(self):
		self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.server_socket.bind((self.ip, self.port))
		self.server_socket.listen(self.max_num_of_connections)
	
	def listen_for_connections(self):
		while True:
			conn, (_, _) = self.server_socket.accept()
			message_size = self.receive_message_with_timeout(conn, 2)
			if message_size is None:
				conn.close()
				continue
			try:
				message_size = struct.unpack('h', message_size)[0]
			except struct.error:
				conn.close()
				continue
			message = self.receive_message_with_timeout(conn, message_size)
			if not message or message.decode('utf-8') != self.auth:
				conn.close()
				continue
			self.client_lists.add(conn)
			threading.Thread(target = self.receive_forever, args = (conn,), daemon=True).start()
	
	def receive_message_with_timeout(self, conn, size_of_message):
		receive_message, _, _ = select.select([conn], [], [], self.auth_timeout)
		if not receive_message:
			return None
		return receive_message[0].recvfrom(size_of_message)[0]

	def receive_message(self, conn):
		try:
			binmessage_size = conn.recv(2)
			if not binmessage_size:
				return None
			message_size = struct.unpack('h', binmessage_size)[0]
			message = conn.recv(message_size)
			if not message:
				return None
			return message.decode('utf-8')
		except (struct.error, ConnectionResetError):
			return None
	
	def receive_forever(self, conn):
		while True:
			message = self.receive_message(conn)
			if not message:
				conn.close()
				self.client_lists.remove(conn)
				return
			self.broad_cast(message, conn)
		conn.close()

	def broad_cast(self, message, sender_socket):
		to_be_deleted = []
		for client in self.client_lists:
			conn = client
			if conn is sender_socket:
				continue
			if not self.send_message(message, conn):
				to_be_deleted.append(client)
		
		for client in to_be_deleted:
			self.client_lists.remove(client)

	def send_message(self, message, conn):
		message_size = struct.pack('h', len(message))
		try:
			if not conn.send(message_size) or not conn.send(message.encode('utf-8')):
				return None
			return True
		except OSError:
			return None
	
	def clean_up(self):
		for client in self.client_lists:
			client.close()
		self.server_socket.shutdown(socket.SHUT_RDWR)
		self.server_socket.close()