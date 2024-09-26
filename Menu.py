import tkinter as tk
from PIL import ImageTk,Image
import os
from datetime import date, datetime
from dodaj import*
from dodajE import*
from usun import*
from szukaj import*
from minutnik import*


class Menu:

#utworzenie głównego menu
    def __init__(self):

        self.menu = tk.Tk()

        self.menu.title("KSIAZKA KUCHARSKA")   #tytul okna

        self.menu.geometry("600x600")   #ustawienie okna menu

        self.menu.resizable(0,0)   # ustawienie na stale okna

        # obrazek w glownym menu
        image = Image.open(r'D:\Projekt\Ksiazka\szkic.png')

        image_wbk = Image.open(r'D:\Projekt\Ksiazka\wbk.png')

        image_pol = Image.open(r'D:\Projekt\Ksiazka\polska.png')

        # zaladowanie zdjecia i flag dla języków
        self.img = ImageTk.PhotoImage(image)

        self.img_pol = ImageTk.PhotoImage(image_pol)

        self.img_wbk = ImageTk.PhotoImage(image_wbk)


        # tworzymy przyciski językowe
        self.button_pol = tk.Button(image= self.img_pol, width=50, height=30, bd=4,
                                    command= self.set_polish)
        self.button_pol.place(x= 80, y=10)


        self.button_wbk = tk.Button(image= self.img_wbk, width=50, height=30, bd=4,
                                    command= self.set_english)
        self.button_wbk.place(x=150, y=10 )


        self.labelbg = tk.Label(image = self.img)   #zdjecie jako tlo i umiejscowienie
        self.labelbg.pack(side="right")

        # podpis
        self.__labelA = tk.Label(text= "@by Tomasz R", font= "Helvetica 9 italic underline",
                                 background="yellow")
        self.__labelA.place(x=10, y=580)

        # ustawiamy przyciski opcji na None bez wyboru języka
        self.buttonD = None

        self.buttonS = None

        self.buttonU = None

        self.buttonM = None

            #pokazuje aktualną datę
        self.label_data = tk.Label(background= "LightBlue1", foreground= "orange red",
                                   font= "Arial 15 bold", width= 10)
        self.label_data.place(x= 90, y=420)


        #pokazuje aktualna godzinę
        self.label_godzina = tk.Label(background= "LightBlue1", foreground= "orange red",
                                      font= "Arial 15 bold", width= 10)
        self.label_godzina.place(x=90, y=450)

        # Rozpocznij cykliczne aktualizacje daty i godziny
        self.update_time_and_date()


        self.menu.mainloop()


    def set_polish(self):

            # przycisk dodaj
        self.buttonD = tk.Button(background= "navy", font= "Arial 15 bold",
                            foreground= "red", text = "DODAJ", command=Dodaj, bd=5, width=10)

            # przycisk usun
        self.buttonU = tk.Button(background= "SlateBlue1", foreground= "gold",
                            font= "Arial 15 bold underline", text= "USUŃ", bd=5, width=10, command=Usun)

            # przycisk wyszukaj
        self.buttonS = tk.Button( background= "purple1", foreground= "green2",
                            font= "Arial 15 bold", text= "SZUKAJ", bd=5, width=10, command= Szukaj)

            #przycisk minutnik
        self.buttonM = tk.Button( background= "SpringGreen2", foreground= "purple", command= Minutnik,
                                  font= "Arial 15 bold", text= "MINUTNIK", bd=5, width= 10)

        self.buttonM.place(x=85, y=310)

        self.buttonS.place(x=85, y=240)

        self.buttonU.place(x=85, y=170)

        self.buttonD.place(x=85, y=100)


    def set_english(self):

             # przycisk dodaj
        self.buttonD = tk.Button(background="navy", font="Arial 15 bold",
                                    foreground="red", text="ADD", command=DodajE, bd=5, width=10)

            #przycisk usun
        self.buttonU = tk.Button(background="SlateBlue1", foreground="gold",
                                    font="Arial 15 bold underline", text="DELETE", bd=5, width=10, command= UsunE)

             # przycisk wyszukaj
        self.buttonS = tk.Button(background="purple1", foreground="green2",
                                    font="Arial 15 bold", text="SEARCH", bd=5, width=10, command= SzukajE)

             # przycisk minutnik
        self.buttonM = tk.Button(background="SpringGreen2", foreground="purple",
                                font="Arial 15 bold", text="TIMER", bd=5, width=10, command= MinutnikE)


        self.buttonM.place(x=85, y=310)

        self.buttonS.place(x=85, y=240)

        self.buttonU.place(x=85, y=170)

        self.buttonD.place(x=85, y=100)


        #metoda dodająca datę i godzinę
    def data(self):

        today = date.today()

        now = datetime.now()

        formatted_date = today.strftime("%d %m %Y")  # format "dzien miesiac rok"

        formatted_time = now.strftime("%H:%M:%S")  # format "godzina:minuta:sekunda"

        # Ustawienie tekstu w etykietach
        self.label_data.config(text=formatted_date)

        self.label_godzina.config(text=formatted_time)


    def update_time_and_date(self):

        # Wywołaj funkcję data() co 1000 milisekund (1 sekunda)
        self.data()

        self.menu.after(1000, self.update_time_and_date)


Menu()