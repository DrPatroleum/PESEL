import random
from tkinter import *
import datetime
import tkinter as tk
import tkinter.ttk as ttk
from tkcalendar import Calendar
import babel.numbers

data = ''
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
months = ["01", "02", "03", "04", "05",
          "06", "07", "08", "09", "10", "11", "12"]
today = datetime.date.today()
year = today.year


def zodiaq_from_pesel():
    global zodiaq
    z_month = str(dob_confirm[20:22])
    z_day = int(dob_confirm[17:19])
    if z_month == "01":
        if z_day >= 20:
            zodiaq = "AQUARIUS"
        elif z_day < 20:
            zodiaq = "CAPRICORN"
    if z_month == "02":
        if z_day >= 19:
            zodiaq = "PISCES"
        elif z_day < 19:
            zodiaq = "AQUARIUS"
    if z_month == "03":
        if z_day >= 21:
            zodiaq = "ARIES"
        elif z_day < 21:
            zodiaq = "PISCES"
    if z_month == "04":
        if z_day >= 20:
            zodiaq = "TAURUS"
        elif z_day < 20:
            zodiaq = "ARIES"
    if z_month == "05":
        if z_day >= 21:
            zodiaq = "GEMINI"
        elif z_day < 21:
            zodiaq = "TAURUS"
    if z_month == "06":
        if z_day >= 21:
            zodiaq = "CANCER"
        elif z_day < 21:
            zodiaq = "GEMINI"
    if z_month == "07":
        if z_day >= 23:
            zodiaq = "LEO"
        elif z_day < 23:
            zodiaq = "CANCER"
    if z_month == "08":
        if z_day >= 23:
            zodiaq = "VIRGO"
        elif z_day < 23:
            zodiaq = "LEO"
    if z_month == "09":
        if z_day >= 23:
            zodiaq = "LIBRA"
        elif z_day < 23:
            zodiaq = "VIRGO"
    if z_month == "10":
        if z_day >= 23:
            zodiaq = "SCORPIO"
        elif z_day < 23:
            zodiaq = "LIBRA"
    if z_month == "11":
        if z_day >= 22:
            zodiaq = "SAGITTARIUS"
        elif z_day < 22:
            zodiaq = "SCORPIO"
    if z_month == "12":
        if z_day >= 22:
            zodiaq = "CAPRICORN"
        elif z_day < 22:
            zodiaq = "SAGITTARIUS"


