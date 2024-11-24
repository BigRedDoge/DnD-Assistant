from tkinter import *

# Callback to toggle visibility
def toggle_frame(frame):
    if frame.winfo_viewable():
        frame.grid_remove()
    else:
        frame.grid()

# Main window setup
root = Tk()
root.title("Collapsible Table Test")
root.geometry("600x400")

# Header for Monsters Section
monsters_header = Frame(root, bg="lightblue")
monsters_header.grid(row=0, column=0, sticky="ew")
Button(monsters_header, text="Monsters ▼", command=lambda: toggle_frame(monsters_body)).pack(fill=X)

# Monsters Body
monsters_body = Frame(root, bg="white")
monsters_body.grid(row=1, column=0, sticky="ew")

# Add column headings for Monsters
Label(monsters_body, text="Initiative", width=15, bg="gray", fg="white").grid(row=0, column=0, sticky="ew")
Label(monsters_body, text="Name", width=15, bg="gray", fg="white").grid(row=0, column=1, sticky="ew")

# Add rows for Players
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

# Location Body
defences_body = Frame(root, bg="white")
defences_body.grid(row=1, column=1, sticky="ew")

# Add column headings for Location
Label(defences_body, text="AC", width=20, bg="gray", fg="white").grid(row=0, column=0, sticky="ew")
Label(defences_body, text="Health", width=20, bg="gray", fg="white").grid(row=0, column=1, sticky="ew")
Label(defences_body, text="Damage Taken", width=20, bg="gray", fg="white").grid(row=0, column=2, sticky="ew")

# Add rows for Location
defences_data = [
    ("Gold", "20/20", "0"),
    ("Bronze", "30/30", "0"),
    ("Silver", "40/40", "0"),
]
for i, (ac, health, damage) in enumerate(defences_data, start=1):
    Label(defences_body, text=ac, width=20).grid(row=i, column=0)
    Label(defences_body, text=health, width=20).grid(row=i, column=1)
    Label(defences_body, text=damage, width=20).grid(row=i, column=2)

root.mainloop()
