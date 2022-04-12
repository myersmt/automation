'''
Matt Myers
04/12/2022
File Mover/Renamer
This program will look at the filename of files
being put into /Downloads and move and rename
them.
'''
#Libraries
# from selectors import EpollSelector
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
import json
import shutil
##################################
# Classes and functions

def adjust_keys(file):
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

def check_prefixes(filename):
    options = ['VR', 'EandM2', 'TechWriting']
    for option in options:
        if option in filename:
            return(True)
        else:
            return(False)

def adjust_prefixes(filename):
    vr = 'VR'
    em = 'EandM2'
    tw = 'TechWriting'
    if vr in filename:
        if '_'+vr in filename:
            adjust_name = filename.replace('_'+vr, '')
        else:
            adjust_name = filename.replace(vr, '')
        fold = 'C:\\Users\\Waff\\Desktop\\newTest\\Clemson\\Spring_2022\\VR'
    elif em in filename:
        if '_'+em in filename:
            adjust_name = filename.replace('_'+em, '')
        else:
            adjust_name = filename.replace(em, '')
        fold = 'C:\\Users\\Waff\\Desktop\\newTest\\Clemson\\Spring_2022\\EandM2'
    elif tw in filename:
        if '_'+tw in filename:
            adjust_name = filename.replace('_'+tw, '')
        else:
            adjust_name = filename.replace(tw, '')
        fold = 'C:\\Users\\Waff\\Desktop\\newTest\\Clemson\\Spring_2022\\TechWriting'
    return(fold, adjust_name)

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
        folder_destination = "C:\\Users\\Waff\\Desktop\\newTest"
        #print("testInside")
        for filename in os.listdir(folder_to_track):
            i=1
            #print(filename)
            new_name = filename
            print(new_name)
            if check_prefixes(filename):
                folder_destination, temp_filename = adjust_prefixes(filename)
                new_name = temp_filename
            print(temp_filename)
            file_exists = os.path.isfile(folder_destination + '\\' + temp_filename)
            while file_exists:
                print(temp_filename)
                new_name = temp_filename
                i += 1
                new_name = os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + new_name)[1]
                new_name = new_name.split("\\")[-1]
                print(new_name)
                file_exists = os.path.isfile(folder_destination + '\\' + new_name)
            src = folder_to_track + "\\" + filename
            new_name = folder_destination + "\\" + new_name
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