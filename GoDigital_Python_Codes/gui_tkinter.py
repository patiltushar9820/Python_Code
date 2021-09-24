#tkinter 
import tkinter
from tkinter import *
m=Tk()
m.title('welcome in Go Digital')
Label(m,text='LogIn Id').grid(row=0)
Label(m,text='Password').grid(row=1)
e1=Entry(m)
e2=Entry(m)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


m.mainloop()