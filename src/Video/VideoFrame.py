from .MediaPlayer import media_player
from PyQt5 import QtWidgets, QtCore
from ..Backend.Playlist import playlist

RANGE = 1000

class video_frame(QtWidgets.QWidget):
    
    def __init__(self,parent):
        global RANGE
        
        super().__init__(parent)
        self.playlist = playlist()
        
        #Buttons in video frame
        self.play_btn = QtWidgets.QPushButton()
        self.forward_btn = QtWidgets.QPushButton()
        self.backward_btn = QtWidgets.QPushButton()
        self.volume_up = QtWidgets.QPushButton()
        self.volume_down = QtWidgets.QPushButton()
        self.play_btn.setEnabled(False)
        self.forward_btn.setEnabled(False)
        self.backward_btn.setEnabled(False)
        self.volume_up.setEnabled(False)
        self.volume_down.setEnabled(False)
        
        #Button icons
        self.play_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
        self.forward_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaSeekForward))
        self.backward_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaSeekBackward))
        self.volume_up.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowUp))
        self.volume_down.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_ArrowDown))
        
        #Connect buttons to functions
        self.is_paused = True

        
        time_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        time_slider.setRange(0,RANGE)
        time_slider.sliderMoved.connect(self.set_position)
        self.is_dragged = False
        time_slider.sliderPressed.connect(self.dragged)
        time_slider.sliderReleased.connect(self.released)
        #Connect timer to mediaplayer position
        
        #initialize mediaplayer
        self.media_player_widget = media_player(self)
        
        btn_layout = QtWidgets.QHBoxLayout()
        space1 = QtWidgets.QSpacerItem(200,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        space2 = QtWidgets.QSpacerItem(100,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        btn_layout.addItem(space1)
        btn_layout.addWidget(self.backward_btn, 1)
        btn_layout.addWidget(self.play_btn, 1)
        btn_layout.addWidget(self.forward_btn, 1)
        btn_layout.addItem(space2)
        btn_layout.addWidget(self.volume_down, 1)
        btn_layout.addWidget(self.volume_up, 1)
        btn_layout.setContentsMargins(0,0,0,0)
        
        
        screen_layout = QtWidgets.QVBoxLayout()
        screen_layout.addWidget(self.media_player_widget.video_widget)
        screen_layout.addWidget(time_slider)
        screen_layout.addLayout(btn_layout)
        
        self.setLayout(screen_layout)
        
        
    def dragged(self):
        self.is_dragged = True
        
    def released(self,position):
        if self.is_dragged:
            self.is_dragged = False
            self.set_position(position)
    
    def set_position(self, position):
        global RANGE

        pos = (self.media_player_widget.duration()/RANGE) * position
        self.media_player_widget.position_changed(pos)
        
    def enable(self):
        self.play_btn.setEnabled(True)
        self.forward_btn.setEnabled(True)
        self.backward_btn.setEnabled(True)
        self.volume_up.setEnabled(True)
        self.volume_down.setEnabled(True)
        
        
                
     
        
        
        
        
        