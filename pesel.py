import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

date = ''


def dob_from_pesel():
    if Enter1.get()[2] == 1 or Enter1.get()[2] == 0:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-" + str(Enter1.get()[2:4]) + "-19" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 8:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-0" + str(Enter1.get()[3]) + "-18" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 9:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-1" + str(Enter1.get()[3]) + "-18" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 2:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-0" + str(Enter1.get()[3]) + "-20" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 3:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-1" + str(Enter1.get()[3]) + "-20" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 4:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-0" + str(Enter1.get()[3]) + "-21" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 5:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-1" + str(Enter1.get()[3]) + "-21" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 6:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-0" + str(Enter1.get()[3]) + "-22" + (str(Enter1.get()[0:2])))
    if Enter1.get()[2] == 7:
        dob_confirm = ("Data urodzenia to " +
                       str(Enter1.get()[4:6]) + "-1" + str(Enter1.get()[3]) + "-21" + (str(Enter1.get()[0:2])))
    Lab5.config(text=dob_confirm)


def sex_from_pesel():
    if int(Enter1.get()[9]) % 2 == 0:
        sex = "PESEL nalezy do kobiety."
        Lab3.config(text=sex)
    else:
        sex = "PESEL nalezy do mezczyzny"
        Lab3.config(text=sex)


def check_pesel():
    global result
    if len(Enter1.get()) == 11:
        p0 = str(int(Enter1.get()[0]) * 1)
        p1 = str(int(Enter1.get()[1]) * 3)
        p2 = str(int(Enter1.get()[2]) * 7)
        p3 = str(int(Enter1.get()[3]) * 9)
        p4 = str(int(Enter1.get()[4]) * 1)
        p5 = str(int(Enter1.get()[5]) * 3)
        p6 = str(int(Enter1.get()[6]) * 7)
        p7 = str(int(Enter1.get()[7]) * 9)
        p8 = str(int(Enter1.get()[8]) * 1)
        p9 = str(int(Enter1.get()[9]) * 3)
        suma = str(int(p0[-1]) + int(p1[-1]) + int(p2[-1]) + int(p3[-1]) + int(p4[-1]) +
                   int(p5[-1]) + int(p6[-1]) + int(p7[-1]) + int(p8[-1]) + int(p9[-1]))
        suma_kontrolna = 10 - int(suma[-1])
        if suma_kontrolna == int(Enter1.get()[10]):
            result = "PESEL poprawny, suma kontrolna się zgadza."
        else:
            result = "Podany PESEL jest niepoprawny."
    else:
        result = "Niepoprawna ilość cyfr w PESELu"
    sex_from_pesel()
    dob_from_pesel()
    Lab4.config(text=result)


def generate_pesel():
    global generated_pesel
    if E1.get().isdigit() == False:
        info = "Nieprawidłowe znaki"
        L4.config(text=info)
    if len(E1.get()) > 8 or len(E1) < 8:
        info = "Nieprawidłowa ilość cyfr"
        L4.config(text=info)
    if man.get() == 1:
        num_list = [1, 3, 5, 7, 9]
        position_1 = E1.get()[6]
        position_2 = E1.get()[7]
        if E1.get()[4] == "1" and E1.get()[5] == "8" and E1.get()[2] == "0":
            position_3 = 8
        if E1.get()[4] == "1" and E1.get()[5] == "8" and E1.get()[2] == "1":
            position_3 = 9
        if E1.get()[4] == "2" and E1.get()[5] == "0" and E1.get()[2] == "0":
            position_3 = 2
        if E1.get()[4] == "2" and E1.get()[5] == "0" and E1.get()[2] == "1":
            position_3 = 3
        if E1.get()[4] == "2" and E1.get()[5] == "1" and E1.get()[2] == "0":
            position_3 = 4
        if E1.get()[4] == "2" and E1.get()[5] == "1" and E1.get()[2] == "1":
            position_3 = 5
        if E1.get()[4] == "2" and E1.get()[5] == "2" and E1.get()[2] == "0":
            position_3 = 6
        if E1.get()[4] == "2" and E1.get()[5] == "2" and E1.get()[2] == "1":
            position_3 = 7
        if E1.get()[4] == "1" and E1.get()[5] == "9" and E1.get()[2] == "0":
            position_3 = E1.get()[2]
        if E1.get()[4] == "1" and E1.get()[5] == "9" and E1.get()[2] == "1":
            position_3 = E1.get()[2]
        position_4 = E1.get()[3]
        position_5 = E1.get()[0]
        position_6 = E1.get()[1]
        position_7 = random.randint(0, 9)
        position_8 = random.randint(0, 9)
        position_9 = str(random.randint(0, 9))
        position_10 = random.choice(num_list)
        p_2 = position_2 * 3
        p_3 = str(position_3 * 7)
        p_4 = position_4 * 9
        p_6 = position_6 * 3
        p_7 = str(position_7 * 7)
        p_8 = str(position_8 * 9)
        p_10 = str(position_10 * 3)
        sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                  int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
        control_sum = 10 - int(sum[-1])
        generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
            str(position_7) + str(position_8) + str(position_9) + \
            str(position_10) + str(control_sum)
        L4.config(text=generated_pesel)
    if woman.get() == 1:
        num_list = [0, 2, 4, 6, 8]
        position_1 = E1.get()[6]
        position_2 = E1.get()[7]
        if E1.get()[4] == "1" and E1.get()[5] == "8" and E1.get()[2] == "0":
            position_3 = 8
        if E1.get()[4] == "1" and E1.get()[5] == "8" and E1.get()[2] == "1":
            position_3 = 9
        if E1.get()[4] == "2" and E1.get()[5] == "0" and E1.get()[2] == "0":
            position_3 = 2
        if E1.get()[4] == "2" and E1.get()[5] == "0" and E1.get()[2] == "1":
            position_3 = 3
        if E1.get()[4] == "2" and E1.get()[5] == "1" and E1.get()[2] == "0":
            position_3 = 4
        if E1.get()[4] == "2" and E1.get()[5] == "1" and E1.get()[2] == "1":
            position_3 = 5
        if E1.get()[4] == "2" and E1.get()[5] == "2" and E1.get()[2] == "0":
            position_3 = 6
        if E1.get()[4] == "2" and E1.get()[5] == "2" and E1.get()[2] == "1":
            position_3 = 7
        if E1.get()[4] == "1" and E1.get()[5] == "9" and E1.get()[2] == "0":
            position_3 = E1.get()[2]
        if E1.get()[4] == "1" and E1.get()[5] == "9" and E1.get()[2] == "1":
            position_3 = E1.get()[2]
        position_4 = E1.get()[3]
        position_5 = E1.get()[0]
        position_6 = E1.get()[1]
        position_7 = random.randint(0, 9)
        position_8 = random.randint(0, 9)
        position_9 = str(random.randint(0, 9))
        position_10 = random.choice(num_list)
        p_2 = position_2 * 3
        p_3 = str(position_3 * 7)
        p_4 = position_4 * 9
        p_6 = position_6 * 3
        p_7 = str(position_7 * 7)
        p_8 = str(position_8 * 9)
        p_10 = str(position_10 * 3)
        sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                  int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
        control_sum = 10 - int(sum[-1])
        generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
            str(position_7) + str(position_8) + str(position_9) + \
            str(position_10) + str(control_sum)
        L4.config(text=generated_pesel)

