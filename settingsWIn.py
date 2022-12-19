import tkinter as tk

#settings window, adjust time, and breaks
class settings:
    def __init__(self,update):
        self.win2 = tk.Toplevel()
        self.win2.title("Settings")
        self.update = update
        
        self.workTime = tk.StringVar()
        self.shortTime = tk.StringVar()
        self.longTime = tk.StringVar()
        
        
        # work interval Gui Setting
        workLabel = tk.Label(self.win2, text= "Work interval duration")
        workLabel.place(x= 10, y= 10)
        
        workEntry = tk.Entry(self.win2, width= 3,  textvariable= self.workTime) ## entry window for work interval tiem duration, user input.
        workEntry.place(x= 130, y= 10)
        
        #short break GUI setting
        shortLabel = tk.Label(self.win2, text= "Short break duration")
        shortLabel.place(x= 10, y= 40)
        
        shortEntry = tk.Entry(self.win2, width= 3, textvariable= self.shortTime) ## entry window for short interval time duration, user input
        shortEntry.place(x= 130, y = 40)
        #long break GUI setting
        longLabel = tk.Label(self.win2, text= "long break duration")
        longLabel.place(x= 10, y= 70)
        
        longEntry = tk.Entry(self.win2, width= 3, textvariable= self.longTime)
        longEntry.place(x= 130, y= 70)
    
        # APPLY SETTINGS BUTTON, command submit, passes values to main window
        applyBtn = tk.Button(self.win2, text= "apply changes", command= self.submit)
        applyBtn.place(x=70, y=90)
        
    #passes values to main window
    def submit(self):
        self.update(self.workTime.get(), self.shortTime.get(),self.longTime.get())

