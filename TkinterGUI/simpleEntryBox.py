from tkinter import *

window = Tk()
window.title("Entry box")

entry = Entry(window, 
              font=("Courier", 50),
              bg="black",
              fg="#00ff00")
entry.pack(side=LEFT)

# Submit function
def submit():
    while True:
        name = entry.get()
        if name == "":
            print("Error, enter a valid name")
        else:
            print(f"Hello, {name}")
            break
        break
    
# Submit button
submitBtn = Button(window,
                   text="Submit",
                   command=submit)
submitBtn.pack(side=RIGHT)

# Delete function
def delete():
    entry.delete(0,END)

# Delete button
deleteBtn = Button(window, 
                   text="Delete",
                   command=delete)
deleteBtn.pack(side=LEFT)

# Backspace function 
def backspace():
    entry.delete(len(entry.get()) - 1, END)
    
backSpaceBtn = Button(window,
                      text="BackSpace",
                      command=backspace)
backSpaceBtn.pack(side=RIGHT)

window.mainloop()