from tkinter import *

def button_clicked():
    print("I got clicked")
    new_text = user_input.get()
    my_label.config(text=new_text)

window = Tk()
window.title("GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Label
my_label = Label(text="I am a Label", font=("Ariel", 24, "bold"))
#my_label["text"] = "New text"
my_label.config(text="New Text")
# my_label.pack(side="left")    Pack
# my_label.place(x=100, y=200)   Place
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# Button
button1 = Button(text="Click Me", command=button_clicked)
# button.pack()
button1.grid(column=2, row=0)

button2 = Button(text="Smash Me", command=button_clicked)
# button.pack()
button2.grid(column=1, row=1)

# Entry
user_input = Entry(width=10)
# user_input.pack()
user_input.grid(column=4, row=3)

# Can't mix up pack and grid

window.mainloop()


