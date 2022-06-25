import time
import os
import shutil

SECONDS_IN_DAY = 24 * 60 * 60 #calculates the number of seconds in a day

src = "C:/Users/Student/Desktop/Folder1"
dst = "C:/Users/Student/Desktop/Folder2"

now = time.time() #method that returns the current tme
before = now - SECONDS_IN_DAY #will be used to calculate how logn ago file was last modified

def last_mod_time(fname):
    return os.path.getmtime(fname)

for fname in os.listdir(src):
    src_fname = os.path.join(src, fname) #concatenate file name to source directory
    if last_mod_time(src_fname) > before: #check to see if file has been modified witin thelast 24 hours
        dst_fname = os.path.join(dst, fname) ##concatenate file name to source directory
        shutil.move(src_fname, dst_fname)#move file last modified withn 24 hours to destination folder
