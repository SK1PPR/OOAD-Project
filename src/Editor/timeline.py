from moviepy.editor import VideoFileClip

class Timeline:
    _instance = None
    def __new__(obj):
        if obj._instance is None:
            obj._instance = super(Timeline, obj).__new__(obj)
            obj._clips = []
        return obj._instance

    def add_clip(self, clip):
        self._clips.append(clip)

    def remove_clip(self, clip):
        if clip in self._clips:
            self._clips.remove(clip)

    def clear_clips(self):
        self._clips.clear()

    def get_timeline_duration(self):
        if not self._clips:
            return 0
        return max(clip.end_time for clip in self._clips)

    def get_clips_in_range(self, start_time, end_time):
        return [clip for clip in self._clips if start_time <= clip.start_time <= end_time]
    
    def get_duration(clip):
        return clip.duration

