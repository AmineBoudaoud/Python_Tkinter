from tkinter import *
from tkinter import ttk

root =Tk()

entry1=ttk.Entry(root,width=40)
entry1.pack()
pythonintro=PhotoImage(file='pythonintro.png')
resize_pythonintro = pythonintro.subsample(10,10)
bnt1=ttk.Button(root,text='Get Text')
bntExit=ttk.Button(root,text='Exit',command=root.destroy)
bntExit.pack()
bnt1.pack()
bnt1.config(image=resize_pythonintro,compound=LEFT)
def Buclick():

        print(entry1.get(),end="\n")
        entry1.delete(0,END)
bnt1.config(command=Buclick)
root.mainloop()
