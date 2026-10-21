import random
import tkinter as tk
from tkinter import messagebox
import time

root = tk.Tk()
root.title("best calculator")
root.geometry("500x300")

num = random.randint(1, 15)
intext = ""
auto_roll = 0

def buy_auto():
    global roll_in
    global auto_roll
    a_roll = messagebox.askyesno("Buy", "Do you wanna buy auto rolling for only 2,99?")
    if a_roll:
        auto_roll = 1
        button_a.config(command=use_auto)
        roll_in = tk.Entry(root, font=("Arial",20), width=6)
        roll_in.grid(row=2, column=2)
    else:
        auto_roll = 0        

def use_auto():
    global search
    global button1
    global num
    global com
    search = roll_in.get()
    search = list(search)
    search = [x for x in search if x != " "]
    for s in range(len(search)):
        num = random.randint(0, 13)
        button1.config(text=f"{num}")
        if search[s] == "1":
            num1()
        elif search[s] == "2":
            num2()
        elif search[s] == "3":
            num3()
        elif search[s] == "4":
            num4()
        elif search[s] == "5":
            num5()
        elif search[s] == "6":
            num6()
        elif search[s] == "7":
            num7()
        elif search[s] == "8":
            num8()
        elif search[s] == "9":
            num9()
        elif search[s] == "0":
            num0()
        elif search[s] == "+":
            num_add()
            button1.config(text="+")
        elif search[s] == "-":
            num_sub()
            button1.config(text="-")
        elif search[s] == "*":
            num_mul()
            button1.config(text="*")
        elif search[s] == "/":
            num_div()
            button1.config(text="/")

def reroll():
    global button1
    global num
    global com
    num = random.randint(0, 13)    
    button1.config(text=f"{num}")
    if num == 1:
        button1.config(command=num1)
    elif num == 2:
        button1.config(command=num2)
    elif num == 3:
        button1.config(command=num3)
    elif num == 4:
        button1.config(command=num4)
    elif num == 5:
        button1.config(command=num5)
    elif num == 6:
        button1.config(command=num6)
    elif num == 7:
        button1.config(command=num7)
    elif num == 8:
        button1.config(command=num8)
    elif num == 9:
        button1.config(command=num9)
    elif num == 0:
        button1.config(command=num0)
    elif num == 10:
        button1.config(command=num_add)
        button1.config(text="+")
    elif num == 11:
        button1.config(command=num_sub)
        button1.config(text="-")
    elif num == 12:
        button1.config(command=num_mul)
        button1.config(text="*")
    elif num == 13:
        button1.config(command=num_div)
        button1.config(text="/")
def num1():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "1"
    display_label.config(text=f"{intext}")
def num2():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "2"
    display_label.config(text=f"{intext}")
def num3():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "3"
    display_label.config(text=f"{intext}")
def num4():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "4"
    display_label.config(text=f"{intext}")
def num5():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "5"
    display_label.config(text=f"{intext}")
def num6():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "6"
    display_label.config(text=f"{intext}")
def num7():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "7"
    display_label.config(text=f"{intext}")
def num8():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "8"
    display_label.config(text=f"{intext}")
def num9():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "9"
    display_label.config(text=f"{intext}")
def num0():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "0"
    display_label.config(text=f"{intext}")
def num_add():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "+"
    display_label.config(text=f"{intext}")
def num_sub():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "-"
    display_label.config(text=f"{intext}")
def num_mul():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "*"
    display_label.config(text=f"{intext}")
def num_div():
    global num
    global display_label
    global intext
    global button1
    intext = intext + "/"
    display_label.config(text=f"{intext}")
def num_ans():
    global num
    global display_label
    global intext
    global button1
    ans_roll = messagebox.askyesno("Buy", "Do you wanna buy the answer for only 20 cents?")
    if ans_roll:
        ans = eval(intext)
        display_label.config(text=f"{ans}")
def num_C():
    global num
    global display_label
    global intext
    global button1
    intext = ""
    display_label.config(text=f" ")
    
display_label = tk.Label(root, text="         ", font=("Arial",30), bg="light grey", fg="black", width=10)
display_label.grid(row=0, column=1, pady=10)

button1 = tk.Button(root, text=f"1", font=("Arial",20), width=5, height=2, command=num1)
button1.grid(row=1, column=0)

button2 = tk.Button(root, text=f"=", font=("Arial",20), width=5, height=2, command=num_ans)
button2.grid(row=2, column=0)

button3 = tk.Button(root, text=f"C", font=("Arial",20), width=5, height=2, command=num_C)
button3.grid(row=2, column=1)

button_r = tk.Button(root, text="Reroll", font=("Arial",20), width=5, height=2, command=reroll)
button_r.grid(row=1, column=1)

button_a = tk.Button(root, text=f"Auto roll", font=("Arial",20), width=6, height=2, command=buy_auto)
button_a.grid(row=1, column=2)

root.mainloop()