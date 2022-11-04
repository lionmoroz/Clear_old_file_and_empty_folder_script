import os
import time

"""Cleare file and folder from emty dir and old file"""

DAYS = 5 # max age of file
SIZE_DELETE_FILES = 0
NUMBER_DELETE_FILES = 0
NUMBER_DELETE_EMPTY_FOLDERS = 0

DIRS_LIST = [
    "/home/vlad/project/python/clear_dir/asd",
]

now_time = time.time()

delete_time = now_time - (60*60*24*DAYS)

def clear_file(folders):
    global SIZE_DELETE_FILES
    global NUMBER_DELETE_FILES

    for root, dirs, files in os.walk(folders):
        for file in files:
            file_name = os.path.join(root, file)
            time_modification_file = os.path.getmtime(file_name)
            if time_modification_file < delete_time:
                size_file = os.path.getsize(file_name)
                SIZE_DELETE_FILES += size_file
                NUMBER_DELETE_FILES += 1
                print(f"Deleting file: {file_name}")
                os.remove(file_name)


def clear_empty_dir(folders):
    global NUMBER_DELETE_EMPTY_FOLDERS
    empty_folders_byrun = 0
    for root, dirs, files in os.walk(folders):
        if (not dirs) and (not files):
            NUMBER_DELETE_EMPTY_FOLDERS += 1
            empty_folders_byrun += 1
            print(f"We delete this folder: {root}")
            os.rmdir(root)
    if empty_folders_byrun >0:
        clear_empty_dir(folders) 

starttime = time.asctime()

for folder in DIRS_LIST:
    clear_file(folder)
    clear_empty_dir(folder)


finishtime = time.asctime()

print("----------------------------------------------")
print(f"Start time: {starttime}")
print(f"Size of all delete file: {SIZE_DELETE_FILES/1024} kB")
print(f"Number of all delete file: {NUMBER_DELETE_FILES}")
print(f"Number of all delete empty folders: {NUMBER_DELETE_EMPTY_FOLDERS}")
print(f"Finish time: {finishtime}")
print("----------------------------------------------")