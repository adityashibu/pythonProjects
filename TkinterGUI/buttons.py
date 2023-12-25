from tkinter import * 

window = Tk()
window.title("Buttons")

button = Button(window, 
                text="Click me!",
                )
button.pack()

count = 0

def click():
    print("You clicked the button :P")
    
def counter():
    global count
    count += 1
    print(count)

'''
Tell the button what to do using the command attribute
'''
button1 = Button(window,
                 text="Click me!",
                 command=click)
button1.pack()

'''
Change font size and family using the font attribute
'''
button2 = Button(window,
                 text="Click me",
                 font=("Comic Sans", 30))
button2.pack()

'''
Background and foreground color can be changed using the same commands as before, the bg and fg attributes
'''
button3 = Button(window,
                 text="Click me!",
                 bg="Red",
                 fg="White")
button3.pack()

'''
Change the format of the button when clicked using the activebackground and activebackground attributes
'''
button4 = Button(window,
                 text="Click me!",
                 bg="Red",
                 fg="white",
                 activebackground="White",
                 activeforeground="Red",
                 command=counter)
button4.pack()

'''
To disable interaction with a button use the state attribute, ACTIVE by default
'''
button5 = Button(window,
                 text="Click me!",
                 state=DISABLED)
button5.pack()

'''
As before an image can be added to a button by first converting it to a photoimage and then using the image
attribute of the button to add it to the button, if you want to add text and image to the button then use
the compound attribute to add the image and the text
'''

window.mainloop()