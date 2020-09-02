from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

import os

current_directory = os.getcwd()

def open_file():
    """Openfile for editing
    """
    filepath = askopenfilename(
        initialdir = current_directory,
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_edit.delete("1.0",END)
    with open(filepath, 'r') as input_file:
        text = input_file.read()
        text_edit.insert(END, text)
    root.title(f'Cipher Cesar - {filepath}')

def save_file():
    """Save the current file as a new file
    """
    filepath = asksaveasfilename(
        defaultextension="txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get("1.0", END)
        output_file.write(text)
    root.title(f"Simple Text Editor - {filepath}")



root = Tk()
root.title('Cipher Cesar')

root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

text_edit = Text(root)
frame_buttons = Frame(root)

# Buttons
open_button = Button(frame_buttons, text="Open", command=open_file)
save_button = Button(frame_buttons, text="Save As...", command=save_file)

# Put Buttons in the screen
open_button.grid(row=0, column=0, sticky='ns', padx=5, pady=5)
save_button.grid(row=1, column=0, sticky='ew', padx=5)

# Put frame and text edit in the screen
frame_buttons.grid(row=0, column=0, sticky='ns')
text_edit.grid(row=0, column=1, sticky='nsew')



root.mainloop()