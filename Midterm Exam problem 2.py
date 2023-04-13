from tkinter import *
window = Tk()
window.geometry("500x400+10+10")
window.title("Midterm Exam Problem 2")
class Mywindow:
    def __init__ (self, name):

        self.lbl1 = Label(window,text= "My Full Name")
        self.lbl1.place(x = 190, y = 20)

        self.lbl2 = Label(window,text= "Enter Given Name:", fg="red")
        self.lbl2.place(x = 90, y = 50)

        self. txt1 = Entry(window,border = 2)
        self.txt1.place(x= 250, y =50)

        self.lbl3 = Label(window,text= "Enter Middle Name:", fg="red")
        self.lbl3.place(x = 90, y = 80)

        self.txt2 = Entry(window,border = 2)
        self.txt2.place(x= 250, y = 80)

        self.lbl4 = Label(window,text= "Enter Last Name:", fg="red")
        self.lbl4.place(x = 90, y = 110)

        self.txt3 = Entry(window,border = 2)
        self.txt3.place(x= 250, y = 110)

        self.lbl4 = Label(window,text= "My Full Name is:", fg="red")
        self.lbl4.place(x = 90, y = 150)

        self.txt4 = Entry(window,border = 2)
        self.txt4.place(x= 250, y = 150, width= 190)

        self.btn1 = Button(window, text = "Show Full Name")
        self.btn1.place(x = 200, y = 200)
        self.btn1.bind('<Button-1>', self.name)

        self.btnclear = Button(window, text="Clear All", command=self.clear)
        self.btnclear.place(x=200, y=250)

    def name(self):
        self.txt3.delete(0, 'end')
        num1 = int(self.txt1.get())
        num2 = int(self.txt2.get())
        num3 = int(self.txt3.get())
        result = print(self.txt1,self.txt2,self.txt3)

    def clear(self, clear):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')

myname = Mywindow(window)
window.mainloop()