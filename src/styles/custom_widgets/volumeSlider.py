import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor,QPen
from PyQt5.QtWidgets import QApplication, QMainWindow, QSlider, QVBoxLayout, QWidget

class volume_slider(QSlider):
    def __init__(self,*a):
        super().__init__(*a)
        self.range = self.maximum()
        self.setStyleSheet("""
            QSlider::handle{
                width : 100px;
            }
        """)

    def paintEvent(self,event):
        self.range = self.maximum()
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        slider_x_cords = int(self.sliderPosition()/self.range* self.size().width())
        slider_y_cords = int(self.size().height())
        painter.setPen(QColor(13,13,13))
        painter.setBrush(QColor(13,13,13))            
        painter.drawRect(0,0,int(self.size().width()),slider_y_cords)
        painter.setPen(QColor(200,255,200))
        painter.setBrush(QColor(200,255,200))            
        painter.drawRect(0,0,slider_x_cords,slider_y_cords)
        painter.end()
