import sqlite3

conn = sqlite3.connect('new.db') #create the database


#Your database will require 2 fields: an auto-increment primary integer field
#and a field with the data type “string.”
with conn: 
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_textFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_file TEXT \
        )")
    conn.commit()

conn = sqlite3.connect('new.db')

# tuple of names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#loop through each object in the tuple to find the .txt files
for x in fileList:
    if x.endswith('txt'):
        with conn:
            cur = conn.cursor()
        #the value of each row will be one name out of the tuple therefore (x,)
        #will denote a one element tuple for each file ending in txt.
        #add qualifying data to the new.db with the code line below
            cur.execute("INSERT INTO tbl_textFiles (col_file) VALUES (?)", (x,))
            print(x) #print the qualifying text files to the console.

conn.close()
