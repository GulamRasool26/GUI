from tkinter import*
class MenuDemo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Menu Demo")
        #Creatig Menu bar
        menubar = Menu(self.window)
        self.window.config(menu= menubar)
        #Creating pulldown menu
        operationMenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Operation",menu=operationMenu)
        operationMenu.add_command(label="ADD",command = self.add)
        operationMenu.add_command(label="Subtract",command = self.subtract)
        operationMenu.add_separator()
        operationMenu.add_command(label="Multiply", command= self.multiply)
        operationMenu.add_command(label="Divide",command= self.divide)
        #create Exit Menu
        exitmenu = Menu(menubar,tearoff=0)
        menubar.add_cascade(label = "Exit",menu=exitmenu)
        exitmenu.add_command(label="Quit",command=self.window.quit)
        #Frame For inputs
        self.frm1 = Frame(self.window)
        self.frm1.grid(row=1,column=1,pady=10)
        Label(self.frm1,text="Number 1:").pack(side=LEFT)
        self.v1 = StringVar()
        Entry(self.frm1,width=5,textvariable=self.v1,justify=RIGHT).pack(side=LEFT)
        
        Label(self.frm1,text="Number 2:").pack(side=LEFT)
        self.v2 =StringVar()
        Entry(self.frm1,width=5,textvariable=self.v2,justify=RIGHT).pack(side=LEFT)
       
        
        Label(self.frm1,text="Result:").pack(side=LEFT)
        self.v3 = StringVar()
        Entry(self.frm1,width=5,textvariable=self.v3,justify=RIGHT).pack(side=LEFT)
        #Frame for buttons
        self.frm2 = Frame(self.window)
        self.frm2.grid(row=2,column=1,pady=10,sticky=E)
        Button(self.frm2,text="Add",command=self.add).pack(side=LEFT)
        Button(self.frm2,text="Subtract",command=self.subtract).pack(side=LEFT)
        Button(self.frm2,text="Multiply",command=self.multiply).pack(side=LEFT)
        Button(self.frm2,text="Divide",command=self.divide).pack(side=LEFT)
        self.window.mainloop()
    
    def add(self):
        self.v3.set(eval(self.v1.get())+eval(self.v2.get()))
    def subtract(self):
        self.v3.set(eval(self.v1.get())-eval(self.v2.get()))
    def multiply(self):
        self.v3.set(eval(self.v1.get())*eval(self.v2.get()))
    def divide(self):
        self.v3.set(eval(self.v1.get())/eval(self.v2.get()))


MenuDemo()