from ..Backend.playlist import playlist
from ..Backend.playlist import get_media_files_from_folder
from PyQt5 import QtWidgets, QtCore
from ..Drive.drive import google_drive_downloader_app
import os

MEDIA_EXTENSIONS = ['.mp3', '.mp4', '.avi', '.mkv', '.mov', '.flv']

class menu_bar(QtWidgets.QMenuBar):
    
    
    def __init__(self, parent=None):
        #Create the menu bar
        super().__init__(parent)
        self.parent = parent
        self.setEnabled(True)
        self.setNativeMenuBar(False)
        self.setGeometry(0,0,700,30)
        self.playlist = playlist()
        
        # <-- Import icons over here -->
        
                
        #Create the various menu buttons
        file_menu = QtWidgets.QMenu("&File" ,self)
        wp_menu = QtWidgets.QMenu("&WatchParty" ,self)
        help_menu = QtWidgets.QMenu("&Help" ,self)
        drive_menu = QtWidgets.QMenu("&Drive" ,self)
        
        #Adding the menu buttons
        self.addMenu(file_menu)
        self.addMenu(wp_menu)
        self.addMenu(help_menu)
        self.addMenu(drive_menu)
        
        # Adding actions and submenus
        #File menu       
        add_action(file_menu, "&Open File", "Ctrl+O", "Open file", self.open_file)
        add_action(file_menu, "&Open Playlist", "Ctrl+Shift+O", "Open playlist", self.open_playlist)
        #WP Menu
        add_action(wp_menu, "Start", "Ctrl+L", "Host a new Watch-Party", self.start_party)
        #Drive menu
        add_action(drive_menu, "Import", "Ctrl-I", "Import directly from Google Drive", import_file)
        
    #File menu functionality
        
    def open_file(self):
        global MEDIA_EXTENSIONS
        
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open Video", '', 'Video (*mp4 *avi *mkv *flv *mov);;Audio (*mp3)')
        
        if filename is not None:
            playlist_t = playlist()
            playlist_t.add_file(filename)
            
    def open_playlist(self):
        
        foldername = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Open Folder"))
        
        if foldername != '':
            print('a')
            files = get_media_files_from_folder(foldername)
            print(files)
            playlist_t = playlist()
            for file in files:
                playlist_t.add_file(file)
                
    def start_party(self):
        self.parent.start_party()
            
      
def add_action(menu, name, shortcut, tip, func, icon=None):
    if icon is None:
        action = QtWidgets.QAction(name, menu)
    else:
        action = QtWidgets.QAction(icon, name, menu)
    action.setShortcut(shortcut)
    action.setStatusTip(tip)
    action.triggered.connect(func)
    menu.addAction(action)
       
        
#Drive functions
def import_file():
    drive_dialog = google_drive_downloader_app()
    drive_dialog.exec_()