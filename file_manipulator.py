'''
Matt Myers
04/12/2022
File Mover/Renamer
This program will look at the filename of files
being put into /Downloads and move and rename
them.
'''
'''
TO DO
~~~~~~
> Make run at startup
> Add more destinations
> Make base for school(i.e. Clemson)
> Run in background
> Make file that has cheat names and paths
> If no prefixes sort by file type (i.e. .mp3 -> \Music)
> Add Installer prefix for /applications folder
'''
#Libraries
# from selectors import EpollSelector
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import time
##################################
# Classes and functions

def adjust_keys(file):
    
    #     img_exts = ['.png', '.jpg']
    #     mus_exts = ['.mp3', '.flac']
    #     vid_exts = ['.mp4', '.mkv']
    #     doc_exts = ['.pdf', '.txt']
    #     ext = os.path.splitext(file)[1]
    #     if ext in img_exts:
    #         fold = '\\Pictures'
    #     elif ext in mus_exts:
    #         fold = '\\Music'
    #     elif ext in vid_exts:
    #         fold = '\\Videos'
    #     elif ext in doc_exts:
    #         fold = '\\Documents'
    #     else:
    #         fold = '\\Other'
    #     return(fold)
    pass

def check_prefixes(filename):
    options = ['VR', 'EandM2', 'TechWriting']
    if any(option in filename for option in options):
        return(True)
    else:
        return(False)

def adjust_prefixes(filename):
    prefixes = ['VR','EandM2','TechWriting']
    paths = ['C:\\Users\\Waff\\Desktop\\newTest\\Clemson\\Spring_2022\\VR',
            'C:\\Users\\Waff\\Desktop\\newTest\\Clemson\\Spring_2022\\EandM2',
            'C:\\Users\\Waff\\Desktop\\newTest\\Clemson\\Spring_2022\\TechWriting']
    adjust_name = filename
    any_pref = any(pre in filename for pre in prefixes)
    pre = next(filter(lambda pre: pre in filename, prefixes), None)
    ind = prefixes.index(pre)
    while any_pref:
        if pre+'_.' in adjust_name:
            adjust_name = adjust_name.replace('_.', '.')
        if pre+'_' in adjust_name:
            adjust_name = adjust_name.replace(pre+'_', '')
        elif '_'+pre in adjust_name:
            adjust_name = adjust_name.replace('_'+pre, '')
        else:
            adjust_name = adjust_name.replace(pre, '')
        any_pref = any(pre in adjust_name for pre in prefixes)
        pre = next(filter(lambda pre: pre in adjust_name, prefixes), None)
        fold = paths[ind]
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
        for filename in os.listdir(folder_to_track):
            i=1
            new_name = filename
            if check_prefixes(filename):
                folder_destination, temp_filename = adjust_prefixes(filename)
                new_name = temp_filename
            file_exists = os.path.isfile(folder_destination + '\\' + temp_filename)
            while file_exists:
                new_name = temp_filename
                i += 1
                new_name = os.path.splitext(folder_to_track + '\\' + new_name)[0] + str(i) + os.path.splitext(folder_to_track + '\\' + new_name)[1]
                new_name = new_name.split("\\")[-1]
                file_exists = os.path.isfile(folder_destination + '\\' + new_name)
            src = folder_to_track + "\\" + filename
            new_name = folder_destination + "\\" + new_name
            os.rename(src, new_name)

#################################
if __name__ == '__main__':
    folder_to_track = "C:\\Users\\Waff\\Desktop\\Test"
    folder_destination = "C:\\Users\\Waff\\Desktop\\newTest"
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
