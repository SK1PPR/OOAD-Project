import os
import pickle
import googleapiclient.discovery
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from PyQt5 import QtWidgets

# Define the scopes for the Google Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
#location of credentials.json
basedir = os.path.dirname(__file__)
credential_location = os.path.join(basedir,'credentials.json')
#location of the token being downloaded and searched for
token_location = os.path.join(basedir,'token.pickle')

def get_drive_service(): #Returns the authenticated API service object 
    creds = None

    # The file token.pickle stores the user's access and refresh tokens
    if os.path.exists(token_location): #change if path where you want to save and search for token.pickle
        with open(token_location, 'rb') as token:
            creds = pickle.load(token)

    # If there are no (valid) credentials, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credential_location, SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open(token_location, 'wb') as token: #change if path where you want to save and search for token.pickle
            pickle.dump(creds, token)

    return googleapiclient.discovery.build('drive', 'v3', credentials=creds)

# List folders in Google Drive (currently lists all folders and subfolders as distinct entities)
def list_folders(service): #returns items (a list of dictionary objects, each dict has 'id' and 'name' representing ID and name of folders found) 
    results = service.files().list(q="mimeType='application/vnd.google-apps.folder'", fields="files(id, name)").execute()
    items = results.get('files', [])

    if not items:
        print("No folders found.")
    else:
        return items

# Download media files from a folder
def download_media_files(service, folder_id, save_dir):
    results = service.files().list(q=f"'{folder_id}' in parents", fields="files(id, name, mimeType)").execute()
    files = results.get('files', []) 

    if not files:
        print("No media files found in the selected folder.")
    else:
        for file in files:
            allowed_types = ['video/mpeg','audio/mpeg'] #CHANGE TO ADD MIME OF ALL ALLOWED FILE TYPES
            if file['mimeType'] in allowed_types:
                request = service.files().get_media(fileId=file['id'])
                filename = os.path.join(save_dir, file['name'])
                with open(filename, 'wb') as f:
                    downloader = googleapiclient.http.MediaIoBaseDownload(f, request)
                    done = False
                    while not done:
                        status, done = downloader.next_chunk()
                        print(f"Downloading {file['name']}... {int(status.progress() * 100)}%")

def get_folders():
    service = get_drive_service()
    return list_folders(service)

#function to use in the application
def download_to_location(folder_id, save_directory):
    #provide this function with the folder_id and absolute path of the save_directory and it does the job 
    service = get_drive_service()
    download_media_files(service,folder_id,save_directory)
    
def map_folder_name_to_id(target_name):
    service = get_drive_service()
    folders = get_folders()

    for folder in folders:
        if folder['name'] == target_name:
            return folder['id']

    # Return None if the folder with the specified name is not found
    return None

class google_drive_downloader_app(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Google Drive Downloader")
        self.setGeometry(100,100,400,300)
        
        self.folder_checkboxes = []
        
        layout = QtWidgets.QVBoxLayout()
        folders = get_folders()
        
        for folder in folders:
            checkbox = QtWidgets.QCheckBox(folder['name'])
            self.folder_checkboxes.append(checkbox)
            layout.addWidget(checkbox)
            
        download_button = QtWidgets.QPushButton("Download Selected Folder")
        download_button.clicked.connect(self.download_selected_folder)
        layout.addWidget(download_button)
        
        self.setLayout(layout)
        
    def download_selected_folder(self):
        selected_folder = None
        for checkbox in self.folder_checkboxes:
            if checkbox.isChecked():
                selected_folder = checkbox.text()
                
        if selected_folder:
            save_dir = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Download Location")
            if save_dir:
                folder_id = map_folder_name_to_id(selected_folder)
                download_to_location(folder_id, save_dir)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please selct a folder to download")
            msg.setWindowTitle("Error")
            msg.exec_()
            