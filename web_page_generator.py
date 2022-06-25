
from tkinter import *

win = Tk()
l = Label(win, text="Enter the body text for the page and click Submit")
l.pack(side= TOP, padx= 10, pady=5)
b1 = Button(win, text="Submit")
b1.pack(side=RIGHT, padx =10)

v = StringVar()
e = Entry(win, textvariable =v)
e.pack(side=LEFT, padx= 10)

v.get()

import webbrowser
f = open("summer_sale.html", "w")

message = ("""<html><body>
<h1>
Stay tuned for our amazing summer sale!
</h1>
</body>
</html>""")
f.write(message)
f.close()

webbrowser.open_new_tab('summer_sale.html')

