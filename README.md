## Overview:
This script is a desktop automation tool that monitors my download folder. It moves each file to a specific folder based on its file extension. The tool is written in Python and uses the os and shutil modules to perform file operations.

## Technical Problems:
Some technical problems that I faced while coding this script are:
- How to set the paths to the download and destination folders.
- How to create a dictionary to map file extensions to the destination folder.
- How to iterate over the files in the download folder and get their file extensions.
- How to move files from the download folder to the corresponding destination folders using shutil.

## Solutions:
To solve these technical problems, I applied the following solutions:
- I used the os.path.join() function to set the paths to the download and destination folders. This function joins one or more path components and returns a normalized path.
- I used a Python dictionary to create a key-value pair for each file extension and destination folder. A dictionary is a collection of items that are unordered, changeable, and indexed.
- I used the os.listdir() function to iterate over the files in the download folder. This function returns a list of all the files and directories in the specified path. I also used the os.path.splitext() function to get the file extension of each file. This function splits the pathname into a pair (root, ext) such that root + ext == p.
- I used the shutil.move() function to move files from the download folder to the corresponding destination folders. This function recursively moves a file or directory to another location.


