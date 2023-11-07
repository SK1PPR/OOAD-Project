from .MediaPlayer import media_player
from PyQt5 import QtWidgets, QtCore
from ..Backend.playlist import playlist
from ..Editor.edit import *
from ..styles.custom_widgets.videoProgressBar import video_progress_bar
from ..styles.custom_widgets.volumeSlider import volume_slider

RANGE = 10000

class video_frame(QtWidgets.QWidget):
    
    def __init__(self,parent):
        global RANGE
        
        super().__init__(parent)
        self.playlist = playlist()
        
        #Buttons in video frame
        self.play_btn = QtWidgets.QPushButton()
        self.forward_btn = QtWidgets.QPushButton()
        self.backward_btn = QtWidgets.QPushButton()
        self.start_cut = QtWidgets.QPushButton('Start Cut')
        self.end_cut = QtWidgets.QPushButton('End Cut')
        self.add_to_timeline = QtWidgets.QPushButton('Add Clip')
        self.save_timeline = QtWidgets.QPushButton('Save')
        self.vol_icon = QtWidgets.QPushButton()
        self.play_btn.setEnabled(False)
        self.forward_btn.setEnabled(False)
        self.backward_btn.setEnabled(False)
        self.start_cut.setEnabled(False)
        self.end_cut.setEnabled(False)
        self.add_to_timeline.setEnabled(False)
        self.save_timeline.setEnabled(False)
        
        #initialize mediaplayer
        self.media_player_widget = media_player(self)

        #Button icons
        self.play_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
        self.forward_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipForward))
        self.backward_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaSkipBackward))
        self.save_timeline.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_DialogSaveButton))
        self.vol_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaVolume))
        
        self.time_slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.time_slider.setRange(0,RANGE)
        self.time_slider.setSingleStep(1)
        self.time_slider.sliderMoved.connect(self.set_position)
        self.is_dragged = False

        #Tool Tips
        self.play_btn.setToolTip("Play/Pause")
        self.forward_btn.setToolTip("Play next media file")
        self.backward_btn.setToolTip("Play previous media file")
        self.start_cut.setToolTip("Start cut")
        self.end_cut.setToolTip("End Cut")
        self.add_to_timeline.setToolTip("Add to timeline")
        self.save_timeline.setToolTip("Save the current timeline")
        self.vol_icon.setToolTip("Adjust volume")
        
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
        self.start_cut.clicked.connect(self.cutting_start)
        self.end_cut.clicked.connect(self.cutting_end)
        self.add_to_timeline.clicked.connect(self.adding_timeline)
        self.save_timeline.clicked.connect(self.saving_timeline)
        self.vol_icon.clicked.connect(self.toggle_mute)
               
        
        
        
        btn_layout = QtWidgets.QHBoxLayout()
        space1 = QtWidgets.QSpacerItem(100,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        space2 = QtWidgets.QSpacerItem(600,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        space3 = QtWidgets.QSpacerItem(100,0, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)

        btn_layout.addItem(space1)

        btn_layout.addWidget(self.backward_btn, 1)
        btn_layout.addWidget(self.play_btn, 1)
        btn_layout.addWidget(self.forward_btn, 1)

        btn_layout.addItem(space2)

        btn_layout.addWidget(self.start_cut, 1)
        btn_layout.addWidget(self.end_cut, 1)
        btn_layout.addWidget(self.add_to_timeline, 1)
        btn_layout.addWidget(self.save_timeline, 1)        
        btn_layout.addWidget(self.vol_icon, 1)        
        btn_layout.addWidget(self.volume_slider,2)

        btn_layout.setContentsMargins(0,0,0,0)
        # btn_layout.addItem(space3)
        
        
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

    def get_time(self):
        global RANGE 
        return (int)((self.time_slider.value())*(self.media_player_widget.duration()/(1000*RANGE)))
    
    def cutting_start(self):
        # print("check")
        return Buttons.start_cutting(self,self.get_time())
    
    def cutting_end(self):
        return Buttons.end_cutting(self,self.get_time())
    
    def adding_timeline(self):
        return Buttons.add_it(self)
    
    def saving_timeline(self):
        return Buttons.save_all()
    
    def slider_being_moved(self):
        self.media_player_widget.blockSignals(True)
    
    def slider_stopped_moving(self):
        self.media_player_widget.blockSignals(False)

    def enable(self):
        self.play_btn.setEnabled(True)
        self.forward_btn.setEnabled(True)
        self.backward_btn.setEnabled(True)
        self.start_cut.setEnabled(True)
        self.end_cut.setEnabled(True)
        self.add_to_timeline.setEnabled(True)
        self.save_timeline.setEnabled(True)
        
    def play_pause(self):
        if self.is_paused:
            self.is_paused = False
            self.play_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPause))
            self.media_player_widget.play()
        else:
            self.is_paused = True
            self.play_btn.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaPlay))
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

    def toggle_mute(self):
        if self.media_player_widget.isMuted():
            self.media_player_widget.setMuted(False)  # Unmute
            self.vol_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaVolume))
            self.volume_slider.setValue(50)
        else:
            self.media_player_widget.setMuted(True)  # Mute
            self.vol_icon.setIcon(self.style().standardIcon(QtWidgets.QStyle.SP_MediaVolumeMuted))
            self.volume_slider.setValue(0)
        
                
     
        
        
        
        
        