class Timeline:
    def __init__(self):
        self.clips = []

    def add_clip(self, clip):
        self.clips.append(clip)

    def remove_clip(self, clip):
        if clip in self.clips:
            self.clips.remove(clip)

    def get_timeline_duration(self):
        if not self.clips:
            return 0
        return max(clip.end_time for clip in self.clips)

    def get_clips_in_range(self, start_time, end_time):
        return [clip for clip in self.clips if start_time <= clip.start_time <= end_time]

class MediaClip:
    def __init__(self, start_time, duration, media_file):
        self.start_time = start_time
        self.duration = duration
        self.media_file = media_file

    @property
    def end_time(self):
        return self.start_time + self.duration

    def __str__(self):
        return f"Clip: {self.media_file}, Start: {self.start_time}, End: {self.end_time}"