def dob_from_pesel():
    global dob_confirm
    if int(Enter1.get()[2]) == 1 or int(Enter1.get()[2]) == 0:
        dob_confirm = ("Date of birth is " + str(Enter1.get()[4:6]) + "-" + str(
            Enter1.get()[2:4]) + "-19" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 8:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-0" + str(Enter1.get()[3]) + "-18" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 9:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-1" + str(Enter1.get()[3]) + "-18" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 2:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-0" + str(Enter1.get()[3]) + "-20" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 3:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-1" + str(Enter1.get()[3]) + "-20" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 4:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-0" + str(Enter1.get()[3]) + "-21" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 5:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-1" + str(Enter1.get()[3]) + "-21" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 6:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-0" + str(Enter1.get()[3]) + "-22" + (str(Enter1.get()[0:2])))
    if int(Enter1.get()[2]) == 7:
        dob_confirm = ("Date of birth is " + str(Enter1.get()
                       [4:6]) + "-1" + str(Enter1.get()[3]) + "-21" + (str(Enter1.get()[0:2])))
    return dob_confirm


def sex_from_pesel():
    global sex
    if int(Enter1.get()[9]) % 2 == 0:
        sex = "PESEL belongs to a woman."
        return sex
    else:
        sex = "PESEL belongs to a man."
        return sex


def check_pesel():
    global result
    while True:
        if not Enter1.get():
            result = "Provide PESEL!"
            Lab4.config(text=result)
            break
        if not Enter1.get().isdigit():
            result = "Incorrect characters!"
            Lab4.config(text=result)
            break
        if len(Enter1.get()) != 11:
            result = "Incorrect number of digits in PESEL"
            Lab4.config(text=result)
            break
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
            sum = str(int(p0[-1]) + int(p1[-1]) + int(p2[-1]) + int(p3[-1]) + int(p4[-1]) +
                      int(p5[-1]) + int(p6[-1]) + int(p7[-1]) + int(p8[-1]) + int(p9[-1]))
            control_sum = 10 - int(sum[-1])
            if control_sum == int(Enter1.get()[10]):
                result = "PESEL is correct, the checksum is correct"
            else:
                result = "The provided PESEL number is incorrect"
            dob_from_pesel()
            sex_from_pesel()
            final_result = result + "\n" + dob_confirm + "\n" + sex + "\n"
            Lab4.config(text=final_result)
            break


def checkbutton_man_opt_selected():
    if man_opt.get() == 1:
        option_woman.config(state=tk.DISABLED)
    else:
        option_woman.config(state=tk.NORMAL)


def checkbutton_woman_opt_selected():
    if woman_opt.get() == 1:
        option_man.config(state=tk.DISABLED)
    else:
        option_man.config(state=tk.NORMAL)


def checkbutton_man_selected():
    if man.get() == 1:
        check_woman.config(state=tk.DISABLED)
    else:
        check_woman.config(state=tk.NORMAL)


def checkbutton_woman_selected():
    if woman.get() == 1:
        check_man.config(state=tk.DISABLED)
    else:
        check_man.config(state=tk.NORMAL)


def copy_result():
    win.clipboard_clear()
    win.clipboard_append(generated_pesel)
    info = "PESEL has been copied!"
    L4a.config(text=info)


def copy_result2():
    win.clipboard_clear()
    win.clipboard_append(generated_identity)


def generate_pesel():
    global generated_pesel
    if man_opt.get() == 0 and woman_opt.get() == 0:
        info = "Choose gender!"
        L4.config(text=info)
    if man.get() == 1:
        num_list = [1, 3, 5, 7, 9]
        while True:
            position_1 = kalendarz.get_date()[8]
            position_2 = kalendarz.get_date()[9]
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "8" and kalendarz.get_date()[3] == "0":
                position_3 = 8
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "8" and kalendarz.get_date()[3] == "1":
                position_3 = 9
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "0" and kalendarz.get_date()[3] == "0":
                position_3 = 2
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "0" and kalendarz.get_date()[3] == "1":
                position_3 = 3
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "1" and kalendarz.get_date()[3] == "0":
                position_3 = 4
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "1" and kalendarz.get_date()[3] == "1":
                position_3 = 5
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "2" and kalendarz.get_date()[3] == "0":
                position_3 = 6
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "2" and kalendarz.get_date()[3] == "1":
                position_3 = 7
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "9" and kalendarz.get_date()[3] == "0":
                position_3 = kalendarz.get_date()[2]
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "9" and kalendarz.get_date()[3] == "1":
                position_3 = kalendarz.get_date()[2]
            position_4 = kalendarz.get_date()[4]
            position_5 = kalendarz.get_date()[0]
            position_6 = kalendarz.get_date()[1]
            position_7 = random.randint(0, 9)
            position_8 = random.randint(0, 9)
            position_9 = str(random.randint(0, 9))
            position_10 = random.choice(num_list)
            p_2 = str(position_2 * 3)
            p_3 = str(position_3 * 7)
            p_4 = str(position_4 * 9)
            p_6 = str(position_6 * 3)
            p_7 = str(position_7 * 7)
            p_8 = str(position_8 * 9)
            p_10 = str(position_10 * 3)
            sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                      int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
            if int(sum[-1]) != 0:
                break
        control_sum = 10 - int(sum[-1])
        generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
            str(position_7) + str(position_8) + str(position_9) + \
            str(position_10) + str(control_sum)
        inf = ""
        L4.config(text=generated_pesel)
        L4a.config(text=inf)
    elif woman.get() == 1:
        num_list = [0, 2, 4, 6, 8]
        while True:
            position_1 = kalendarz.get_date()[8]
            position_2 = kalendarz.get_date()[9]
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "8" and kalendarz.get_date()[3] == "0":
                position_3 = 8
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "8" and kalendarz.get_date()[3] == "1":
                position_3 = 9
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "0" and kalendarz.get_date()[3] == "0":
                position_3 = 2
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "0" and kalendarz.get_date()[3] == "1":
                position_3 = 3
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "1" and kalendarz.get_date()[3] == "0":
                position_3 = 4
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "1" and kalendarz.get_date()[3] == "1":
                position_3 = 5
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "2" and kalendarz.get_date()[3] == "0":
                position_3 = 6
            if kalendarz.get_date()[6] == "2" and kalendarz.get_date()[7] == "2" and kalendarz.get_date()[3] == "1":
                position_3 = 7
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "9" and kalendarz.get_date()[3] == "0":
                position_3 = kalendarz.get_date()[2]
            if kalendarz.get_date()[6] == "1" and kalendarz.get_date()[7] == "9" and kalendarz.get_date()[3] == "1":
                position_3 = kalendarz.get_date()[2]
            position_4 = kalendarz.get_date()[4]
            position_5 = kalendarz.get_date()[0]
            position_6 = kalendarz.get_date()[1]
            position_7 = random.randint(0, 9)
            position_8 = random.randint(0, 9)
            position_9 = str(random.randint(0, 9))
            position_10 = random.choice(num_list)
            p_2 = str(position_2 * 3)
            p_3 = str(position_3 * 7)
            p_4 = str(position_4 * 9)
            p_6 = str(position_6 * 3)
            p_7 = str(position_7 * 7)
            p_8 = str(position_8 * 9)
            p_10 = str(position_10 * 3)
            sum = str(int(position_1[-1]) + int(p_2[-1]) + int(p_3[-1]) + int(p_4[-1]) + int(position_5[-1]) +
                      int(p_6[-1]) + int(p_7[-1]) + int(p_8[-1]) + int(position_9[-1]) + int(p_10[-1]))
            if int(sum[-1]) != 0:
                break
        control_sum = 10 - int(sum[-1])
        generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
            str(position_7) + str(position_8) + str(position_9) + \
            str(position_10) + str(control_sum)
        inf = ""
        L4.config(text=generated_pesel)
        L4a.config(text=inf)


def zodiaq_new_identity():
    global zodiaq
    z_month = str(date_of_birth[3:5])
    z_day = int(date_of_birth[:2])
    if z_month == "01":
        if z_day >= 20:
            zodiaq = "AQUARIUS"
        elif z_day < 20:
            zodiaq = "CAPRICORN"
    if z_month == "02":
        if z_day >= 19:
            zodiaq = "PISCES"
        elif z_day < 19:
            zodiaq = "AQUARIUS"
    if z_month == "03":
        if z_day >= 21:
            zodiaq = "ARIES"
        elif z_day < 21:
            zodiaq = "PISCES"
    if z_month == "04":
        if z_day >= 20:
            zodiaq = "TAURUS"
        elif z_day < 20:
            zodiaq = "ARIES"
    if z_month == "05":
        if z_day >= 21:
            zodiaq = "GEMINI"
        elif z_day < 21:
            zodiaq = "TAURUS"
    if z_month == "06":
        if z_day >= 21:
            zodiaq = "CANCER"
        elif z_day < 21:
            zodiaq = "GEMINI"
    if z_month == "07":
        if z_day >= 23:
            zodiaq = "LEO"
        elif z_day < 23:
            zodiaq = "CANCER"
    if z_month == "08":
        if z_day >= 23:
            zodiaq = "VIRGO"
        elif z_day < 23:
            zodiaq = "LEO"
    if z_month == "09":
        if z_day >= 23:
            zodiaq = "LIBRA"
        elif z_day < 23:
            zodiaq = "VIRGO"
    if z_month == "10":
        if z_day >= 23:
            zodiaq = "SCORPIO"
        elif z_day < 23:
            zodiaq = "LIBRA"
    if z_month == "11":
        if z_day >= 22:
            zodiaq = "SAGITTARIUS"
        elif z_day < 22:
            zodiaq = "SCORPIO"
    if z_month == "12":
        if z_day >= 22:
            zodiaq = "CAPRICORN"
        elif z_day < 22:
            zodiaq = "SAGITTARIUS"


def generate_identity():
    global generated_identity
    global date_of_birth
    while True:
        if man_opt.get() == 0 and woman_opt.get() == 0:
            generated_personality = "Choose gender!"
            Lab6.config(text=generated_personality)
            break
        if not EE.get():
            generated_personality = "Provide age!"
            Lab6.config(text=generated_personality)
            break
        if not EE.get().isdigit():
            generated_personality = "Incorrect age!"
            Lab6.config(text=generated_personality)
            break
        if man_opt.get() == 1:
            name = random.choice(men_names)
            last_name = random.choice(men_surnames)
            year_of_birth = int(year) - int(EE.get())
            month_of_birth = random.choice(months)
            day_of_birth = random.choice(days)
            date_of_birth = str(day_of_birth) + "-" + \
                str(month_of_birth) + "-" + str(year_of_birth)
            dob_for_pesel = str(day_of_birth) + \
                str(month_of_birth) + str(year_of_birth)
            num_list = [1, 3, 5, 7, 9]
            while True:
                position_1 = dob_for_pesel[6]
                position_2 = dob_for_pesel[7]
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "0":
                    position_3 = 8
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "1":
                    position_3 = 9
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "0":
                    position_3 = 2
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "1":
                    position_3 = 3
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "0":
                    position_3 = 4
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "1":
                    position_3 = 5
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "0":
                    position_3 = 6
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "1":
                    position_3 = 7
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "0":
                    position_3 = dob_for_pesel[2]
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "1":
                    position_3 = dob_for_pesel[2]
                position_4 = dob_for_pesel[3]
                position_5 = dob_for_pesel[0]
                position_6 = dob_for_pesel[1]
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
                if int(sum[-1]) != 0:
                    break
            control_sum = 10 - int(sum[-1])
            generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
                str(position_7) + str(position_8) + str(position_9) + \
                str(position_10) + str(control_sum)
            zodiaq_new_identity()
            generated_identity = "Generated identity:\n" + \
                name + " " + last_name + "\nDate of birth: " + \
                date_of_birth + "\nPESEL: " + generated_pesel + "\nZodiaq sign: " + zodiaq
            Lab6.config(text=generated_identity)
            break
        if woman_opt.get() == 1:
            name = random.choice(women_names)
            last_name = random.choice(women_surnames)
            year_of_birth = int(year) - int(EE.get())
            month_of_birth = random.choice(months)
            day_of_birth = random.choice(days)
            date_of_birth = str(day_of_birth) + "-" + \
                str(month_of_birth) + "-" + str(year_of_birth)
            dob_for_pesel = str(day_of_birth) + \
                str(month_of_birth) + str(year_of_birth)
            num_list = [0, 2, 4, 6, 8]
            while True:
                position_1 = dob_for_pesel[6]
                position_2 = dob_for_pesel[7]
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "0":
                    position_3 = 8
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "8" and dob_for_pesel[2] == "1":
                    position_3 = 9
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "0":
                    position_3 = 2
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "0" and dob_for_pesel[2] == "1":
                    position_3 = 3
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "0":
                    position_3 = 4
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "1" and dob_for_pesel[2] == "1":
                    position_3 = 5
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "0":
                    position_3 = 6
                if dob_for_pesel[4] == "2" and dob_for_pesel[5] == "2" and dob_for_pesel[2] == "1":
                    position_3 = 7
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "0":
                    position_3 = dob_for_pesel[2]
                if dob_for_pesel[4] == "1" and dob_for_pesel[5] == "9" and dob_for_pesel[2] == "1":
                    position_3 = dob_for_pesel[2]
                position_4 = dob_for_pesel[3]
                position_5 = dob_for_pesel[0]
                position_6 = dob_for_pesel[1]
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
                if int(sum[-1]) != 0:
                    break
            control_sum = 10 - int(sum[-1])
            generated_pesel = str(position_1) + str(position_2) + str(position_3) + str(position_4) + str(position_5) + str(position_6) + \
                str(position_7) + str(position_8) + str(position_9) + \
                str(position_10) + str(control_sum)
            zodiaq_new_identity()
            generated_identity = "Generated identity:\n" + \
                name + " " + last_name + "\nDate of birth: " + \
                date_of_birth + "\nPESEL: " + generated_pesel + "\nZodiaq sign: " + zodiaq
            Lab6.config(text=generated_identity)
            break


win = tk.Tk()
win.title("PESEL")
win.geometry('350x350')
win.resizable(True, True)

tabGeneral = ttk.Notebook(win)
tabGeneral.pack()

# Zakładka numer 1 GENEROWANIE PESEL

tab1_gen = ttk.Frame(tabGeneral)
tabGeneral.add(tab1_gen, text='Generate PESEL')

L1 = Label(tab1_gen, text="Date of birth")
L1.grid(row=0, column=0, columnspan=6, padx=5, pady=5)

kalendarz = Calendar(tab1_gen, selectmode='day',
                     date_pattern='dd/mm/yyyy', locale='pl_PL')
date = kalendarz.datetime.today()
kalendarz.grid(row=1, column=0, columnspan=6)

L2 = Label(tab1_gen, text="Select gender:")
L2.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

man = IntVar()
check_man = Checkbutton(tab1_gen,
                        text="Man",
                        variable=man,
                        command=checkbutton_man_selected)
check_man.grid(row=2, column=2, columnspan=2, padx=5, pady=5)


woman = IntVar()
check_woman = Checkbutton(tab1_gen,
                          text="Woman",
                          variable=woman,
                          command=checkbutton_woman_selected)
check_woman.grid(row=2, column=4, columnspan=2, padx=5, pady=5)


gen_button = Button(tab1_gen,
                    text="GENERATE",
                    command=generate_pesel,
                    state=ACTIVE,
                    compound=LEFT)
gen_button.grid(row=3, column=0, columnspan=3, sticky=E, padx=5, pady=5)


copy_button0 = Button(tab1_gen,
                      text="COPY",
                      command=copy_result,
                      state=ACTIVE,
                      compound=LEFT)
copy_button0.grid(row=3, column=3, columnspan=3, sticky=W, padx=5, pady=5)


L4 = Label(tab1_gen)
L4.grid(row=4, column=0, columnspan=6, padx=5, pady=5)


L4a = Label(tab1_gen)
L4a.grid(row=5, column=0, columnspan=6, padx=5, pady=5)


# Zakładka numer 2 SPRAWDZANIE PESEL

tab2_check = ttk.Frame(tabGeneral)
tabGeneral.add(tab2_check, text='Check PESEL')

Lab1 = Label(tab2_check, text="Provide PESEL")
Lab1.grid(row=0, column=3, padx=100, pady=5, sticky=N)

Enter1 = Entry(tab2_check, width=15)
Enter1.grid(row=1, column=3, padx=100, pady=5)

check_button = Button(tab2_check,
                      text="CHECK",
                      command=check_pesel,
                      state=ACTIVE)
check_button.grid(row=2, column=3, padx=5, pady=5)

Lab4 = Label(tab2_check)
Lab4.grid(row=3, column=3, padx=5, pady=5)

# Zakładka numer 3 TWORZENIE TOZSAMOSCI

tab3_check = ttk.Frame(tabGeneral)
tabGeneral.add(tab3_check, text='Create identity')

Ldsd2 = Label(tab3_check, text="Choose gender:")
Ldsd2.grid(row=0, column=0, padx=5, pady=5)

man_opt = IntVar()
option_man = Checkbutton(tab3_check,
                         text="Man",
                         variable=man_opt,
                         command=checkbutton_man_opt_selected)
option_man.grid(row=0, column=1, padx=5, pady=5)

woman_opt = IntVar()
option_woman = Checkbutton(tab3_check,
                           text="Woman",
                           variable=woman_opt,
                           command=checkbutton_woman_opt_selected)
option_woman.grid(row=0, column=2, padx=5, pady=5)

L7 = Label(tab3_check, text="Age in years:")
L7.grid(row=1, column=0, padx=5, pady=5)

EE = Entry(tab3_check, width=15)
EE.grid(row=1, column=1, columnspan=2, padx=5, pady=5, sticky=W)

makenew_button = Button(tab3_check,
                        text="MAKE NEW ONE",
                        command=generate_identity,
                        state=ACTIVE,
                        compound=LEFT)
makenew_button.grid(row=3, column=0, padx=5, pady=5, sticky=E)

copy_button01 = Button(tab3_check,
                       text="COPY",
                       command=copy_result2,
                       state=ACTIVE,
                       compound=RIGHT)
copy_button01.grid(row=3, column=1, padx=5, pady=5, sticky=W)

Lab6 = Label(tab3_check)
Lab6.grid(row=4, column=0, padx=5, pady=5, columnspan=3)

Lab7 = Label(tab3_check)
Lab7.grid(row=5, column=0, padx=5, pady=5, columnspan=3)

win.mainloop()
