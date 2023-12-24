import PyPDF2
import tkinter as tk
from tkinter import filedialog
import os

def merge_pdfs(file1, file2, output_file):
    merger = PyPDF2.PdfMerger()
    merger.append(file1)
    merger.append(file2)
    merger.write(output_file)
    merger.close()

def select_pdf_file(entry_var):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    entry_var.set(file_path)

def merge_files():
    file1 = entry1.get()
    file2 = entry2.get()

    if file1 and file2:
        output_file = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        merge_pdfs(file1, file2, output_file)
        result_label.config(text="Merge successful.")
    else:
        result_label.config(text="Please select two PDF files.")

# Create the main window
root = tk.Tk()
root.title("PDF Merger")
root.geometry("300x260")

# Create and place widgets
entry1_var = tk.StringVar()
entry2_var = tk.StringVar()

label1 = tk.Label(root, text="Select PDF file 1:")
entry1 = tk.Entry(root, textvariable=entry1_var, state="readonly")
button1 = tk.Button(root, text="Browse", command=lambda: select_pdf_file(entry1_var))

label2 = tk.Label(root, text="Select PDF file 2:")
entry2 = tk.Entry(root, textvariable=entry2_var, state="readonly")
button2 = tk.Button(root, text="Browse", command=lambda: select_pdf_file(entry2_var))

merge_button = tk.Button(root, text="Merge PDFs", command=merge_files)
result_label = tk.Label(root, text="")

label1.pack(pady=5)
entry1.pack(pady=5)
button1.pack(pady=5)

label2.pack(pady=5)
entry2.pack(pady=5)
button2.pack(pady=5)

merge_button.pack(pady=10)
result_label.pack()

# Run the GUI
root.mainloop()
