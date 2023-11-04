import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QPushButton, QFileDialog
from drive import get_folders, download_to_location, map_folder_name_to_id

class GoogleDriveDownloaderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Google Drive Downloader")
        self.setGeometry(100, 100, 400, 300)

        self.folder_checkboxes = []

        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()

        # Fetch and list folders using get_folders
        folders = get_folders()

        for folder in folders:
            checkbox = QCheckBox(folder['name'])
            self.folder_checkboxes.append(checkbox)
            layout.addWidget(checkbox)

        # Add a download button
        download_button = QPushButton("Download Selected Folder")
        download_button.clicked.connect(self.download_selected_folder)
        layout.addWidget(download_button)

        self.setLayout(layout)

    def download_selected_folder(self):
        selected_folder = None
        for checkbox in self.folder_checkboxes:
            if checkbox.isChecked():
                selected_folder = checkbox.text()

        if selected_folder:
            save_dir = QFileDialog.getExistingDirectory(self, "Select Download Location")
            if save_dir:
                # Assuming you have a function to map folder name to its ID
                folder_id = map_folder_name_to_id(selected_folder)
                download_to_location(folder_id, save_dir)
        else:
            print("Please select a folder to download.")

def main():
    app = QApplication(sys.argv)
    window = GoogleDriveDownloaderApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
