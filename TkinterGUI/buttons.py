from tkinter import * 

window = Tk()
window.title("Buttons")

button = Button(window, 
                text="Click me!",
                )
button.pack()

def click():
    print("You clicked the button :P")

'''
Tell the button what to do using the command attribute
'''
button1 = Button(window,
                 text="Click me!",
                 command=click)
button1.pack()

window.mainloop()