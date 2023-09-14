from tkinter import *
window = Tk()

window.title("TikTakToe")
width = w = 1024 # Width 
height = h =  640 # Height

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.mainloop()