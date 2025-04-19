# GUI
Hey My name is Gulam Rasool
Today is 19th of April and I am going to practice GUI in Python
The Library we are using is #Tkinter to create and Customise Forms 
Following are the Key point and tools We are using: 
    TK() = to create a whole form.
    Frame(form) = to create a separate panel and parameter is the window/form on which frame will created
    pack(side= TOP/BOTTOM/LEFT/RIGHT) = place at specific block of window
    BUTTON(destination,text="..",fg="..",borderwidth=,command=)=to place button on form or frame
    grid(row= , column= ,rowspan= ,columnspan=,padx=,pady=,Sticky=E/W/N/S) = adjust in table like structure using columns and rows
    Label(destination,text="..",fg="..") = to display captions of Textboxes/entry box
    Entry(destination,bd=,textvariable=) = When you want user to enter data it will be in entry box- bd is border
    place(x=,y=) = to place at specific position on the bases of X and Y values
    Menu(destination) = To add Menu in the window
Description of each code:
1. Double Frame:
                In this we Just create 2 separate Frames.
                3 buttons in one frame(TOP) 
                1 in the Second frame(BOTTOM)
                Adjust the Text on the button
                Did all this using pack() geometry organizer
2. Grid Geometry:
                Adjust Buttons using grid() instead of pack() 
                Create a grid of 25 buttons
                input rows and columns not left or right as in pack()
3. Grid Manager Demo:
                Create a form 
                Adjust the positions using grid()
                We use Label()
                We use Entry()
                We adjust padding padx=,pady=
                We use Sticky
                A form we  see somewhere in our daily life
4. Place Geometry
                Creating Simple forms using Place() function
                Using X and Y value to place at specific positon
5. Calculator Menu
                Create a Menu Bar add two option Operation and Exit
                Create separate frames for Buttons
                Create separate frames for Inputs
                Adding Commands for buttons
6. Calculator with Input Buttons
                Create a Calculator
                Add Buttons for input(0-9) 
                Also Add Clear Button
7. Loan Calculator
                Take inputs from the user through entry boxes
                compute the inputs using EMI formula
                display the value using Labels
                
