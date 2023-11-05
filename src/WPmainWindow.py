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
		self.finalString = None
		self.chatTunnel = None
		self.chatServer = None
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
		self.videoSyncTimer.timeout.connect(self.sendTimeStamp)