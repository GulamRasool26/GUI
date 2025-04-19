from tkinter import*
class InterestCalculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Loan Calculator")
        #Frame for inputs
        self.frm1 = Frame(self.window)
        self.frm1.grid(row=1,column=1)
        L1 = Label(self.frm1,text="Annual Interest Rate: ").grid(row=1,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        self.rate = StringVar()
        E1 = Entry(self.frm1,width=15,textvariable=self.rate).grid(row=1,column=4,padx=5,pady=5)
        L2 = Label(self.frm1,text="Number of years: ").grid(row=2,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        self.years = StringVar()
        E1 = Entry(self.frm1,width=15,textvariable=self.years).grid(row=2,column=4,padx=5,pady=5)
        L1 = Label(self.frm1,text="Loan Amount: ").grid(row=3,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        self.Lamount = StringVar()
        E1 = Entry(self.frm1,width=15,textvariable=self.Lamount).grid(row=3,column=4,padx=5,pady=5)
        L1 = Label(self.frm1,text="Monthly Payment: ").grid(row=4,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        L1 = Label(self.frm1,text="Total Payment: ").grid(row=5,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        btn = Button(self.frm1,text="Compute Payment: ",width=15 ,fg="Red",command=self.compute).grid(row=6,column=4,padx=5,pady=5,sticky=E)
        
        
        self.window.mainloop()
    def compute(self):
        self.n = int(self.years.get()) * 12
        self.r = float(self.rate.get()) /100 / 12
        self.P = float(self.Lamount.get()) 
        self.monthly = self.P * (self.r * ( (1+self.r) ** self.n) ) / ( ( (1+self.r) ** self.n ) - 1)
        self.payment  =self.monthly * self.n
        L1 = Label(self.frm1,text=str(self.monthly)).grid(row=4,column=3,rowspan=1,columnspan=2,padx=5,pady=5)
        L1 = Label(self.frm1,text=self.payment).grid(row=5,column=3,rowspan=1,columnspan=2,padx=5,pady=5)
        

        return
InterestCalculator()
       