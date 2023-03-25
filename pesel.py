import random
from tkinter import *
from tkinter import messagebox
import tkinter as tk
import tkinter.ttk as ttk

date = ''

women_names = ["ANNA", "KATARZYNA", "MARIA", "MAŁGORZATA", "AGNIESZKA", "BARBARA", "EWA", "MAGDALENA", "ELŻBIETA", "KRYSTYNA", "JOANNA",
               "ALEKSANDRA", "MONIKA", "ZOFIA", "TERESA", "NATALIA", "JULIA", "DANUTA", "KAROLINA", "MARTA", "BEATA", "DOROTA", "ALICJA", "HALINA",
               "JADWIGA", "JOLANTA", "IWONA", "GRAŻYNA", "JANINA", "PAULINA", "ZUZANNA", "JUSTYNA", "IRENA", "HANNA", "WIKTORIA",
               "BOŻENA", "RENATA", "URSZULA", "AGATA", "SYLWIA", "MAJA", "PATRYCJA", "HELENA", "IZABELA", "EMILIA", "OLIWIA", "ANETA", "WERONIKA",
               "EWELINA", "MARTYNA", "KLAUDIA", "GABRIELA", "MARZENA", "LENA", "DOMINIKA", "MARIANNA", "AMELIA", "KINGA",
               "STANISŁAWA", "EDYTA", "KAMILA", "WIESŁAWA", "ALINA", "WANDA", "DARIA", "LIDIA", "MARIOLA", "LUCYNA", "NIKOLA", "MILENA", "WIOLETTA",
               "MIROSŁAWA", "LAURA", "ANTONINA", "ANGELIKA", "OLGA", "KAZIMIERA", "BOGUMIŁA", "ILONA", "MICHALINA", "SANDRA", "GENOWEFA", "KORNELIA",
               "MARLENA", "HENRYKA", "ŁUCJA", "SABINA", "BOGUSŁAWA", "NINA", "JÓZEFA", "ANITA", "STEFANIA", "IGA", "LILIANA", "REGINA", "POLA",
               "MARCELINA", "JAGODA", "CZESŁAWA", "ANIELA", "WŁADYSŁAWA", "KARINA", "WIOLETA", "ADRIANNA", "DIANA", "ROKSANA",
               "DAGMARA", "SARA", "MALWINA", "ELIZA", "CECYLIA", "ŻANETA", "ZDZISŁAWA", "KLARA", "RÓŻA", "KAJA", "LEOKADIA", "BLANKA", "ANASTAZJA", "BRONISŁAWA",
               "EUGENIA", "JULITA", "ALDONA", "ROZALIA", "DANIELA", "LILIANNA", "MAGDA", "CELINA", "MATYLDA", "ADRIANA", "HONORATA", "VERONIKA",
               "NELA", "PAULA", "BRYGIDA", "AURELIA", "KALINA", "MARIKA", "GERTRUDA", "MIECZYSŁAWA", "SONIA", "ELWIRA", "ANDŻELIKA", "POLINA",
               "ARLETA", "LUIZA", "ADELA", "JUDYTA", "NICOLE", "FRANCISZKA", "MARIANA", "NICOLA", "LIWIA", "JOWITA", "VANESSA", "ALFREDA"]
