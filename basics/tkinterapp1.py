from tkinter import *


def convert():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)
    grams = float(e2_val.get()) * 1000
    grams = str(grams) + " grams"
    t1.insert(END, grams)
    ounces = round(float(e2_val.get()) * 35.274, 5)
    ounces = str(ounces) + " ounces"
    t2.insert(END, ounces)
    pounds = round(float(e2_val.get()) * 2.20462, 5)
    pounds = str(pounds) + " pounds"
    t3.insert(END, pounds)


def deletethis():
    t1.delete('1.0', END)
    t2.delete('1.0', END)
    t3.delete('1.0', END)


window = Tk()
e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)
e2_val = StringVar()
e2 = Entry(window, textvariable=e2_val)
e2.grid(row=0, column=1)
b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=2)
b2 = Button(window, text="Delete", command=deletethis)
b2.grid(row=0, column=3)
t1 = Text(window, height=1, width=20)
t1.grid(row=1, column=0)
t2 = Text(window, height=1, width=20)
t2.grid(row=1, column=1)
t3 = Text(window, height=1, width=20)
t3.grid(row=1, column=2)
window.mainloop()
