from tkinter import * 

window = Tk()
window.geometry("500x500")
window.title("Labels")

# Instantiate the label from tkinter
# 1st argument -> The container / window that is going to be holding the label
# 2nd argument -> Options to set for the label, text etc
label = Label(window, text="Hello world!") 
# label.pack() # Display the label on the given window, 1st way to do it. By default places it in the center towards the top
label.place(x=5, y=5) # Second way to place labels, takes inputs as coordinates of where you want to place the label

window.mainloop()