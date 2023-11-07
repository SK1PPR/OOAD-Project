from PyQt5 import QtWidgets,QtGui,QtCore
from .PyQtFrames.ChatWidget import chat_widget
from .PyQtFrames.WPToolBarWidget import ToolBar
from .PyQtFrames.WPVideoFrame import VideoFrame
from pyngrok import ngrok,conf
from .Video.Player import Player
from .Backend.Server import chat_server
import sys, os, json, base64, threading, time, random, string, pyperclip, urllib

DEBUG = False

class MainClass(QtWidgets.QMainWindow):

	def __init__(self):
		QtWidgets.QMainWindow.__init__(self,None)
		self.isPaused = True
		self.isHost = False
		self.name = None
		self.videoServer = None
		self.final_string = None
		self.chatTunnel = None
		self.chat_server = None
		self.videoTunnel = None
		self.player = Player()
		self.askForName()
		self.createUI()
		self.createRandomUserPassword()
		with open('config.json','r') as f:
			self.configuration=json.load(f)
	
	def createUI(self):
		self.mainWidget = QtWidgets.QWidget()
		self.setCentralWidget(self.mainWidget)
		#Menu
		self.menuBar = self.menuBar()
		menu = self.menuBar.addMenu('Options')
		#Host
		host = QtWidgets.QAction('Host a Video', self)
		host.triggered.connect(self.createHost)
		#Client
		client = QtWidgets.QAction('Connect to Host', self)
		client.triggered.connect(self.createClient)
		#Close
		close = QtWidgets.QAction('Close App', self)
		close.triggered.connect(sys.exit)

		menu.addAction(host)
		menu.addAction(client)
		menu.addAction(close)

		#Adding Differet Frames and Widgets
		self.videoFrame = VideoFrame()
		self.chatWidget = chat_widget(self.name)
		self.toolBar = ToolBar(self.player,self)
		#FinalLayout
		self.vBoxLayout = QtWidgets.QVBoxLayout()
		self.upperBoxLayout = QtWidgets.QGridLayout()
		self.upperBoxLayout.setColumnStretch(0,2)
		self.upperBoxLayout.addWidget(self.videoFrame, 0, 0, 1, 1)
		self.upperBoxLayout.addWidget(self.chatWidget, 0, 1, 1, 6)
		self.vBoxLayout.addLayout(self.upperBoxLayout)
		self.vBoxLayout.addWidget(self.toolBar)
		self.setLayout(self.vBoxLayout)
		self.mainWidget.setLayout(self.vBoxLayout)

		#Creating a Timer to update GUI every 100ms
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(100)
		self.timer.timeout.connect(self.updateUI)

		#Creating a Timer which would send Data Packets every 1second to connected clients if the current Instance is host.
		self.videoSyncTimer = QtCore.QTimer(self)
		self.videoSyncTimer.setInterval(1000)
		self.videoSyncTimer.timeout.connect(self.sendtime_stamp)
  
	def updateUI(self):
		media_pos = int(self.player.getPosition()*1000)
		self.toolBar.positionSlider.setValue(media_pos)
		if not self.player.isPlaying():
			self.timer.stop()
			self.videoSyncTimer.stop()
			if not self.isPaused:
				self.toolBar.stop()

	def sendtime_stamp(self):
		media_pos = int(self.player.getAbsolutePosition()/1000)
		final_string = f'2345time_stamp:{not self.player.isPlaying()}:{media_pos}'
		self.chat_server.broad_cast(final_string, None)

	def receivetime_stamp(self, msg):
		_, host_paused, time_stamp = msg.split(':')
		time_stamp = int(time_stamp)
		host_paused = host_paused == 'True'
		if abs(self.player.getAbsolutePosition()/1000-time_stamp)>2:
			self.player.setTime(time_stamp*1000)
		if (not host_paused and not self.player.isPlaying()) or (host_paused and self.player.isPlaying()):
			self.player.playPause()
		
	def createRandomUserPassword(self):
		self._userName = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
		self._password = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
  
	def _getConcatUserPassword(self):
		return f'{self._userName}:{self._password}'

	def askForName(self):
		name,ok_pressed=QtWidgets.QInputDialog.getText(None, "Enter your NickName", "Enter your NickName:",QtWidgets.QLineEdit.Normal,"")
		if not ok_pressed or not name:
			self.name='NoobMaster69'
		self.name=name
	
	def createNgrokTunnels(self,file_folder):
		ngrok.set_auth_token(self.configuration['ngrokAuthKey'])
		conf.get_default().ngrok_path = self.configuration['ngrokPath']
		class b:
			def __init__(self,a):
				self.public_url=a
		if not DEBUG:
			self.videoTunnel = ngrok.connect(f'file:///{file_folder}','http',auth=f'{self._getConcatUserPassword()}')
			self.chatTunnel = ngrok.connect(self.configuration['chat_serverPort'],'tcp')
		else:
			file_name = [i for i in __import__('os').listdir(file_folder) if i.endswith('.mp4')][0]
			self.videoTunnel = b(f"{file_folder}/{file_name}")
			self.chatTunnel = b(f'tcp://0.0.0.0:{self.configuration["chat_serverPort"]}')

	def createHost(self):
		self.cleanUp()
		file_name = QtWidgets.QFileDialog.getOpenfile_name(self, 'Choose video file which you wanna stream.', os.path.expanduser('~'))
		if not file_name[0]:
			return
		file_path = file_name[0]
		file_folder = '/'.join(file_path.split('/')[:-1])
		file_name = file_path.split('/')[-1]
		self.createNgrokTunnels(file_folder)
		self.chat_server = chat_server('0.0.0.0' ,self.configuration['chat_serverPort'],self._getConcatUserPassword())
		threading.Thread(target=self.chat_server.listen_for_connections,daemon=True).start()
		time.sleep(1)
		self.chatWidget.intializeClient('0.0.0.0', self.configuration['chat_serverPort'], self._getConcatUserPassword(), True)
		self.toolBar.volumeSlider.setEnabled(True)
		self.toolBar.playButton.setEnabled(True)
		self.toolBar.stopButton.setEnabled(True)
		self.toolBar.positionSlider.setEnabled(True)
		self.isHost = True
		# self.chatWidget.client.time_stampTrigger.connect(self.receivetime_stamp)
		window_name = self.player.openFileOrUrl(file_path)
		self.setWindowTitle(window_name)
		self.player.setWindowToPyQT(self.videoFrame.winId())
		self.final_string = ';;;'.join([self.chatTunnel.public_url, self.videoTunnel.public_url, urllib.parse.quote(file_name), self._getConcatUserPassword()])
		self.final_string = base64.b64encode(self.final_string.encode('ascii')).decode('ascii')
		msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information , 'Copy to ClipBoard', 'Click on Yes to copy the String to ClipBoard you can then send it to your friend to add them in your session.')
		msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
		msg_box.buttonClicked.connect(self.copyToClipBoard)
		msg_box.exec_()
		self.videoSyncTimer.start()

	def createClient(self):
		self.cleanUp()
		b64string,ok_pressed = QtWidgets.QInputDialog.getText(None, "Enter the String given to you","Enter The String given to you by Others.", QtWidgets.QLineEdit.Normal,"")
		if not ok_pressed or not b64string:
			return 
		try:
			decoded_strings = base64.b64decode(b64string).decode('ascii').split(';;;')
			self.chatWidget.intializeClient(decoded_strings[0].split(':')[1][2:], int(decoded_strings[0].split(':')[2]), decoded_strings[3], False)
			if not DEBUG:
				video_url = decoded_strings[1].split('//')
				video_url = video_url[0] + '//' + decoded_strings[3] + '@' + video_url[1] + '/' + decoded_strings[2]
			else:
				video_url = decoded_strings[1]

		except (IndexError, base64.binascii.Error) as e:
			msg_box = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical, 'Invalid String', 'The String Given is either invalid or malfunctioned.')
			msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
			msg_box.exec_()
			return
		
		self.chatWidget.client.time_stampTrigger.connect(self.receivetime_stamp)
		window_name = self.player.openFileOrUrl(video_url)
		self.setWindowTitle(window_name)
		self.player.setWindowToPyQT(self.videoFrame.winId())
		self.toolBar.playButton.setEnabled(False)
		self.toolBar.stopButton.setEnabled(False)
		self.toolBar.positionSlider.setEnabled(False)
		self.toolBar.volumeSlider.setEnabled(True)
		self.isHost = False
		self.player.playPause()
		self.player.playPause()

	def copyToClipBoard(self,button):
		if button.text=='No':
			return
		pyperclip.copy(self.final_string)

	def cleanUp(self):
		if self.videoTunnel and self.chatTunnel:
			ngrok.disconnect(self.videoTunnel.public_url)
			ngrok.disconnect(self.chatTunnel.public_url)
		self.chatWidget.cleanUp()
		if self.chat_server:
			self.chat_server.clean_up()