women_surnames = ["NOWAK", "KOWALSKA", "WIŚNIEWSKA", "WÓJCIK", "KOWALCZYK", "KAMIŃSKA", "LEWANDOWSKA", "ZIELIŃSKA", "SZYMAŃSKA", "DĄBROWSKA",
                  "WOŹNIAK", "KOZŁOWSKA", "MAZUR", "JANKOWSKA", "KWIATKOWSKA", "WOJCIECHOWSKA", "KRAWCZYK", "KACZMAREK", "PIOTROWSKA", "GRABOWSKA", "PAWŁOWSKA",
                  "MICHALSKA", "KRÓL", "ZAJĄC", "WIECZOREK", "JABŁOŃSKA", "WRÓBEL", "NOWAKOWSKA", "MAJEWSKA", "OLSZEWSKA", "ADAMCZYK", "JAWORSKA", "MALINOWSKA",
                  "STĘPIEŃ", "DUDEK", "GÓRSKA", "NOWICKA", "WITKOWSKA", "PAWLAK", "SIKORA", "WALCZAK", "RUTKOWSKA", "MICHALAK", "SZEWCZYK", "OSTROWSKA", "BARAN",
                  "TOMASZEWSKA", "ZALEWSKA", "WRÓBLEWSKA", "PIETRZAK", "JASIŃSKA", "MARCINIAK", "SADOWSKA", "JAKUBOWSKA", "ZAWADZKA", "DUDA", "WŁODARCZYK",
                  "CHMIELEWSKA", "BORKOWSKA", "BĄK", "WILK", "SOKOŁOWSKA", "SZCZEPAŃSKA", "SAWICKA", "LIS", "KUCHARSKA", "KALINOWSKA", "MACIEJEWSKA", "MAZUREK",
                  "WYSOCKA", "KUBIAK", "KOŁODZIEJ", "CZARNECKA", "KAŹMIERCZAK", "URBAŃSKA", "SIKORSKA", "KRUPA", "SOBCZAK", "KRAJEWSKA", "GŁOWACKA", "ZAKRZEWSKA",
                  "WASILEWSKA", "LASKOWSKA", "ZIÓŁKOWSKA", "GAJEWSKA", "KOZAK", "SZULC", "MRÓZ", "MAKOWSKA", "BRZEZIŃSKA", "PRZYBYLSKA", "KACZMARCZYK",
                  "BARANOWSKA", "SZYMCZAK", "ADAMSKA", "BŁASZCZYK", "BOROWSKA", "GÓRECKA", "SZCZEPANIAK", "KANIA", "LESZCZYŃSKA", "JANIK", "CZERWIŃSKA",
                  "CHOJNACKA", "LIPIŃSKA", "ANDRZEJEWSKA", "WESOŁOWSKA", "KOWALEWSKA", "MIKOŁAJCZYK", "MUCHA", "CIEŚLAK", "JAROSZ", "ZIĘBA", "KONIECZNA",
                  "KOZIOŁ", "MARKOWSKA", "KOWALIK", "KOŁODZIEJCZYK", "MUSIAŁ", "BRZOZOWSKA", "DOMAŃSKA", "TOMCZYK", "ORŁOWSKA", "PAWLIK", "PIĄTEK", "NOWACKA",
                  "KOPEĆ", "TOMCZAK", "KRUK", "KUREK", "ŻAK", "CIESIELSKA", "KOT", "MARKIEWICZ", "POLAK", "WAWRZYNIAK", "WOLSKA", "WÓJTOWICZ", "STANKIEWICZ",
                  "JASTRZĘBSKA", "SOWA", "URBANIAK", "KARPIŃSKA", "CZAJKOWSKA", "STASIAK", "WIERZBICKA", "ŁUCZAK", "NAWROCKA", "PIASECKA", "KLIMEK", "DZIEDZIC",
                  "SOSNOWSKA", "JANICKA", "BEDNAREK", "BIELECKA", "MILEWSKA", "GAJDA", "STEFAŃSKA", "MADEJ", "MAJCHRZAK", "LEŚNIAK", "JÓŹWIAK", "MAJ", "URBAN",
                  "KOWAL", "ŚLIWIŃSKA", "SKIBA", "MAŁECKA", "BEDNARCZYK", "SOCHA", "DOBROWOLSKA", "MICHALIK", "ROMANOWSKA", "DOMAGAŁA", "RATAJCZAK", "WRONA",
                  "WILCZYŃSKA", "KASPRZAK", "MATUSZEWSKA", "ORZECHOWSKA", "ŚWIĄTEK", "OLEJNICZAK", "PAJĄK", "RYBAK", "KUROWSKA", "BUKOWSKA", "SOBOLEWSKA",
                  "OWCZAREK", "MAZURKIEWICZ", "ŁUKASIK", "ROGOWSKA", "OLEJNIK", "GRZELAK", "KĘDZIERSKA", "KOSIŃSKA", "BARAŃSKA", "MATUSIAK", "SOBCZYK"]
