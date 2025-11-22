from tkinter import *

window = Tk()
window.geometry('300x400')
window.title("Calculator")

e = Entry(window, width=35, borderwidth=5)
e.place(x=40, y=20)

f_num = 0
math_op = ""

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

def button_clear():
    e.delete(0, END)

def add():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def sub():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def mul():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def div():
    first_number = e.get()
    global f_num
    global math_op
    math_op = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math_op == "addition":
        e.insert(0, f_num + float(second_number))
    elif math_op == "subtraction":
        e.insert(0, f_num - float(second_number))
    elif math_op == "multiplication":
        e.insert(0, f_num * float(second_number))
    elif math_op == "division":
        try:
            e.insert(0, f_num / float(second_number))
        except ZeroDivisionError:
            e.insert(0, "Error")

b7 = Button(window, text='7', width=5, height=2, command=lambda: button_click(7))
b7.place(x=40, y=60)

b8 = Button(window, text='8', width=5, height=2, command=lambda: button_click(8))
b8.place(x=100, y=60)

b9 = Button(window, text='9', width=5, height=2, command=lambda: button_click(9))
b9.place(x=160, y=60)

b4 = Button(window, text='4', width=5, height=2, command=lambda: button_click(4))
b4.place(x=40, y=120)

b5 = Button(window, text='5', width=5, height=2, command=lambda: button_click(5))
b5.place(x=100, y=120)

b6 = Button(window, text='6', width=5, height=2, command=lambda: button_click(6))
b6.place(x=160, y=120)

b1 = Button(window, text='1', width=5, height=2, command=lambda: button_click(1))
b1.place(x=40, y=180)

b2 = Button(window, text='2', width=5, height=2, command=lambda: button_click(2))
b2.place(x=100, y=180)

b3 = Button(window, text='3', width=5, height=2, command=lambda: button_click(3))
b3.place(x=160, y=180)

b0 = Button(window, text='0', width=5, height=2, command=lambda: button_click(0))
b0.place(x=40, y=240)

b_add = Button(window, text='+', width=5, height=2, command=add)
b_add.place(x=100, y=240)

b_sub = Button(window, text='-', width=5, height=2, command=sub)
b_sub.place(x=160, y=240)

b_mul = Button(window, text='*', width=5, height=2, command=mul)
b_mul.place(x=220, y=60)

b_div = Button(window, text='/', width=5, height=2, command=div)
b_div.place(x=220, y=120)

b_equal = Button(window, text='=', width=5, height=5, command=button_equal)
b_equal.place(x=220, y=180)

b_clear = Button(window, text='Clear', width=25, height=2, command=button_clear)
b_clear.place(x=40, y=300)

window.mainloop()


