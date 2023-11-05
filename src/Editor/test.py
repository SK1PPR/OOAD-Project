# from tkinter import filedialog as fd
# from moviepy.editor import VideoFileClip, concatenate_videoclips
# import moviepy.editor as mp


# def cut_video(input_video, start_time, end_time):
#         video_clip = VideoFileClip(input_video).subclip(start_time, end_time)
#         print(video_clip.duration)
#         return video_clip


# input =r"D:\Downlfrom moviepy.editor import VideoFileClip, concatenate_videoclips
# import moviepy.editor as mp
# from tkinter import filedialog as fd
# from ..Backend.Playlist import playlist
# from ..Editor.timeline import Timeline

# start_time = -1
# end_time = -1

# class tools:
#     def cut_video(input_video, start_time, end_time):
#         video_clip = VideoFileClip(input_video).subclip(start_time, end_time)
#         print(video_clip.duration)
#         return video_clip

#     # this is not to be shown as a tool on frontend
#     def concatenate_video(clip1,clip2):
#         input_file1=VideoFileClip(f'{clip1}')
#         input_file2=VideoFileClip(f'{clip2}')
#         new_clip=concatenate_videoclips([input_file1,input_file2]) 
#         return new_clip
    
# class Buttons:
#     _instance=  None
    
#     # def __init__(self, parent):
#     #     super().__init__(parent)
#     #     self.playlist = playlist()
#     #     self.start_time = -1
#     #     self.cut_tiem = -1

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(Buttons, cls).__new__(cls)
#             cls.playlist = playlist()
#             cls.start_time = -1
#             cls.cut_tiem = -1
#         return cls._instance
    
#     def start_cutting(self,timee):
#         self.start_time = timee
#         # print(self.start_time)
    
#     def end_cutting(self,timee):
#         self.end_time = timee
#         # print(self.end_time)

#     def add_it(self):
#         curr_video = self.playlist._list[self.playlist.playing_index]
#         print(curr_video)
#         print(self.start_time)
#         print(self.end_time)
#         clip = tools.cut_video(rf'{curr_video}', self.start_time, self.end_time)
#         time = Timeline()
#         time.add_clip(clip)

#     def save_all():
#         time = Timeline()
#         # final_clip = None
#         for items in time._clips:
#             # print(items.duration)
#             file_path = fd.asksaveasfilename(
#                 title="Save As",
#                 filetypes=[("MP4 files", "*.mp4")]
#             )
#             print(file_path)
#             items.write_videofile(rf'{file_path}', codec = 'libx264')


    

        
    

    
    
#         oads\hi.mp4"

# clip=cut_video(input,0,15)
# clips=[]
# clips.append(clip)
# for items in clips:
#     file_path = fd.asksaveasfilename(
#         title="Save As",
#         filetypes=[("MP4 files", "*.mp4")]
#     )
#     items.write_videofile(rf'{file_path}',codec='libx264')