men_names = ["PIOTR", "KRZYSZTOF", "ANDRZEJ", "TOMASZ", "PAWEŁ", "MICHAŁ", "JAN", "MARCIN", "JAKUB", "ADAM", "ŁUKASZ", "MAREK", "GRZEGORZ",
             "MATEUSZ", "STANISŁAW", "WOJCIECH", "MARIUSZ", "DARIUSZ", "MACIEJ", "ZBIGNIEW", "RAFAŁ", "ROBERT", "KAMIL", "JERZY", "DAWID",
             "SZYMON", "JACEK", "KACPER", "JÓZEF", "RYSZARD", "TADEUSZ", "BARTOSZ", "ARTUR", "JAROSŁAW", "SŁAWOMIR", "SEBASTIAN", "JANUSZ",
             "DAMIAN", "MIROSŁAW", "PATRYK", "ROMAN", "DANIEL", "FILIP", "HENRYK", "ANTONI", "PRZEMYSŁAW", "KAROL", "ALEKSANDER", "ADRIAN",
             "KAZIMIERZ", "WIESŁAW", "MARIAN", "ARKADIUSZ", "DOMINIK", "FRANCISZEK", "MIKOŁAJ", "BARTŁOMIEJ", "LESZEK", "WIKTOR", "KRYSTIAN",
             "WALDEMAR", "RADOSŁAW", "BOGDAN", "ZDZISŁAW", "KONRAD", "IGOR", "HUBERT", "EDWARD", "MIECZYSŁAW", "OSKAR", "MARCEL", "WŁADYSŁAW",
             "CZESŁAW", "MAKSYMILIAN", "EUGENIUSZ", "MIŁOSZ", "BOGUSŁAW", "IRENEUSZ", "NIKODEM", "STEFAN", "WITOLD", "LEON", "OLIWIER", "SYLWESTER",
             "ZYGMUNT", "ALAN", "WŁODZIMIERZ", "CEZARY", "ZENON", "GABRIEL", "IGNACY", "JULIAN", "NORBERT", "TYMON", "TYMOTEUSZ", "FABIAN", "BŁAŻEJ",
             "ERYK", "EMIL", "LECH", "BRONISŁAW", "WACŁAW", "NATAN", "KSAWERY", "BORYS", "BOLESŁAW", "REMIGIUSZ", "OLAF", "BERNARD", "KAJETAN", "KUBA",
             "EDMUND", "LUCJAN", "BRUNO", "ALBERT", "TOBIASZ", "ROMUALD", "GRACJAN", "SEWERYN", "SZCZEPAN", "ALFRED", "ERNEST", "JOACHIM", "LUDWIK",
             "LESŁAW", "BOGUMIŁ", "JĘDRZEJ", "GERARD", "FELIKS", "LEONARD", "JULIUSZ", "KLAUDIUSZ", "DORIAN", "TEODOR"]
