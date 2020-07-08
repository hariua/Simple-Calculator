from tkinter import *

window=Tk()
window.title("Simple Calculator")
window.configure(bg="violet")
value=""
txt=StringVar()


entry=Entry(window,textvariable=txt,bg="powderblue",bd=5).grid(columnspan=4,padx=15,pady=15)

window.mainloop()