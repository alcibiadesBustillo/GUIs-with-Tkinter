import tkinter as tk

def open_file():
    pass

def save_file():
    pass

def show():
    method = clicked.get()
    if method == 'NONE':
        print('Select a method')
    elif method == 'Method 1':
        print('method 1')
    elif method == 'Method 2':
        print('method 2')
    elif method == 'Method 3':
        print('method 3')




root = tk.Tk()
root.title('Numerical methods')

root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)

text_edit = tk.Text(root)
frame_buttons = tk.Frame(root)

# Buttons
open_button = tk.Button(frame_buttons, text="Open")
save_button = tk.Button(frame_buttons, text="Save As...")

# Put Buttons in the screen
open_button.grid(row=0, column=0, sticky='ns', padx=5, pady=5)
save_button.grid(row=1, column=0, sticky='ew', padx=5, pady=5)


# Put frame and text edit in the screen
frame_buttons.grid(row=0, column=0, sticky='ns')
text_edit.grid(row=0, column=1, sticky='nsew')

# Dropdown menu
# Create a Tkinter variable
clicked = tk.StringVar(root)

CHOICES = [ 'NONE','Method 1', 'Method 2', 'Method 3']
clicked.set(CHOICES[0])

popup_menu = tk.OptionMenu(frame_buttons, clicked, *CHOICES)
popup_menu.grid(row=2, column=0)

method_button = tk.Button(frame_buttons, text="Go Method", command=show)
method_button.grid(row=3, column=0, sticky='ew', padx=5, pady=5)



root.mainloop()