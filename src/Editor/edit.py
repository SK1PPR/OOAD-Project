from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.editor as mp
from tkinter import filedialog as fd
from ..PyQtFrames.MenuBar import menu_bar

start_time=-1
end_time=-1

class tools:
    def cut_video(input_video, start_time, end_time):
        video_clip = VideoFileClip(input_video).subclip(start_time, end_time)
        return video_clip

    # this is not to be shown as a tool on frontend
    def concatenate_video(clip1,clip2):
        input_file1=VideoFileClip(f'{clip1}')
        input_file2=VideoFileClip(f'{clip2}')
        new_clip=concatenate_videoclips([input_file1,input_file2]) 
        return new_clip
    
class Buttons:
    def __init__(self, parent):
        super().__init__(parent)
        self.menu_bar = menu_bar()

        
    def start_cutting(timee):
        start_time = timee
        print(start_time)
    
    def end_cutting(timee):
        end_time = timee
        # print(end_time)

    def add_it(self):
        print(self.menu_bar.currfile)
        


    def save_all():
        pass
    

        
    

    
    
        