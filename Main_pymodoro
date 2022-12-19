'''
Manuel Paredes

Pymodoro

This app is pomodoro timer to help studying, it hahs a simple gui, and no distractions overall, ifuser want to change
time intervals go to settings and put the times that work for user.


My app ended up being simpler than i wanted, but i got the modular proogramming and everything is contain within an object, its easier to read, and understand.
'''

import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from background import settings
import time


class mainWin:
    # main window of the timer, has title timer, start button and settings button
    def __init__(self, master):
        #GUI configuration, 
        self.master = master
        self.frame = tk.Frame(self.master, width=245, height=200)
        self.frame['background'] = "#8c2e22"
        self.frame.pack()
        self.counter = 0
        
        
    
        ## title of the app, and values such as position in the window, font, or image used to display the title
        image_1 = Image.open('pymodoro.png')
        titleImg = ImageTk.PhotoImage(image_1)
        
        self.title = tk.Label(self.frame, image= titleImg)
        self.title.Image = titleImg
        self.title.place(x=0, y=0)

        ## variables for the time 
        self.minute = tk.StringVar()
        self.seconds = tk.StringVar()
        self.workTime = tk.StringVar()
        self.shortTime = tk.StringVar()
        self.longTime = tk.StringVar()
        
        ## set value of variables
        self.workTime.set("00")
        self.shortTime.set("00")
        self.longTime.set("00")
        self.minute.set("00")
        self.seconds.set("00")

        ## set variables on the GUI
        '''
        GUI only displays minutes and seeconds, other variables stated before this alter this two on the GUI
        '''
        self.minuteEntry = tk.Entry(self.frame, width=3, textvariable=self.minute)
        self.minuteEntry.place(x=100,y=60)
        secondEntry = tk.Entry(self.frame, width=3, textvariable=self.seconds)
        secondEntry.place(x=120,y=60)
        
        
    
        #settings button uses open function to open new window
        self.settingsbtn = tk.Button(root,text= "settings", command= self.open)
        self.settingsbtn.place(x=95, y=150)
        
        startBtn = tk.Button(self.frame, text="\N{Black Right-Pointing Triangle}", command= self.start)
        startBtn.place(x=110, y= 100)
    
    def update(self, workTime, shortTime, longTime):
        #brings values from settigns screen and set them as values for the timer
        self.workTime.set(workTime)
        self.shortTime.set(shortTime)
        self.longTime.set(longTime)
    
    def start(self):
        #counter keep number of iteration and changes the times from work to short break and long break
        self.counter += 1
        
        print (self.counter)
        try:
            # the input provided by entries stored in temp
            if self.counter % 8 == 0:
                temp = int(self.longTime.get()) * 60 + int(self.seconds.get())
            elif self.counter % 2 == 0:
                temp = int(self.shortTime.get())*60 + int(self.seconds.get())
            elif self.counter %2 != 0:
                temp = int(self.workTime.get())*60 + int(self.seconds.get())
        except:
            print("Please input the right value")
    
        while temp >-1:
         
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)
            self.minute.set("{0:2d}".format(mins))
            self.seconds.set("{0:2d}".format(secs))
  
            # updating the GUI window after decrementing the
            # temp value every time
            root.update()
            time.sleep(1)
  
            # when temp value = 0; then a messagebox pop's up
            # with a message:"Time's up"
            if (temp == 0):
                messagebox.showinfo("Time Countdown", "Time's up ")
            temp -= 1
    
    def open(self):
        #this function open a new window
        settingsWin = settings(self.update)
    
    
    
        
root = tk.Tk()
root.resizable(False,False)
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='pomicon.png'))
window = mainWin(root)
root.mainloop()
