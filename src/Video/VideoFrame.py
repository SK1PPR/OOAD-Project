from .MediaPlayer import media_player
from PyQt5 import QtWidgets, QtCore

RANGE = 1000

class video_frame(QtWidgets.QWidget):
    
    def __init__(self,parent):
        global RANGE
        
        super().__init__(parent)
        
        #Buttons in video frame
        play_btn = QtWidgets.QPushButton()
        forward_btn = QtWidgets.QPushButton()
        backward_btn = QtWidgets.QPushButton()
        volume_up_btn = QtWidgets.QPushButton()
        volume_down_btn = QtWidgets.QPushButton()
        play_btn.setEnabled(False)
        forward_btn.setEnabled(False)
        backward_btn.setEnabled(False)
        volume_up_btn.setEnabled(False)
        volume_down_btn.setEnabled(False)
        
        #Connect buttons to functions
        
        time_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        time_slider.setRange(0,RANGE)
        time_slider.sliderMoved.connect(self.set_position)
        self.is_dragged = False
        time_slider.sliderPressed.connect(self.dragged)
        time_slider.sliderReleased.connect(self.released)
        #Connect timer to mediaplayer position
        
        #initialize mediaplayer
        self.media_player_widget = media_player()
        
        btn_layout = QtWidgets.QHBoxLayout()
        space1 = QtWidgets.QSpacerItem(200,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        space2 = QtWidgets.QSpacerItem(100,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        btn_layout.addItem(space1)
        btn_layout.addWidget(backward_btn, 1)
        btn_layout.addWidget(play_btn, 1)
        btn_layout.addWidget(forward_btn, 1)
        btn_layout.addItem(space2)
        btn_layout.addWidget(volume_down_btn, 1)
        btn_layout.addWidget(volume_up_btn, 1)
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
     
        
        
        
        
        