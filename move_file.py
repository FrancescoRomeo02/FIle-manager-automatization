from datetime import datetime
from os import walk, rename
import shutil
import os
from dotenv import load_dotenv

# path of the directory to be scanned
path = os.environ['PATH_TO_SCAN']

# path for the different suffixes
path_image = os.environ['PATH_IMAGE']
path_video = os.environ['PATH_VIDEO']
path_documents = os.environ['PATH_DOCUMENTS']
path_compressed = os.environ['PATH_COMPRESSED']
path_executables = os.environ['PATH_EXECUTABLES']
path_not_recognized = os.environ['PATH_NOT_RECOGNIZED']

# tuple of suffixes to be scanned
suffixes_images = ('.jpg', '.jpeg', '.png')
suffixes_videos = ('.mp4', '.avi', '.mkv', '.mov')
suffixes_documents = ('.doc', '.docx', '.txt', '.pdf')
suffixes_compressed = ('.zip', '.rar', '.7z')
suffixes_executables = ('.exe', '.msi')

# function to move files to a specific directory


def move_file(file_path, destination_path):
    shutil.move(file_path, destination_path)

# function to rename the file


def renamefile(filename):
    # rename the file with the current date ( prevent duplicate )
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y").replace('/', '-')
    filenametmp = filename.split('.')
    new_filename = filenametmp[0] + '_' + \
        dt_string + '.' + filenametmp[1]
    rename(filename, new_filename)
    return new_filename

# function to scan the directory and move the files to the right directory


def files_detection():
    for (dirpath, dirnames, filenames) in walk(path):
        for filename in filenames:
            # make file path ( dirpath + filename + date)
            file_path = (dirpath + '/' + filename)

            # raneme the file
            file_path = renamefile(file_path)

            # check the file suffix
            if(filename.endswith(suffixes_images)):
                move_file(file_path, path_image)
            elif(filename.endswith(suffixes_videos)):
                move_file(file_path, path_video)
            elif(filename.endswith(suffixes_documents)):
                move_file(file_path, path_documents)
            elif(filename.endswith(suffixes_compressed)):
                move_file(file_path, path_compressed)
            elif(filename.endswith(suffixes_executables)):
                move_file(file_path, path_executables)
            else:
                move_file(file_path, path_not_recognized)
        break
