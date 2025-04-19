from tkinter import*
class InterestCalculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Loan Calculator")
        #Frame for inputs
        self.frm1 = Frame(self.window)
        self.frm1.grid(row=1,column=1)
        L1 = Label(self.frm1,text="Annual Interest Rate: ").grid(row=1,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        E1 = Entry(self.frm1,width=15).grid(row=1,column=4,padx=5,pady=5)
        L2 = Label(self.frm1,text="Number of years: ").grid(row=1,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        E1 = Entry(self.frm1,width=15).grid(row=1,column=4,padx=5,pady=5)
        L1 = Label(self.frm1,text="Annual Interest Rate: ").grid(row=1,column=1,rowspan=1,columnspan=2,padx=5,pady=5)
        E1 = Entry(self.frm1,width=15).grid(row=1,column=4,padx=5,pady=5)
        

       