import tkinter as tk
from tkinter import ttk
from tkinter import *
import random

rollSum = 0

def d20():
    global rollSum
    roll = random.randint(1, 20)
    print("d20 > ",roll)
    rollSum += roll

    rollText = Label(frame2, text=random.randint(1, 20))
    rollText.pack()

# root window
root = tk.Tk()
root.geometry('400x300')
root.title('Notebook Demo')

# create a notebook
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=500, height=380)
frame2 = ttk.Frame(notebook, width=500, height=380)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

# frame1
notebook.add(frame1, text='Info')

infoText = Label(frame1, text="Click over to the Rolling tab to\n generate random numbers between 1 and 20.")
infoText.pack()

# frame2
notebook.add(frame2, text='Rolling')

rollButton = Button(frame2, text="ROLL", command=d20)
rollButton.pack()


root.mainloop()
