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
##################################
# Classes and functions

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + "\\" + filename
            new_desination = folder_destination + "\\" + filename
            os.rename(src, new_desination)

#################################
folder_to_track = 'C:\\Users\\Waff\\Desktop\\Test'
folder_destination = 'C:\\Users\\Waff\\Desktop\\newTest'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()