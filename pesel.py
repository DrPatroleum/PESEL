import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

date = ''


def dob_from_pesel(pesel):
    print("Data urodzenia to " +
          str(pesel[4:6]) + "-" + str(pesel[2:4]) + "-19" + (str(pesel[0:2])))


def sex_from_pesel(pesel):
    if int(pesel[9]) % 2 == 0:
        print("Kobieta")
    else:
        print("Męczyna")


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
    Lab4.config(text=result)


def generate_pesel():
    global generated_pesel
    if man.get() == 1:
        man_list = [1, 3, 5, 7, 9]
        m = random.choice(man_list)
        position_7 = random.randint(0, 9)
        position_8 = random.randint(0, 9)
        position_9 = random.randint(0, 9)
        # 0  1 . 2  3 . 4  5  6  7
        # 1  9 . 1  1 . 1  9  9  1
        p_0 = str(int(E1.get()[6]) * 1)
        p_1 = str(int(E1.get()[7]) * 3)
        if E1.get()[2] == 0 and E1.get()[5] == 8:
            p_2 = str(int(E1.get()[2]) * 7)
            p_3 = str(int(E1.get()[3]) * 9)
        if E1.get()[4] == 1 and E1.get()[5] == 9:
            p_2 = str(int(E1.get()[2]) * 7)
            p_3 = str(int(E1.get()[3]) * 9)

        p_4 = str(int(E1.get()[0]) * 1)
        p_5 = str(int(E1.get()[1]) * 3)
        p_6 = str(position_7 * 7)
        p_7 = str(position_8 * 9)
        p_8 = str(position_9 * 1)
        p_9 = str(m * 3)
        sum_man = str(int(p_0[-1]) + int(p_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) +
                      int(p_5[-1]) + int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(p_9[-1]))
        control_sum_man = 10 - int(sum_man[-1])
        generated_pesel = E1.get()[6] + E1.get()[7] + E1.get()[2] + E1.get()[3] + E1.get()[0] + E1.get()[1] + \
            str(position_7) + str(position_8) + str(position_9) + \
            str(m) + str(control_sum_man)
        L4.config(text=generated_pesel)
    if woman.get() == 1:
        woman_list = [0, 2, 4, 6, 8]
        k = random.choice(woman_list)
        position_7 = random.randint(0, 9)
        position_8 = random.randint(0, 9)
        position_9 = random.randint(0, 9)
        p_0 = str(int(E1.get()[6]) * 1)
        p_1 = str(int(E1.get()[7]) * 3)
        p_2 = str(int(E1.get()[2]) * 7)
        p_3 = str(int(E1.get()[3]) * 9)
        p_4 = str(int(E1.get()[0]) * 1)
        p_5 = str(int(E1.get()[1]) * 3)
        p_6 = str(position_7 * 7)
        p_7 = str(position_8 * 9)
        p_8 = str(position_9 * 1)
        p_9 = str(k * 3)
        sum_woman = str(int(p_0[-1]) + int(p_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) +
                        int(p_5[-1]) + int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(p_9[-1]))
        control_sum_woman = 10 - int(sum_woman[-1])
        generated_pesel = E1.get()[6] + E1.get()[7] + E1.get()[2] + E1.get()[3] + E1.get()[0] + E1.get()[1] + \
            str(position_7) + str(position_8) + str(position_9) + \
            str(k) + str(control_sum_woman)
        L4.config(text=generated_pesel)

# dorobic wyjatki zeby nie wprowadzic blednych wartosci
# w pasku wprowadzania ma być DDMMRRR
# zrobic wersje okienkowa
# generowanie tozsamosci z imionami i nazwiskami
# opcja kopiowania peselu
# zrobic plik readme


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
L1 = Label(topframe, text="Data urodzenia")
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
                      text="GENERATE",
                      command=check_pesel,
                      state=ACTIVE,
                      compound="center")
check_button.pack()

Lab3 = Label(downframe)
Lab3.pack(side=LEFT)

Lab4 = Label(downframe)
Lab4.pack(side=LEFT)

win.mainloop()
