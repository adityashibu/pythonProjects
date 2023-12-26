from tkinter import *

window = Tk()
window.title("Checkboxes")

x = IntVar()

def display():
    if (x.get() == 1):
        print("Hurray you clicked on the checkbox :)")
    else:
        print("You clicked off the checkbox :(")

checkBtn = Checkbutton(window, 
                       text="This is a checkbox",
                       variable=x, 
                       onvalue=1,
                       offvalue=0,
                       command=display, 
                       font=("Arial", 20), 
                       fg="#00ff00",
                       bg="black",
                       activebackground="black",
                       activeforeground="#00ff00",
                       padx = 10,
                       pady = 10)
checkBtn.pack()

window.mainloop()