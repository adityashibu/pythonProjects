from tkinter import * 

# Create window for adding the labels
window = Tk()
window.geometry("500x500")
window.title("Labels")

# Instantiate the label from tkinter
# 1st argument -> The container / window that is going to be holding the label
# 2nd argument -> Options to set for the label, text etc
label = Label(window, text="Hello world!") 
label.pack() # Display the label on the given window, 1st way to do it. By default places it in the center towards the top
# label.place(x=5, y=5) # Second way to place labels, takes inputs as coordinates of where you want to place the label

'''
Other parameters of label include changing the font of the label, using the font attribute
'''
label2 = Label(window, text="This is a label with a different font", font=('Arial', 20, "bold"))
label2.pack()

'''
Creating a label with a different foreground color using the fg attribute
'''
label3 = Label(window, text="Different foreground", fg="green")
label3.pack()

'''
Creating a label with a different background color using the bg attribute
'''
label4 = Label(window, text="Different background", bg="green", fg="white")
label4.pack()

'''
Adding border to the text using the relief attribute, increase depth using bd attribute
'''
label5 = Label(window, text="Text with a border", relief=RAISED, bd=10)
label5.pack()

'''
Adding padding to the text using padx and pady attributes
'''
label6 = Label(window, 
               text="Text with padding", 
               relief=RAISED, 
               bd=10, 
               padx=10,
               pady=10)
label6.pack()

window.mainloop()