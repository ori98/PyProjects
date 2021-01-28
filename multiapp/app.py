import os
import tkinter as tk
from tkinter import Text, filedialog

root = tk.Tk()                          #consists of the entire structure

#listo of apps
apps = []


#reading the last opened apps
if os.path.isfile('save.txt'):             #path exists or not
    with open ("save.txt", 'r') as f:
        tempApps = f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]       #strip out the empty spaces

#adding some functionlaity to the button
def addApp():

    #to delete the names of the apps that have already been added to the list 
    for widget in frame.winfo_children():
        widget.destroy()

    #open up file directory, add app as we click it and save it in a list
    filename = filedialog.askopenfilename(initialdir  = "/", title = "Select File" ,
    filetypes = (("executables", "*.exe"),("all files", "*.*")))
    apps.append(filename)
    print(filename)

    #going through each app to make it appear in the application window
    for app in apps:
        label  = tk.Label(frame, text = app, bg = "gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)

#command to actually run the apps

canvas = tk.Canvas(root, height = 400, width = 400, bg = "#3071EA") #setup the resolution along with the bg color
canvas.pack()           #attach it to root

#adding a frame
frame = tk.Frame(root, bg = "white")

#centering the frame
frame.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

#attaching a button
openFile = tk.Button(root, text = "Open File", padx = 10, pady = 5, fg = "white", bg = "#3071EA", command = addApp)
openFile.pack()

#attaching another button
RunApps = tk.Button(root, text = "Run Apps", padx = 10, pady = 5, fg = "white", bg = "#3071EA", command = runApps)
RunApps.pack()


for app in apps:
    label = tk.Label(frame, text = app)
    label.pack()

root.mainloop()                         #consists of the GUI




#to save the last opened apps
with open("save.txt", 'w') as f:
    for app in apps:
        f.write(app + ",")
