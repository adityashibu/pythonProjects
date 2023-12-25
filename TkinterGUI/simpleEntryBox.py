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
    name = entry.get()
    print(f"Hello, {name}")
    
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

window.mainloop()