import time
import os
import shutil

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

win = Tk()
win.geometry("600x250")
def src_folder():
   path= filedialog.askdirectory()
   src.delete(0, END)
   src.insert(0, path)

def dst_folder():
   path= filedialog.askdirectory()
   dst.delete(0, END)
   dst.insert(0, path)

def check_files_folder():
    SECONDS_IN_DAY = 24 * 60 * 60 #calculates the number of seconds in a day
    now = time.time() #method that returns the current tme
    before = now - SECONDS_IN_DAY #will be used to calculate how logn ago file was last modified

    #src = #Gets the selected folder by the user
    source=src.get()
    #dst = #Gets the selected destination folder from the user
    destination=dst.get()
    

    for fname in os.listdir(source):
        src_fname = os.path.join(source, fname) #used for checking time
        last_mod_time = os.path.getmtime(src_fname)
        if last_mod_time > before: #check to see if file has been modified witin thelast 24 hours
            shutil.move(source+'/'+fname, destination)#concatenate file name to source directory andmove file
            #last modified withn 24 hours to destination folder
   
l = Label(win, text="Enter source and desitnation directories and click Submit")
l.grid(row=0,column=1)   


# Button that calls function for selecting source directory
b2 = Button(win, text="Source", command=src_folder)
b2.grid(row=1,column=0)
# Entry for source
src= Entry(win, width=100)
src.grid(row=1,column=1)


# Button that calls function for selecting destination directory
b3 = Button(win, text="Desitnation", command=dst_folder)
b3.grid(row=2,column=0)
# Entry for destination
dst=Entry(win, width=100)
dst.grid(row=2,column=1)

#Submit Button
b1 = Button(win, text="Submit", command=check_files_folder)
b1.grid(row=5,column=1)



#Function got getting the path for source
    #Look up askdirectory() function from tkinter
    #Insert method from Python

    

#Function that gets the destination





