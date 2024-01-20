I have written a Python script for desktop automation. This tool monitors my download folder and automatically allocates each file according to their format. I used the PyAutoGUI module to perform GUI and desktop automation tasks.

While coding this script, I faced some technical problems such as detecting new files in the download folder, creating subfolders for different file formats, moving files from the download folder to the corresponding subfolders using PyAutoGUI, and handling errors and exceptions that may occur during the file operations.

To solve these problems, I applied the following solutions:
- I used the os module to list the files in the download folder and the os.path module to get their file names and extensions. I also used the time module to check the modification time of each file to detect new files.
- I used the os module to create subfolders for different file formats like images, videos, documents, etc. I also checked if the subfolders already existed to avoid creating duplicate folders.
- I used the PyAutoGUI module to move files from the download folder to the corresponding subfolders using the pyautogui.moveTo() and pyautogui.dragTo() functions. I also used the pyautogui.position() function to get the current position of the mouse cursor and the pyautogui.click() function to simulate mouse clicks.
- Finally, I used the try and except blocks to handle errors and exceptions that may occur during the file operations like FileNotFoundError, PermissionError, etc. I also used the logging module to log the errors and the status of the file operations.

