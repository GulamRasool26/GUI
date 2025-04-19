from tkinter import *
#Main form/window
window = Tk()
window.title("Gird Manager demo")
message = Message(window,text="This message widget occupies two row and two columns")
message.grid(row = 1,column=1,rowspan=3,columnspan=2)
Label(window,text="First Name",fg="Black").grid(row=1,column=5,rowspan=1,columnspan=3,padx=5,pady=5)
Entry(window).grid(row=1,column=9,padx=5,pady=5)
Label(window,text="Last Name",fg="Black").grid(row=2,column=5,rowspan=1,columnspan=3,padx=5,pady=5)
Entry(window).grid(row=2,column=9,padx=5,pady=5)
Button(window,text="Submit",fg="black").grid(row=3,padx=5,pady=5,column=9,sticky=E)
window.mainloop()
