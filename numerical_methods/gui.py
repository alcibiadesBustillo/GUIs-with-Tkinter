import tkinter as tk
from tkinter import font as tkfont
from bisection.bisection import bisection
from fix_point.fix_point import fix_point

class NumericlaApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, BisectionMethod, FixPointMethod):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.grid(row=0, column=0)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        # button2 = tk.Button(self, text="Go to Page Two",
        #                     command=lambda: controller.show_frame("PageTwo"))
        button1.grid(row=2, column=0)
        # button2.grid(row=2, column=1)


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Numerical Methods", font=controller.title_font)
        label.grid(row=0, column=1)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.grid(row=1, column=0)

        frame_buttons = tk.Frame(self)
        frame_buttons.grid(row=2, column=0, sticky='ns')

        # Dropdown menu
        # Create a Tkinter variable
        self.clicked = tk.StringVar(self)

        CHOICES = [ 'NONE','Bisection Method', 'Fix Point Method', 'Method 3']
        self.clicked.set(CHOICES[0])

        popup_menu = tk.OptionMenu(frame_buttons, self.clicked, *CHOICES)
        popup_menu.grid(row=3, column=0)

        method_button = tk.Button(frame_buttons, text="Go Method", command=self.go_method)
        method_button.grid(row=4, column=0)
    
    def go_method(self):
        
        method = self.clicked.get()
        if method == 'NONE':
            print('Select a method')            
        elif method == 'Bisection Method':
            self.controller.show_frame('BisectionMethod')
        elif method == 'Fix Point Method':
            self.controller.show_frame('FixPointMethod')
        elif method == 'Method 3':
            print('method 3')


