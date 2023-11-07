from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl
from ..Backend.playlist import playlist

class media_player(QMediaPlayer):
    
    def __init__(self,parent):
        self.parent = parent
        super().__init__(None, QMediaPlayer.VideoSurface)
        self.video_widget = QVideoWidget()
        self.playlist = playlist()
        self.playlist.change_callback = self.start_player
        self.has_opened = True
        
    def start_player(self):
        filename = self.playlist._list[0]
        if self.has_opened:
            self.open_file(filename)
            self.has_opened = False
            self.parent.enable()
            self.play()
        
        
    def open_file(self, filename):
        self.setMedia(QMediaContent(QUrl.fromLocalFile(''.join(filename))))
        self.setVideoOutput(self.video_widget)
        # self.stateChanged.connect(self.media_state_changed)
        self.positionChanged.connect(self.position_changed)
        
    # #Returns true if playing
    # def media_state_changed(self):
    #     if self.state() == QMediaPlayer.StoppedState:
    #         self.playlist.playing_index += 1
    #         file_list = self.playlist._list
    #         if len(file_list) < self.playlist.playing_index:
    #             self.open_file(self.playlist._list[self.playlist.playing_index])
            
    
    def position_changed(self, position):
        self.parent.get_position(position)
    
    
        
        
        
        
    