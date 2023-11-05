from .MediaPlayer import media_player
from PyQt5 import QtWidgets, QtCore
from ..Backend.playlist import playlist
from ..styles.custom_widgets.videoProgressBar import video_progress_bar
from ..styles.custom_widgets.volumeSlider import volume_slider

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
        self.is_paused = False
        self.play_btn.clicked.connect(self.play_pause)
        self.forward_btn.clicked.connect(self.forward)
        self.backward_btn.clicked.connect(self.previous)
        
        #time slider
        self.time_slider = video_progress_bar(QtCore.Qt.Horizontal)
        self.time_slider.setRange(0,RANGE)
        self.time_slider.sliderPressed.connect(self.slider_being_moved)
        self.time_slider.sliderMoved.connect(self.set_position)
        self.time_slider.sliderReleased.connect(self.slider_stopped_moving)
        self.is_dragged = False
        
        #volume slider
        self.volume_slider = volume_slider(QtCore.Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.valueChanged.connect(self.change_volume)

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
        # btn_layout.addWidget(self.volume_down, 1)
        # btn_layout.addWidget(self.volume_up, 1)
        btn_layout.addWidget(self.volume_slider,1)
        btn_layout.setContentsMargins(0,0,0,0)
        
        
        screen_layout = QtWidgets.QVBoxLayout()
        screen_layout.addWidget(self.media_player_widget.video_widget)
        screen_layout.addWidget(self.time_slider)
        screen_layout.addLayout(btn_layout)
        
        self.setLayout(screen_layout)
    
    def set_position(self):
        global RANGE
        position = self.time_slider.value()
        pos = (int((self.media_player_widget.duration()/RANGE) * position))
        self.media_player_widget.setPosition(pos)
        
    def get_position(self, position):
        global RANGE
        # print(self.media_player_widget.duration())
        if self.media_player_widget.duration() != 0:
            pos = (int((position / self.media_player_widget.duration()) * RANGE))
            self.time_slider.setValue(pos)
    
    def slider_being_moved(self):
        self.media_player_widget.blockSignals(True)
    
    def slider_stopped_moving(self):
        self.media_player_widget.blockSignals(False)

    def enable(self):
        self.play_btn.setEnabled(True)
        self.forward_btn.setEnabled(True)
        self.backward_btn.setEnabled(True)
        self.volume_up.setEnabled(True)
        self.volume_down.setEnabled(True)
        
    def play_pause(self):
        if self.is_paused:
            self.is_paused = False
            self.media_player_widget.play()
        else:
            self.is_paused = True
            self.media_player_widget.pause()
    
    def forward(self):
        self.playlist.playing_index += 1
        if len(self.playlist._list) > self.playlist.playing_index:
            self.media_player_widget.stop()
            self.media_player_widget.open_file(self.playlist._list[self.playlist.playing_index])
            self.media_player_widget.play()
        else:
            self.media_player_widget.stop()
    
    def previous(self):
        if self.playlist.playing_index > 0:
            self.playlist.playing_index -= 1
            self.media_player_widget.open_file(self.playlist._list[self.playlist.playing_index])
            self.media_player_widget.play()
        else:
            pass
    
    def change_volume(self,volume):
        self.media_player_widget.setVolume(volume)
        
                
     
        
        
        
        
        