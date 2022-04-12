'''
Matt Myers
04/12/2022
File Mover/Renamer
This program will look at the filename of files
being put into /Downloads and move and rename
them.
'''
#Libraries
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json
import shutil
##################################
# Classes and functions

def check_keys(file):
    img_exts = ['.png', '.jpg']
    mus_exts = ['.mp3', '.flac']
    vid_exts = ['.mp4', '.mkv']
    doc_exts = ['.pdf', '.txt']
    ext = os.path.splitext(file)[1]
    if ext in img_exts:
        fold = '\\Pictures'
    elif ext in mus_exts:
        fold = '\\Music'
    elif ext in vid_exts:
        fold = '\\Videos'
    elif ext in doc_exts:
        fold = '\\Documents'
    else:
        fold = '\\Other'
    return(fold)

class MyHandler(FileSystemEventHandler):
    # #print("test")
    # def on_modified(self, event):
    #     #print("testInside")
    #     for filename in os.listdir(folder_to_track):
    #         i=1
    #         #print(filename)
    #         new_name = filename
    #         file_exists = os.path.isfile(folder_destination + '\\' + new_name)
    #         while file_exists:
    #             new_name = filename
    #             i += 1
    #             new_name = os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + new_name)[1]
    #             new_name = new_name.split("\\")[-1]
    #             file_exists = os.path.isfile(folder_destination + '\\' + new_name)
    #         src = folder_to_track + "\\" + filename
    #         new_name = folder_destination + "\\" + new_name
    #         os.rename(src, new_name)
    def on_created(self, event):
        #print("testInside")
        for filename in os.listdir(folder_to_track):
            i=1
            #print(filename)
            new_name = filename
            file_exists = os.path.isfile(folder_destination + check_keys(new_name) + '\\' + new_name)
            while file_exists:
                new_name = filename
                i += 1
                new_name = os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + new_name)[1]
                new_name = new_name.split("\\")[-1]
                file_exists = os.path.isfile(folder_destination + check_keys(new_name) + '\\' + new_name)
            src = folder_to_track + "\\" + filename
            new_name = folder_destination + check_keys(new_name) + "\\" + new_name
            os.rename(src, new_name)

#################################
#print(os.getcwd())
folder_to_track = "C:\\Users\\Waff\\Desktop\\Test"
#print(folder_to_track)
folder_destination = "C:\\Users\\Waff\\Desktop\\newTest"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        #print(os.getcwd())
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()