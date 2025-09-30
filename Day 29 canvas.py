from tkinter import *


window = Tk()
window.title("Password Manager")

label = PhotoImage(file = "c:\Users\pganesan\Documents\Kinaxis Docs\Gen AI\logo.png")


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=label)