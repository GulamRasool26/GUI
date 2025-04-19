from tkinter import*
class MenuDemo:
    def __init__(self):
        self.window = Tk()
        self.window.title("Menu Demo")
        
        self.active_input = "v1"
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
        Button(self.frm2,text="Add",command=self.add).pack(side=LEFT,padx=10)
        Button(self.frm2,text="Subtract",command=self.subtract).pack(side=LEFT,padx=10)
        Button(self.frm2,text="Multiply",command=self.multiply).pack(side=LEFT,padx=10)
        Button(self.frm2,text="Divide",command=self.divide).pack(side=LEFT,padx=10)
       
        # Frame for Number Buttons
        self.frm3 = Frame(self.window)
        self.frm3.grid(row=4, column=1, pady=10)

        b = 1
        for r in range(3):
            for c in range(3):
                Button(self.frm3, text=str(b), width=5, command=lambda d=b: self.append_digit(d)).grid(row=r, column=c, padx=3, pady=3)
                b = b + 1
        # Zero Button
        Button(self.frm3, text="0", width=16, command=lambda: self.append_digit(0)).grid(row=3, column=0, columnspan=3, pady=3)

        # Clear button
        Button(self.window, text="Clear", width=20, command=self.clear_all).grid(row=5, column=1, pady=10)

        # Toggle input buttons
        self.frm_toggle = Frame(self.window)
        self.frm_toggle.grid(row=3, column=1, pady=5)
        Button(self.frm_toggle, text="Edit Number1", command=lambda: self.set_active("v1")).pack(side=LEFT, padx=10)
        Button(self.frm_toggle, text="Edit Number2", command=lambda: self.set_active("v2")).pack(side=LEFT, padx=10)    
        self.window.mainloop()         
        


    def set_active(self, field_name):
        self.active_input = field_name   
    def append_digit(self, digit):
        if self.active_input == "v1":
            current = self.v1.get()
            self.v1.set(current + str(digit))
        else:
            current = self.v2.get()
            self.v2.set(current + str(digit))

    def clear_all(self):
        self.v1.set("")
        self.v2.set("")
        self.v3.set("")
        self.active_input = "v1"
    def add(self):
        self.v3.set(eval(self.v1.get())+eval(self.v2.get()))
    def subtract(self):
        self.v3.set(eval(self.v1.get())-eval(self.v2.get()))
    def multiply(self):
        self.v3.set(eval(self.v1.get())*eval(self.v2.get()))
    def divide(self):
        self.v3.set(eval(self.v1.get())/eval(self.v2.get()))


MenuDemo()