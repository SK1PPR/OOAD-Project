import os 

class playlist(object):
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            print('Creating the playlist')
            cls._instance = super(playlist, cls).__new__(cls)
            cls.filename = ''
            cls._list = []
            cls.playing_index = 0
            cls._change_callback = None
        return cls._instance
            
    @property
    def change_callback(self):
        return self._change_callback
    
    @change_callback.setter
    def change_callback(self, value):
        self._change_callback = value
        
    @property
    def list(self):
        return self._list
    
    @list.setter
    def list(self, value):
        if self._list != value:
            self._list = value
            if self._change_callback is not None:
                self._change_callback()

    def add_file(self, file):
        new_file = self._list + [file]
        self.list = new_file 
    
    def remove_file(self,file):
        new_list = [item for item in self._list if item != file]
        self.list = new_list

    def save_playlist(self,filename):
        with open(filename, "w") as file:
            for file_path in self._list:
                file.write(file_path + '\n')
        self.filename = filename
        
    def load_playlist(self,filename):
        with open(filename, 'r') as file:
            self._list = [line.strip() for line in file.readlines()]
        self.filename = filename

    #getter and setters
    def get_files(self):
        return self._list

    def get_filename(self):
        return self.filename
    
    def increment_index(self):
        self.playing_index += 1
        
    def get_filename(self):
        if self.playing_index >= self._list.len():
            return None
        else:
            return self._list[self.playing_index]

    
def get_media_files_from_folder(folder_path): #folder path is full absolute path to selected folder
    media_extensions = {'.mp3', '.mp4', '.avi', '.mkv', '.mov', '.flv'}  #change according to what file extensions are allowed
    media_files = []

    for root, _, files in os.walk(folder_path):
        for file in _list:
            if os.path.splitext(file)[1].lower() in media_extensions:
                media_files.append(os.path.join(root, file))

    return media_files

def select_folder_and_create_playlist(folder_path): #folder path is full absolute path to selected folder
    #no folder selected
    if not folder_path:
        return  
    #extract media _list from folder
    media_files = get_media_files_from_folder(folder_path)
    #no media _list found
    if not media_files:
        print("No media _list found in the selected folder.")
        return

    playlist_new = playlist()
    playlist_new._list = media_files

    playlist_filename = input("Enter filename : ") #change to GUI messagebox
    playlist_filename = os.path.join(os.path.dirname(__file__), playlist_filename) #determines where the playlist will be stored
    playlist_new.save_playlist(playlist_filename)

    print(f"Playlist saved as {playlist_filename}")
    return playlist_new


