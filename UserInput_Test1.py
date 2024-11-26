from tkinter import *
import random

# Function to toggle visibility
def toggle_frame(frame):
    if frame.winfo_viewable():
        frame.grid_remove()
    else:
        frame.grid()

# Main window setup
root = Tk()
root.title("DnD Assistant")
root.geometry("1100x300")

# Header for Monsters Section
monsters_header = Frame(root, bg="lightblue")
monsters_header.grid(row=0, column=0, sticky="ew")
Button(monsters_header, text="Monsters ▼", command=lambda: toggle_frame(monsters_body)).pack(fill=X)

# Monsters Body, I don't know why there's a white space between the headings and data rows
monsters_body = Frame(root, bg="white")
monsters_body.grid(row=1, column=0, sticky="ew")

# Add column headings for Monsters
Label(monsters_body, text="Initiative", width=15, bg="gray", fg="white").grid(row=0, column=0, sticky="ew")
Label(monsters_body, text="Name", width=15, bg="gray", fg="white").grid(row=0, column=1, sticky="ew")

# Add rows for Monsters
monsters_data = [
    ("1", "Ninja"),
    ("2", "Goblin"),
]
for i, (name, init) in enumerate(monsters_data, start=1):
    Label(monsters_body, text=name, width=15).grid(row=i, column=0)
    Label(monsters_body, text=init, width=15).grid(row=i, column=1)

# Header for Defences Section
defences_header = Frame(root, bg="lightgreen")
defences_header.grid(row=0, column=1, sticky="ew")
Button(defences_header, text="Defences ▼", command=lambda: toggle_frame(defences_body)).pack(fill=X)

# Defences Body
defences_body = Frame(root, bg="white")
defences_body.grid(row=1, column=1, sticky="ew")

# Add column headings for Defences
Label(defences_body, text="AC", width=20, bg="gray", fg="white").grid(row=0, column=0, sticky="ew")
Label(defences_body, text="Health", width=20, bg="gray", fg="white").grid(row=0, column=1, sticky="ew")
Label(defences_body, text="Damage Taken", width=20, bg="gray", fg="white").grid(row=0, column=2, sticky="ew")

# Add rows for Defences
defences_data = [
    ("Gold", "20/20", "0"),
    ("Bronze", "30/30", "0"),
    ("Silver", "40/40", "0"),
]
for i, (ac, health, damage_taken) in enumerate(defences_data, start=1):
    Label(defences_body, text=ac, width=20).grid(row=i, column=0)
    Label(defences_body, text=health, width=20).grid(row=i, column=1)
    Label(defences_body, text=damage_taken, width=20).grid(row=i, column=2)


# d20 roll function (wanted to use this to test Attack Button, which DOES NOT WORK)
def d20():
    global rollSum
    roll = random.randint(1, 20)
    print("d20 > ",roll)
    rollSum += roll

    window = Toplevel(root)
    window.title("Random Number Between 1 and 20:")
    text = Label(window, text=random.randint(1, 20))
    text.pack()


# Header for Attacks Section
attacks_header = Frame(root, bg="red")
attacks_header.grid(row=0, column=2, sticky="ew")
Button(attacks_header, text="Attacks ▼", command=lambda: toggle_frame(attacks_body)).pack(fill=X)

# Attacks Body
attacks_body = Frame(root, bg="white")
attacks_body.grid(row=1, column=2, sticky="ew")

# Creating the ATTACK Button, NOT WORKING
attack_button = Button(attacks_body, text="ATTACK", command=d20),

# Add column headings for Attacks
Label(attacks_body, text="Attack Mod.", width=20, bg="gray", fg="white").grid(row=0, column=0, sticky="ew")
Label(attacks_body, text="Damage", width=20, bg="gray", fg="white").grid(row=0, column=1, sticky="ew")
Label(attacks_body, text="ATTACK", width=20, bg="gray", fg="white").grid(row=0, column=2, sticky="ew")

# Add rows for Attacks
attacks_data = [
    ("+[7]", "[2]d[8]+[3]", attack_button),
    ("+[9]", "[2]d[7]+[1]", attack_button),
    ("+[1]", "[2]d[5]+[2]", attack_button),
]
for i, (attack_mod, damage, attack) in enumerate(attacks_data, start=1):
    Label(attacks_body, text=attack_mod, width=20).grid(row=i, column=0)
    Label(attacks_body, text=damage, width=20).grid(row=i, column=1)
    Label(attacks_body, text=attack, width=20).grid(row=i, column=2)

# Attempt at user input
tkWindow = Tk()  
entry = Entry(tkWindow)
entry.get()

from functools import partial

def printDetails(usernameEntry) :
    usernameText = usernameEntry.get()
    print("user entered :", usernameText)
    return

usernameLabel = Label(tkWindow, text="Enter your name")

usernameEntry = Entry(tkWindow)

printDetailsCallable = partial(printDetails, usernameEntry)

submitButton = Button(tkWindow, text="Submit", command=printDetailsCallable)

usernameLabel.grid(row=0, column=0)
usernameEntry.grid(row=0, column=1) 
submitButton.grid(row=1, column=1)  

root.mainloop()
