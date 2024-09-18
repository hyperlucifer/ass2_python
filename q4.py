import tkinter as tk
from tkinter import font

# Function to update the label's font style
def update_font():
    font_family = font_var.get()
    font_bold = 'bold' if bold_var.get() else 'normal'
    font_size = size_var.get()
    label.config(font=(font_family, font_size, font_bold))

# Create the main window
root = tk.Tk()
root.title("Change Label Font Style")

# Variables for font settings
font_var = tk.StringVar(value="Arial")
bold_var = tk.IntVar(value=0)
size_var = tk.IntVar(value=12)

# Label to display
label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 12))
label.pack(pady=20)

# Frame for font family selection
font_frame = tk.LabelFrame(root, text="Font Family")
font_frame.pack(padx=10, pady=10)

font_list = ["Arial", "Courier", "Helvetica", "Times"]
for family in font_list:
    tk.Radiobutton(font_frame, text=family, variable=font_var, value=family, command=update_font).pack(anchor="w")

# Check button for Bold option
bold_check = tk.Checkbutton(root, text="Bold", variable=bold_var, command=update_font)
bold_check.pack(pady=10)

# Frame for font size selection
size_frame = tk.LabelFrame(root, text="Font Size")
size_frame.pack(padx=10, pady=10)

size_list = [12, 16, 20, 24]
for size in size_list:
    tk.Radiobutton(size_frame, text=str(size), variable=size_var, value=size, command=update_font).pack(anchor="w")

# Start the GUI event loop
root.mainloop()