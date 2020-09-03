from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import cesar as cs
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
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_edit.get("1.0", END)
        output_file.write(text)
    root.title(f"Simple Text Editor - {filepath}")


def encrypt():
    text = text_edit.get("1.0", END)    
    if entry.get():
        try:
            key = int(entry.get())
            print(f'Correct is a number {key}')
            if key >= 0 and key <= 26:
                print('Correct the key is between 0 and 26')        

                #check the text is not blank or None
                if text and text.strip():
                    text = " ".join(text.split())
                    text2 = cs.encryption(text, key)
                    text_edit.delete("1.0", END)
                    text_edit.insert(END, text2)
                else:
                    print('Es empty')
                #print(type(text)) 
            else:
                print('Incorrect the key is not between 0 and 26')
        except ValueError:
            print('Is not a number')
    else:
        print('Insert the key')
    
    


def decrypt():
    text = text_edit.get("1.0", END)    
    if entry.get():
        try:
            key = int(entry.get())
            print(f'Correct is a number {key}')
            if key >= 0 and key <= 26:
                print('Correct the key is between 0 and 26')        

                #check the text is not blank or None
                if text and text.strip():
                    text = " ".join(text.split())
                    text2 = cs.decryption(text, key)
                    text_edit.delete("1.0", END)
                    text_edit.insert(END, text2)
                else:
                    print('Es empty')
                #print(type(text)) 
            else:
                print('Incorrect the key is not between 0 and 26')
        except ValueError:
            print('Is not a number')
    else:
        print('Insert the key')
    
    



root = Tk()
root.title('Cipher Cesar')

root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

text_edit = Text(root)
frame_buttons = Frame(root)

# Buttons
open_button = Button(frame_buttons, text="Open", command=open_file)
save_button = Button(frame_buttons, text="Save As...", command=save_file)

encrypt_button = Button(frame_buttons, text="Encrypt", command=encrypt)
decrypt_button = Button(frame_buttons, text="Decrypt", command=decrypt)


# Put Buttons in the screen
open_button.grid(row=0, column=0, sticky='ns', padx=5, pady=5)
save_button.grid(row=1, column=0, sticky='ew', padx=5, pady=5)

encrypt_button.grid(row=3, column=0, sticky='ns', padx=5, pady=5)
decrypt_button.grid(row=4, column=0, sticky='ew', padx=5)

# Entry
entry = Entry(frame_buttons, width=10, borderwidth=5)
entry.grid(row=2, column=0, columnspan=4, padx=10,  pady=10)


# Put frame and text edit in the screen
frame_buttons.grid(row=0, column=0, sticky='ns')
text_edit.grid(row=0, column=1, sticky='nsew')



root.mainloop()