from PyQt5.QtGui import QPainter, QColor,QPen
from PyQt5.QtWidgets import QSlider

class video_progress_bar(QSlider):
    def __init__(self,*a):
        super().__init__(*a)
        self.range = self.maximum()
        self.setStyleSheet("""
            QSlider::handle{
                width : 10px;
            }
        """)

    def paintEvent(self,event):
        self.range = self.maximum()
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QColor(214,104,83))
        painter.setBrush(QColor(214,104,83))            
        slider_x_cords = int(self.sliderPosition()/self.range* self.size().width())
        slider_y_cords = int(self.size().height())
        painter.drawRect(0,0,slider_x_cords,slider_y_cords)
        painter.setPen(QColor(247, 219, 167))
        painter.setBrush(QColor(247, 219, 167))            
        painter.drawRect(slider_x_cords,0,int(self.size().width()),slider_y_cords)
        painter.setPen(QColor(255, 255, 255))
        painter.setBrush(QColor(255, 255, 255)) 
        painter.drawRect(slider_x_cords,0,3,slider_y_cords)
        painter.end()
	

	
