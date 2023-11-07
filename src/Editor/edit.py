from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.editor as mp
from tkinter import filedialog as fd
from ..Backend.playlist import playlist
from ..Editor.timeline import Timeline


import os
os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

start_time = -1
end_time = -1

class tools:
    def cut_video(input_video, start_time, end_time):
        if start_time != -1 and end_time != -1 :
            video_clip = VideoFileClip(input_video).subclip(start_time, end_time)
            return video_clip
        else:
            return None

    # this is not to be shown as a tool on frontend
    def concatenate_video(clip1,clip2):
        input_file1=VideoFileClip(f'{clip1}')
        input_file2=VideoFileClip(f'{clip2}')
        new_clip=concatenate_videoclips([input_file1,input_file2]) 
        return new_clip
    
class Buttons:
    _instance=  None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Buttons, cls).__new__(cls)
            cls.playlist = playlist()
            cls.start_time = -1
            cls.cut_tiem = -1
        return cls._instance
    
    def start_cutting(self,timee):
        self.start_time = timee
        # print(self.start_time)
    
    def end_cutting(self,timee):
        self.end_time = timee
        # print(self.end_time)

    def add_it(self):
        curr_video = self.playlist._list[self.playlist.playing_index]
        clip = tools.cut_video(rf'{curr_video}', self.start_time, self.end_time)
        time = Timeline()
        time.add_clip(clip)

    def save_all(self):
        time = Timeline()
        file_path = fd.asksaveasfilename(title="Save As",filetypes=[("MP4 files", "*.mp4")])
        file_path , _ = os.path.splitext(file_path)
        file_path += '.mp4'
        final_clip = concatenate_videoclips(time._clips)
        final_clip.write_videofile(rf'{file_path}',codec = 'libx264')


    

        
    

    
    
        