import tkinter as tk
from time import strftime #strftime bascially allows us to format date and time by our liking.

 #root window = main window where we'll display our elements

root = tk.Tk() #Here we are creating a root named object using tkinter class 
root.title("Digital Clock") #name that will be shown as the title of root.

#Function that will update and show the time and date 
def time():
    string = strftime('%H:%M:%S %p \n %d/%m/%Y')
    label.config(text = string)
    label.after(1000,time) #This will update the time every second and will show correct time in label.
    
label = tk.Label(root, font = ('calibri', 50, 'bold'), background = 'pink', foreground = 'black' ) #We'll place this object in root window and will assign font with tuple.

#Pack Method = Method of tkinter module which arranges elements in window
label.pack(anchor = 'center')

time()

#Main Loop= Method of tkinter module which puts window loop and wait for user input.
root.mainloop()

