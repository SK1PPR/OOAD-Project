from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl

class media_player(QMediaPlayer):
    
    def __init__(self):
        super().__init__(None, QMediaPlayer.VideoSurface)
        self.video_widget = QVideoWidget()
        
        
    def open_file(self, filename):
        self.setMedia(QMediaContent(QUrl.fromLocalFile(''.join(filename))))
        self.setVideoOutput(self.video_widget)
        self.stateChanged.connect(self.media_state_changed)
        self.positionChanged.connect(self.position_changed)
        
    #Returns true if playing
    def media_state_changed(self) -> bool:
        if self.state() == QMediaPlayer.PlayingState:
            self.pause()
            return True
        else:
            self.play()
            return False
    
    def position_changed(self, position):
        self.setPosition(position)
    
    
        
        
        
        
    