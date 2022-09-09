from  tkinter import *
from tkinter import messagebox
master = Tk()
master.geometry('300x200')
def MyNmae():
    messagebox.showinfo('this is tltie,',"Hello Python3")
bnt = Button(master,text='clicke me',command=MyNmae)
bnt.place(x=30,y=70)
list1 = Listbox(master)
list1.insert(1,'Python')
list1.insert(2,'Java')
list1.insert(3,'C')
list1.insert(4,'C++')
list1.insert(5,'Html')
list1.pack()
list1.insert(6,'javaScript')





master.mainloop()