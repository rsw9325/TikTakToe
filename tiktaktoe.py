from tkinter import *
window = Tk()

window.title("TikTakToe")
w = 1024 
h =  640 

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = (screen_width/2) - (w/2)
y = (screen_height/2) - (h/2)

window.geometry('%dx%d+%d+%d' % (w, h, x, y))

btn_1 = Button(window, text = "1", height = 4, width = 8)
btn_1.place(relx = 0.425, rely = 0.37, anchor = CENTER)

btn_2 = Button(window, text = "2", height = 4, width = 8)
btn_2.place(relx = 0.5, rely = 0.37, anchor = CENTER)

btn_3 = Button(window, text = "3", height = 4, width = 8)
btn_3.place(relx = 0.575, rely = 0.37, anchor = CENTER)

btn_4 = Button(window, text = "4", height = 4, width = 8)
btn_4.place(relx = 0.425, rely = 0.5, anchor = CENTER)

btn_5 = Button(window, text = "5", height = 4, width = 8)
btn_5.place(relx = 0.5, rely = 0.5, anchor = CENTER)

btn_6 = Button(window, text = "6", height = 4, width = 8)
btn_6.place(relx = 0.575, rely = 0.5, anchor = CENTER)

btn_7 = Button(window, text = "7", height = 4, width = 8)
btn_7.place(relx = 0.425, rely = 0.63, anchor = CENTER)

btn_8 = Button(window, text = "8", height = 4, width = 8)
btn_8.place(relx = 0.5, rely = 0.63, anchor = CENTER)

btn_9 = Button(window, text = "9", height = 4, width = 8)
btn_9.place(relx = 0.575, rely = 0.63, anchor = CENTER)


window.mainloop()