from tkinter import*
#Top Frame 
root = Tk()
top = Frame(root)
top.pack() #Default on Top
#Bottom Frame
bottom = Frame(root)
bottom.pack(side=BOTTOM)
btn1 = Button(top,text="Red",fg="red").pack(side= LEFT)
btn2 = Button(top,text="Green",fg="green").pack(side= LEFT)
btn3 = Button(top,text="blue",fg="blue").pack(side=LEFT)
btn4 = Button(bottom,text="Black",fg="Black").pack(side=LEFT)
root.mainloop()