import os
import shutil
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the path to the downloads folder
downloads_path = ''

# Set the paths to the destination folders
movies_path = ''
pictures_path = ''
music_path = ''
zip_files_path = ''
series_path = ''

# Create a dictionary to map file extensions to destination folders
folders = {
    '.webm''.mkv''.mp4': movies_path,
    '.jpg''.jpeg''.png': pictures_path,
    '.mp3': music_path,
    '.zip''.exe': zip_files_path,
   '.mkv': series_path
}

def delete_duplicates(folder):
    # Create an empty set to store file hashes
    file_hashes = set()
    
    # Loop through the files in the folder
    for filename in os.listdir(folder):
        # Construct the file path
        file_path = os.path.join(folder, filename)
        
        # Compute the SHA-1 hash of the file
        with open(file_path, 'rb') as f:
            file_hash = hashlib.sha1(f.read()).hexdigest()
        
        # Check if the file hash is already in the set
        if file_hash in file_hashes:
            # Delete the duplicate file
            os.remove(file_path)
        else:
            # Add the file hash to the set
            file_hashes.add(file_hash)

class DownloadsHandler(FileSystemEventHandler):
    def on_created(self, event):
        # Check if the event is for a file (not a directory)
        if not event.is_directory:
            # Get the file path and name
            file_path = event.src_path
            file_name = os.path.basename(file_path)
            
            # Get the file extension
            file_ext = os.path.splitext(file_name)[1]
            
            # Check if the file extension is in the dictionary
            if file_ext in folders:
                # Get the destination folder
                dest_folder = folders[file_ext]
                
                # Construct the destination file path
                dest_file = os.path.join(dest_folder, file_name)
                
                # Copy the file to the destination folder
                shutil.copy(file_path, dest_file)
                
                # Delete duplicate files in the destination folder
                delete_duplicates(dest_folder)
    
    def on_modified(self, event):
        # Check if the event is for a file (not a directory)
        if not event.is_directory:
            print(f"File modified: {event.src_path}")
    
    def on_deleted(self, event):
        # Check if the event is for a file (not a directory)
        if not event.is_directory:
            print(f"File deleted: {event.src_path}")

if __name__ == "__main__":
    # Create an event handler
    event_handler = DownloadsHandler()
    
    # Create an observer
    observer = Observer()
    
    # Schedule the observer to monitor the downloads folder
    observer.schedule(event_handler, downloads_path, recursive=False)
    
    # Start the observer
    observer.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
