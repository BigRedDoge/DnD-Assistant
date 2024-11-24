from tkinter import *

root = Tk()

#adds title to window
root.title("guiTest")
#changes defult size of window
root.geometry("800x500")

#create label
myLabel = Label(root, text="Hello world", font=('Arial', 48))
#adds label to window
myLabel.pack(padx=20, pady=20)

#creates textbox
textbox = Text(root, height=3, width=12, font=('Arial', 12))
#adds textbox to window
textbox.pack(padx=20, pady=20)

button = Button(root, text="click me", font=('Ariel', 12))
button.pack(padx=20, pady=20)

root.mainloop()