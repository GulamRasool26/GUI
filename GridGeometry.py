from tkinter import*
#creating main form/window/widget
root = Tk()
b = 0
for r in range(5):
    for c in range(5):
        Button(root,text = str(b),borderwidth = 1).grid(row=r,column=c )
        b = b + 1
root.mainloop()