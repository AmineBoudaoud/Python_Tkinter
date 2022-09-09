from tkinter import *
from tkinter import ttk
root=Tk()
# root.title('CallBack')
button1=ttk.Button(root,text='Click Me 1!')
button1.pack()
button2=ttk.Button(root,text='Click Me 2!')
button2.pack()


buttonexit=ttk.Button(root,text='Exit')
buttonexit.pack()

style=ttk.Style()
style.theme_use('classic')
style.configure('TButton',foreground='black',font=('Arial',18,'bold'))
style.configure('TButton',background='red',font=('Arial',18,'bold'))
def buclick(x):
    print('Clicked{}'.format(x))

button1.config(command=lambda:buclick(1))
button2.config(command=lambda:buclick(2))

buttonexit.config(command=lambda:root.destroy())
root.mainloop()
