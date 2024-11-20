import tkinter as tk
from tkinter import *

class myGUI:
    def __init__(self):
        self.root = tk.TK()

        #create label
        self.myLabel = Label(root, text="Hello world", font=('Arial', 48))
        #adds label to window
        self.myLabel.pack(padx=20, pady=20)


        self.root.mainloop()
