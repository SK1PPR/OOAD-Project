import os 

class Playlist:
    def __init__(self):
        self.files = [] #list storing file paths (absolute)
        self.filename = ''

    def add_file(self, file):
        self.files.append(file) 
    
    def remove_file(self,file):
        self.files.remove(file)

    def save_playlist(self,filename): #filename is full path(including filename) where playlist will be saved as a text file
        with open(filename, "w") as file:
            for file_path in self.files:
                file.write(file_path + '\n')
        self.filename = filename
        
    def load_playlist(self,filename): #filename is full path(including filename) where playlist will be loaded from
        with open(filename, 'r') as file:
            self.files = [line.strip() for line in file.readlines()]
        self.filename = filename

    #getter and setters
    def get_files(self):
        return self.files

    def get_filename(self):
        return self.filename

    
def get_media_files_from_folder(folder_path): #folder path is full absolute path to selected folder
    media_extensions = {'.mp3', '.mp4', '.avi', '.mkv', '.mov', '.flv'}  #change according to what file extensions are allowed
    media_files = []

    for root, _, files in os.walk(folder_path):
        for file in files:
            if os.path.splitext(file)[1].lower() in media_extensions:
                media_files.append(os.path.join(root, file))

    return media_files

def select_folder_and_create_playlist(folder_path): #folder path is full absolute path to selected folder
    #no folder selected
    if not folder_path:
        return  
    #extract media files from folder
    media_files = get_media_files_from_folder(folder_path)
    #no media files found
    if not media_files:
        print("No media files found in the selected folder.")
        return

    playlist = Playlist()
    playlist.files = media_files

    playlist_filename = input("Enter filename : ") #change to GUI messagebox
    playlist_filename = os.path.join(os.path.dirname(__file__), playlist_filename) #determines where the playlist will be stored
    playlist.save_playlist(playlist_filename)

    print(f"Playlist saved as {playlist_filename}")
    return playlist


