"""def add(*args):
    summ = 0
    for n in args:
        summ += n
    print(summ)


add(2, 6, 7, 8, 9)"""
from tkinter import *

window = Tk()
window.title("Wassup my nigs")
window.minsize(width=500, height=300)

my_label = Label(text="IM a Label nigs")


my_label.config(text="new name nigs")
my_label.grid(column=0, row=0)     

def button_click():
    new_text = inputt.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_click)
button.grid(column=1, row=1)


def new_button():
    print("hello")


new_button = Button(text="Don't Click me", command=new_button)
new_button.grid(column=3, row=0)

inputt = Entry(width=10)
inputt.grid(column=4, row=4)
print(inputt.get())

window.mainloop()
