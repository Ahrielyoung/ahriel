import tkinter as tk
from tkinter import Button as TkButton

def show_text():
    input_user = Entry.get()
    Label.config(text = input_user)
    Entry.delete(0, tk.END)
def color_change():
    Button.config(background= "black")

root = tk.Tk ()
root.title ("Text Output") #the title 

Entry = tk.Entry(root)
Entry.pack()

Label = tk.Label(root, text="Enter Your Thoughts:", background="orange", foreground="white") # the label under where the text is entered 
Label.pack()

Button = tk.Button(root, text="Show Text", command=lambda:[show_text(Button), color_change(Button)], foreground="yellow", activebackground= "green", background= "black") # the button is yellow 
Button.pack()

root.mainloop()

