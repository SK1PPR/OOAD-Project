from ..Backend.Playlist import playlist
from ..Backend.Playlist import get_media_files_from_folder
from PyQt5 import QtWidgets, QtCore
from ..Drive.drive import google_drive_downloader_app
from .WatchPartyWidgets import join_tab, host_tab
import os

MEDIA_EXTENSIONS = ['.mp3', '.mp4', '.avi', '.mkv', '.mov', '.flv']

class menu_bar(QtWidgets.QMenuBar):
    
    # <--Signals-->
    open_file_signal = QtCore.pyqtSignal()
    
    
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
        edit_menu = QtWidgets.QMenu("&Edit" ,self)
        wp_menu = QtWidgets.QMenu("&WatchParty" ,self)
        help_menu = QtWidgets.QMenu("&Help" ,self)
        drive_menu = QtWidgets.QMenu("&Drive" ,self)
        
        #Adding the menu buttons
        self.addMenu(file_menu)
        self.addMenu(edit_menu)
        self.addMenu(wp_menu)
        self.addMenu(help_menu)
        self.addMenu(drive_menu)
        
        # Adding actions and submenus
        #File menu       
        add_action(file_menu, "&Open File", "Ctrl+O", "Open file", self.open_file)
        add_action(file_menu, "&Open Playlist", "Ctrl+Shift+O", "Open playlist", self.open_playlist)
        add_action(file_menu, "&Save", "Ctrl+S", "Save file with current name", save_file)
        add_action(file_menu, "Save As...", "Ctrl+Shift+S", "Save file as...", save_as)
        #Edit menu
        add_action(edit_menu, "Copy", "Ctrl+C", "Copy clip", copy_file)
        add_action(edit_menu, "Cut", "Ctrl+X", "Cut current clip", cut_file)
        add_action(edit_menu, "Paste", "Ctrl+V", "Paste clip from clipboard", paste_file)
        #WP menu
        add_action(wp_menu, "Join", "Ctrl+K", "Join an existing party", join_party)
        add_action(wp_menu, "Host", "Ctrl+L", "Host a new Watch-Party", host_party)
        #Drive menu
        # <-- Add functionality to display the current acount status -->
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
            
        
        
        
      
def add_action(menu, name, shortcut, tip, func, icon=None):
    if icon is None:
        action = QtWidgets.QAction(name, menu)
    else:
        action = QtWidgets.QAction(icon, name, menu)
    action.setShortcut(shortcut)
    action.setStatusTip(tip)
    action.triggered.connect(func)
    menu.addAction(action)
    

# File menu functions
# def start_cut():
    # declare slider time somewhere semi global, and link the front end slider to slider_object
    # start_time = slider_object.value() * clip.length() / 100 
    
# def end_cut():
    # declare slider time somewhere semi global, and link the front end slider to slider_object
    # end_time = slider_object.value() * clip.length() / 100   

# def add():
    # add the current video, start time and end time to cut_video function and add the returned clip to trimmed_clips array
    # if(start_time>=0 and end_time>0):
    #   timeline_obj.add_clip(cut_video(clip, start_time, end_time))
    #   start_time = -1
    #   end_time = -1
    # else:
    #   kachra
    
# def empty():
    # timeline_obj.clips.clear()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
#def save():
    # run the loop in clips concatenate each of the files and store the file at a given location

    
def open_playlist(self):
    pass
    # self.open_file_signal.emit("Hello darkness my old friend!")        

        
def save_file():
    pass 
        
def save_as():
    pass
   
#Editor functions     
def copy_file():
    pass

def cut_file():
    pass

def paste_file():
    pass        
        
#WP functions
def join_party():
    join_dialog = join_tab()
    join_dialog.exec_()

def host_party():
    host_dialog = host_tab()
    host_dialog.exec_()
        
#Drive functions
def import_file():
    drive_dialog = google_drive_downloader_app()
    drive_dialog.exec_()
        