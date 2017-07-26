# import tkinter as tk

# def reDrew(tolS,tolN):
# 	pass
# def drawNewTree():
# 	pass


# root = tk.Tk()

# li = ['c','python','php','html','sql']
# movie = ['css','jquery','bootstrap']
# listb = tk.Listbox(root)
# listb2 = tk.Listbox(root)
# for item in li:
# 	listb.insert(0,item)
# for item in movie:
# 	listb2.insert(0,item)
# listb.pack()
# listb2.pack()

# root.mainloop()


from tkinter import *
import tkinter.messagebox

class MainWindow:
    def __init__(self):
        self.frame = Tk()
        self.frame.minsize(380,530)
        self.frame.maxsize(380,530)
        self.frame.title('python ui') #set name 

        self.label_name = Label(self.frame,text = "name:")
        self.label_age  = Label(self.frame,text = "age:")
        self.label_sex  = Label(self.frame,text = "sex:")

        self.text_name = Text(self.frame,height = "10",width = 30)
        self.text_age  = Text(self.frame,height = "10",width = 30)
        self.text_sex  = Text(self.frame,height = "1",width = 30)

        self.label_name.grid(row = 0,column = 0)
        self.label_age.grid(row = 1,column = 0)
        self.label_sex.grid(row = 2,column = 0)

        self.button_ok = Button(self.frame,text = "确定",width = 10)
        self.button_cancel = Button(self.frame,text = "cancel",width = 10)

        self.text_name.grid(row = 0,column = 1)
        self.text_age.grid(row = 1,column = 1)
        self.text_sex.grid(row = 2,column = 1)
        
        self.button_ok.grid(row = 3,column = 0)
        self.button_cancel.grid(row = 3,column = 1)

        self.button_ok.bind("<ButtonRelease-1>",self.buttonListener1)  
        self.button_cancel.bind("<ButtonRelease-1>",self.buttonListener2)
        self.frame.mainloop()

    def buttonListener1(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 1 dialog")  
    def buttonListener2(self,event):
        tkinter.messagebox.showinfo("messagebox","this is button 2 dialog")
    def text(self,event):
    	print 

frame = MainWindow()