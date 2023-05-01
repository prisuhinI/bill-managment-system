from tkinter import *


root = Tk()
root.geometry('1000x500')
root.title('Bill Management')
root.resizable(False, False)


def reset():
    entry_dosa.delete(0, END)
    entry_cookies.delete(0, END)
    entry_tea.delete(0, END)
    entry_coffee.delete(0, END)
    entry_juice.delete(0, END)
    entry_pancakes.delete(0, END)
    entry_eggs.delete(0, END)


def total():
    try: a1 = int(dosa.get())
    except: a1 = 0

    try: a2 = int(cookies.get())
    except: a2 = 0

    try: a3 = int(tea.get())
    except: a3 = 0

    try: a4 = int(coffee.get())
    except: a4 = 0

    try: a5 = int(juice.get())
    except: a5 = 0

    try: a6 = int(pancakes.get())
    except: a6 = 0

    try: a7 = int(eggs.get())
    except: a7 = 0

    # Define cost of each item per quantity
    c1 = 60 * a1
    c2 = 30 * a2
    c3 = 7 * a3
    c4 = 100 * a4
    c5 = 20 * a5
    c6 = 15 * a6
    c7 = 7 * a7

    lbl_total = Label(f2, font=('arial', 20, 'bold'), text='Total', width=25, fg='lightyellow', bg='black')
    lbl_total.place(x=0, y=50)

    entry_total = Entry(f2, font=('arial', 20, 'bold'), textvariable=total_bill, bd=6, width=15, bg='lightgreen')
    entry_total.place(x=50, y=100)

    total_cost = c1 + c2 + c3 + c4 + c5 + c6 + c7
    string_bill = "Rs.", str('%.2f' % total_cost)
    total_bill.set(string_bill)


Label(text='Bill Management', bg='black', fg='white', font=('calibri', 33), width='300', height='2').pack()


# Menu card

f = Frame(root, bg='lightgreen', highlightbackground='black', highlightthickness=1, width=300, height=400)
f.place(x=10, y=90)

Label(f, text='Menu', font=('Gabriola', 40, 'bold'), fg='black', bg='lightgreen').place(x=80, y=10)

Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Dosa.......Rs.60/plate', fg='black', bg='lightgreen').place(x=10, y=80)
Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Cookies.......Rs.30/plate', fg='black', bg='lightgreen').place(x=10, y=115)
Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Tea.......Rs.7/cup', fg='black', bg='lightgreen').place(x=10, y=150)
Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Coffee.......Rs.10/cup', fg='black', bg='lightgreen').place(x=10, y=185)
Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Juice.......Rs.20/glass', fg='black', bg='lightgreen').place(x=10, y=220)
Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Pancakes.......Rs.15/pack', fg='black', bg='lightgreen').place(x=10, y=255)
Label(f, font=('Lucida Calligraphy', 20, 'bold'), text='Eggs.......Rs.7/egg', fg='black', bg='lightgreen').place(x=10, y=290)

# Bill
f2 = Frame(root, bg='lightyellow', highlightbackground='black', highlightthickness=1, width=300, height=400)
f2.place(x=690, y=90)

bill = Label(f2, text='Bill', font=('calibri', 20), bg='lightyellow')
bill.place(x=130, y=10)

# Entry Work
f1 = Frame(root, bd=5, height=100, width=300, relief=RAISED)
f1.pack()

dosa = StringVar()
cookies = StringVar()
tea = StringVar()
coffee = StringVar()
juice = StringVar()
pancakes = StringVar()
eggs = StringVar()
total_bill = StringVar()

# Label
lbl_dosa = Label(f1, font=('aria', 20, 'bold'), text='Dosa', width=14, fg='blue4')
lbl_cookies = Label(f1, font=('aria', 20, 'bold'), text='Cookies', width=12, fg='blue4')
lbl_tea = Label(f1, font=('aria', 20, 'bold'), text='Tea', width=12, fg='blue4')
lbl_coffee = Label(f1, font=('aria', 20, 'bold'), text='Coffee', width=12, fg='blue4')
lbl_juice = Label(f1, font=('aria', 20, 'bold'), text='Juice', width=12, fg='blue4')
lbl_pancake = Label(f1, font=('aria', 20, 'bold'), text='Pancakes', width=12, fg='blue4')
lbl_eggs = Label(f1, font=('aria', 20, 'bold'), text='Eggs', width=12, fg='blue4')

lbl_dosa.grid(row=1, column=0)
lbl_cookies.grid(row=2, column=0)
lbl_tea.grid(row=3, column=0)
lbl_coffee.grid(row=4, column=0)
lbl_juice.grid(row=5, column=0)
lbl_pancake.grid(row=6, column=0)
lbl_eggs.grid(row=7, column=0)

# Entry
entry_dosa = Entry(f1, font=('arial', 20, 'bold'), textvariable=dosa, bd=6, width=8, bg='lightpink')
entry_cookies = Entry(f1, font=('arial', 20, 'bold'), textvariable=cookies, bd=6, width=8, bg='lightpink')
entry_tea = Entry(f1, font=('arial', 20, 'bold'), textvariable=tea, bd=6, width=8, bg='lightpink')
entry_coffee = Entry(f1, font=('arial', 20, 'bold'), textvariable=coffee, bd=6, width=8, bg='lightpink')
entry_juice = Entry(f1, font=('arial', 20, 'bold'), textvariable=juice, bd=6, width=8, bg='lightpink')
entry_pancakes = Entry(f1, font=('arial', 20, 'bold'), textvariable=pancakes, bd=6, width=8, bg='lightpink')
entry_eggs = Entry(f1, font=('arial', 20, 'bold'), textvariable=eggs, bd=6, width=8, bg='lightpink')

entry_dosa.grid(row=1, column=1)
entry_cookies.grid(row=2, column=1)
entry_tea.grid(row=3, column=1)
entry_coffee.grid(row=4, column=1)
entry_juice.grid(row=5, column=1)
entry_pancakes.grid(row=6, column=1)
entry_eggs.grid(row=7, column=1)

# Buttons

btn_reset = Button(f1, bd=5, fg='black', bg='lightblue', font=('ariel', 16, 'bold'), width=10, text='Reset', command=reset)
btn_reset.grid(row=8, column=0)

btn_total = Button(f1, bd=5, fg='black', bg='lightblue', font=('arial', 16, 'bold'), width=10, text='Total', command=total)
btn_total.grid(row=8, column=1)

root.mainloop()