men_surnames = ["NOWAK", "KOWALSKI", "WIŚNIEWSKI", "WÓJCIK", "KOWALCZYK", "KAMIŃSKI", "LEWANDOWSKI", "ZIELIŃSKI", "WOŹNIAK", "ZYMAŃSKI", "DĄBROWSKI",
                "KOZŁOWSKI", "MAZUR", "JANKOWSKI", "KWIATKOWSKI", "WOJCIECHOWSKI", "KRAWCZYK", "KACZMAREK", "PIOTROWSKI", "GRABOWSKI", "ZAJĄC",
                "PAWŁOWSKI", "KRÓL", "MICHALSKI", "WRÓBEL", "WIECZOREK", "JABŁOŃSKI", "NOWAKOWSKI", "MAJEWSKI", "OLSZEWSKI", "DUDEK", "JAWORSKI",
                "STĘPIEŃ", "MALINOWSKI", "ADAMCZYK", "GÓRSKI", "PAWLAK", "SIKORA", "NOWICKI", "WITKOWSKI", "RUTKOWSKI", "WALCZAK", "BARAN", "MICHALAK",
                "SZEWCZYK", "OSTROWSKI", "TOMASZEWSKI", "ZALEWSKI", "WRÓBLEWSKI", "PIETRZAK", "JASIŃSKI", "DUDA", "MARCINIAK", "SADOWSKI", "BĄK",
                "ZAWADZKI", "JAKUBOWSKI", "WILK", "CHMIELEWSKI", "BORKOWSKI", "WŁODARCZYK", "SOKOŁOWSKI", "SZCZEPAŃSKI", "SAWICKI", "LIS", "KUCHARSKI",
                "KALINOWSKI", "WYSOCKI", "MAZUREK", "KUBIAK", "MACIEJEWSKI", "KOŁODZIEJ", "KAŹMIERCZAK", "CZARNECKI", "KONIECZNY", "SOBCZAK", "KRUPA",
                "GŁOWACKI", "URBAŃSKI", "MRÓZ", "ZAKRZEWSKI", "WASILEWSKI", "KRAJEWSKI", "KOZAK", "LASKOWSKI", "SIKORSKI", "ZIÓŁKOWSKI", "GAJEWSKI", "SZULC",
                "MAKOWSKI", "KACZMARCZYK", "BRZEZIŃSKI", "BARANOWSKI", "PRZYBYLSKI", "KANIA", "SZYMCZAK", "JANIK", "BOROWSKI", "BŁASZCZYK", "ADAMSKI",
                "GÓRECKI", "SZCZEPANIAK", "CHOJNACKI", "LESZCZYŃSKI", "KOZIOŁ", "MUCHA", "KOWALEWSKI", "LIPIŃSKI", "ANDRZEJEWSKI", "CZERWIŃSKI",
                "WESOŁOWSKI", "MIKOŁAJCZYK", "ZIĘBA", "JAROSZ", "CIEŚLAK", "MUSIAŁ", "KOWALIK", "MARKOWSKI", "KOŁODZIEJCZYK", "KOPEĆ", "BRZOZOWSKI",
                "NOWACKI", "PIĄTEK", "ŻAK", "DOMAŃSKI", "PAWLIK", "ORŁOWSKI", "KUREK", "CIESIELSKI", "KOT", "WÓJTOWICZ", "TOMCZYK", "TOMCZAK", "KRUK",
                "WAWRZYNIAK", "POLAK", "WOLSKI", "MARKIEWICZ", "SOWA", "STASIAK", "JASTRZĘBSKI", "KARPIŃSKI", "STANKIEWICZ", "URBANIAK", "KLIMEK", "PIASECKI",
                "ŁUCZAK", "CZAJKOWSKI", "WIERZBICKI", "NAWROCKI", "GAJDA", "BIELECKI", "DZIEDZIC", "STEFAŃSKI", "BEDNAREK", "MADEJ", "MILEWSKI", "JANICKI",
                "SOSNOWSKI", "SKIBA", "KOWAL", "LEŚNIAK", "MAJ", "MAJCHRZAK", "JÓŹWIAK", "URBAN", "ŚLIWIŃSKI", "SOCHA", "MAŁECKI", "MAREK", "DOMAGAŁA",
                "BEDNARCZYK", "KASPRZAK", "DOBROWOLSKI", "WRONA", "PAJĄK", "MICHALIK", "MATUSZEWSKI", "RATAJCZAK", "OLEJNICZAK", "ORZECHOWSKI", "ŚWIĄTEK",
                "WILCZYŃSKI", "ROMANOWSKI", "KUROWSKI", "OLEJNIK", "ŁUKASIK", "ROGOWSKI", "RYBAK", "GRZELAK", "MAZURKIEWICZ", "BUKOWSKI", "OWCZAREK", "SROKA",
                "SOBOLEWSKI", "KOSIŃSKI", "KĘDZIERSKI", "BARAŃSKI", "ZYCH"]
months = {"01": "stycznia", "02": "lutego", "03": "marca", "04": "kwietnia", "05": "maja", "06": "czerwca", "07": "lipca",
          "08": "sierpnia", "09": "września", "10": "października", "11": "listopada", "12": "grudnia"}


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


def generate_man_personality():
    name = random.choice(men_names)
    last_name = random.choice(men_surnames)


# dorobic wyjatki zeby nie wprowadzic blednych wartosci
# generowanie tozsamosci z imionami i nazwiskami
# opcja kopiowania peselu
# dokonczyc opcje generowania tozsamosci

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

tab3_check = ttk.Frame(tabGeneral)
tabGeneral.add(tab3_check, text='Tworzenie tozsamosci')

upperframe = Frame(tab3_check)
upperframe.pack(side=TOP)

downerframe = Frame(tab3_check)
downerframe.pack(side=BOTTOM)

check_button = Button(upperframe,
                      text="MAKE NEW ONE",
                      command=check_pesel,
                      state=ACTIVE,
                      compound="center")
check_button.pack()

Lab6 = Label(downerframe)
Lab6.pack(side=BOTTOM)

win.mainloop()