# dorobic wyjatki zeby nie wprowadzic blednych wartosci
# generowanie tozsamosci z imionami i nazwiskami
# opcja kopiowania peselu


win = tk.Tk()
win.title("PESEL")
win.geometry('500x500')

tabGeneral = ttk.Notebook(win)
tabGeneral.pack()

tab1_gen = ttk.Frame(tabGeneral)
tabGeneral.add(tab1_gen, text='Generowanie PESEL')

topframe = Frame(tab1_gen)
topframe.pack(side=TOP)

bottomframe = Frame(tab1_gen)
bottomframe.pack(side=BOTTOM)

lastframe = Frame(tab1_gen)
lastframe.pack(side=BOTTOM)
L1 = Label(topframe, text="Data urodzenia (DDMMRRRR)")
L1.pack(side=LEFT)

date = StringVar
E1 = Entry(topframe)
E1.pack(side=RIGHT)

L2 = Label(bottomframe, text="Wybierz płeć")
L2.pack(side=LEFT)

man = IntVar()
check_man = Checkbutton(bottomframe,
                        text="Mezczyzna",
                        variable=man)
check_man.pack()

woman = IntVar()
check_woman = Checkbutton(bottomframe,
                          text="Kobieta",
                          variable=woman)
check_woman.pack()

gen_button = Button(lastframe,
                    text="GENERATE",
                    command=generate_pesel,
                    state=ACTIVE,
                    compound="center")
gen_button.pack()

L3 = Label(lastframe)
L3.pack(side=LEFT)

L4 = Label(lastframe)
L4.pack(side=LEFT)

tab2_check = ttk.Frame(tabGeneral)
tabGeneral.add(tab2_check, text='Sprawdzanie PESEL')

upframe = Frame(tab2_check)
upframe.pack(side=TOP)

midframe = Frame(tab2_check)
midframe.pack(side=BOTTOM)

downframe = Frame(tab2_check)
downframe.pack(side=BOTTOM)
Lab1 = Label(upframe, text="Wpisz PESEL")
Lab1.pack(side=LEFT)

Enter1 = Entry(upframe)
Enter1.pack(side=RIGHT)

check_button = Button(midframe,
                      text="CHECK",
                      command=check_pesel,
                      state=ACTIVE,
                      compound="center")
check_button.pack()

lastestframe = Frame(downframe)
lastestframe.pack(side=BOTTOM)

lastestframe2 = Frame(downframe)
lastestframe2.pack(side=BOTTOM)
Lab3 = Label(lastestframe)
Lab3.pack(side=BOTTOM)

Lab4 = Label(lastestframe)
Lab4.pack(side=TOP)

Lab5 = Label(lastestframe2)
Lab5.pack(side=BOTTOM)
win.mainloop()
