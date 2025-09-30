import tkinter

window = tkinter.Tk()

window.title("My first GUI Project")
window.minsize(width = 300, height = 400)

mylabel = tkinter.Label(text = "I am a robot", font = ("Arial", 24, "bold"))
mylabel.pack()

mylabel["text"] = "New Text"
mylabel.config(text = "New Text")

def button_clicked():
    print("I got clicked")
    newtext = input.get()
    mylabel.config(text = newtext)

button = tkinter.Button(text = "Click me", command = button_clicked)
button.pack()

input = tkinter.Entry(width = 10)
input.pack()
print(input.get())



window.mainloop()


#########



    