class BisectionMethod(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Bisection Method", font=controller.title_font)
        label.grid(row=0, column=1)

        # Left frame
        left_frame = tk.Frame(self, width=200, height= 400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        # right frame
        right_frame = tk.Frame(self, width=450, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # All left frame
        title = tk.Label(left_frame, text="Bisection Method", relief=tk.RAISED)
        title.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

        #Button(tool_bar, text="Select", command=clicked)
        #grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')


        # # labels
        label_function = tk.Label(left_frame, text="Function")
        label_function.grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')
        
        label_lowerLimit = tk.Label(left_frame, text="Lower Limit")
        label_lowerLimit.grid(row=2, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        label_upperLimit = tk.Label(left_frame, text="Upper limit")
        label_upperLimit.grid(row=3, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        label_tolerance = tk.Label(left_frame, text="Tolerance")
        label_tolerance.grid(row=4, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        label_iterations = tk.Label(left_frame, text="Iterations")
        label_iterations.grid(row=5, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        # # Entries
        self.function = tk.Entry(left_frame, width=30)
        self.function.grid(row=1, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.lower_limit = tk.Entry(left_frame, width=30)
        self.lower_limit.grid(row=2, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.upper_limit = tk.Entry(left_frame, width=30)
        self.upper_limit.grid(row=3, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.tolerance = tk.Entry(left_frame, width=30)
        self.tolerance.grid(row=4, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.iteration = tk.Entry(left_frame, width=30)
        self.iteration.grid(row=5, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')               
        
        button_compute = tk.Button(left_frame, text="Compute",
                            command=self.compute, bg="yellow", fg="red")
        button_compute.grid(row=6, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        
        button = tk.Button(left_frame, text="Go to the start page",
                            command=lambda: controller.show_frame("PageOne"))
        button.grid(row=6, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        
        # text
             
        self.text_edit = tk.Text(right_frame)
        self.text_edit.grid(row=0, column=0, sticky='nsew')
    
    def compute(self):
        print('computando....')
        try:
            f = self.function.get()
            a = self.lower_limit.get()
            b = self.upper_limit.get()
            tol = self.tolerance.get()
            n = self.iteration.get()            
            
            p, table, p_x, f_x = bisection(f, float(a), float(b), float(tol), int(n))
            
            if p != None:
                self.text_edit.delete("1.0", tk.END)
                self.text_edit.insert(tk.END, table)
            else:
                self.text_edit.delete("1.0", tk.END)
                self.text_edit.insert(tk.END, "The method fail")

            # self.function.delete(0, tk.END)
            # self.lower_limit.delete(0, tk.END)
            # self.upper_limit.delete(0, tk.END)
            # self.tolerance.delete(0, tk.END)
            # self.iteration.delete(0, tk.END)

            print(table)
        except Exception as e:
            self.text_edit.delete("1.0", tk.END)
            self.text_edit.insert(tk.END, e)
        

class FixPointMethod(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Fix Point Method", font=controller.title_font)
        label.grid(row=0, column=1)

        # Left frame
        left_frame = tk.Frame(self, width=200, height= 400, bg='grey')
        left_frame.grid(row=0, column=0, padx=10, pady=5)

        # right frame
        right_frame = tk.Frame(self, width=450, height=400, bg='grey')
        right_frame.grid(row=0, column=1, padx=10, pady=5)

        # All left frame
        title = tk.Label(left_frame, text="Fix Point Method", relief=tk.RAISED)
        title.grid(row=0, column=0, padx=5, pady=5, columnspan=2)

       
        # # labels
        label_function = tk.Label(left_frame, text="Function:")
        label_function.grid(row=1, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')        

        label_initialApx = tk.Label(left_frame, text="Initial Aproximation po:")
        label_initialApx.grid(row=2, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        label_tolerance = tk.Label(left_frame, text="Tolerance:")
        label_tolerance.grid(row=3, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        label_iterations = tk.Label(left_frame, text="Iterations:")
        label_iterations.grid(row=4, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        # # Entries
        self.function = tk.Entry(left_frame, width=30)
        self.function.grid(row=1, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.initialApx = tk.Entry(left_frame, width=30)
        self.initialApx.grid(row=2, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')       

        self.tolerance = tk.Entry(left_frame, width=30)
        self.tolerance.grid(row=3, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        self.iteration = tk.Entry(left_frame, width=30)
        self.iteration.grid(row=4, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')               
        
        button_compute = tk.Button(left_frame, text="Compute",
                            command=self.compute, bg="yellow", fg="red")
        button_compute.grid(row=5, column=1, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        
        button = tk.Button(left_frame, text="Go to the start page",
                            command=lambda: controller.show_frame("PageOne"))
        button.grid(row=5, column=0, padx=5, pady=5, sticky='w'+'e'+'n'+'s')

        
        # text
             
        self.text_edit = tk.Text(right_frame)
        self.text_edit.grid(row=0, column=0, sticky='nsew')
    
    def compute(self):
        print('computando....')
        try:
            f = self.function.get()
            po = self.initialApx.get()           
            tol = self.tolerance.get()
            n = self.iteration.get()            
            
            p, table = fix_point(f, float(po), float(tol), int(n))
            
            if p != None:
                self.text_edit.delete("1.0", tk.END)
                self.text_edit.insert(tk.END, table)
            else:
                self.text_edit.delete("1.0", tk.END)
                self.text_edit.insert(tk.END, "The method fail")

            # self.function.delete(0, tk.END)
            # self.lower_limit.delete(0, tk.END)
            # self.upper_limit.delete(0, tk.END)
            # self.tolerance.delete(0, tk.END)
            # self.iteration.delete(0, tk.END)

            print(table)
        except Exception as e:
            self.text_edit.delete("1.0", tk.END)
            self.text_edit.insert(tk.END, e)
        


class Template(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to Bisection Method", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("PageOne"))
        button.pack()


if __name__ == "__main__":
    app = NumericlaApp()
    app.title('Numerical App') 
    app.geometry('1200x500')
    #app.rowconfigure(0, minsize=800, weight=1)
    #app.columnconfigure(1, minsize=800, weight=1)
    app.mainloop()