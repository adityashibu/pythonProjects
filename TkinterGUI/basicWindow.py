from tkinter import * 

'''
Difference between windows and widgets

Widgets: GUI elements such as buttons, textboxes, labels etc
Windows: Container to hold these widgets
'''

window = Tk() # Simple window 
window.geometry("500x500") # For setting size of the window, use the geometry attribute 
window.title("Basic window") # To set the title of the window

icon = PhotoImage(file="TKinterGUI/sun.png") # Create a photoimage from the given photo so it can be used by TKinter for the window icon
window.iconphoto(True, icon) # Set the given icon as the icon of the window
window.config(background="light blue") # Set color for the window

window.mainloop() # To show the window