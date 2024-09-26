from datetime import date, datetime
import tkinter as tk
import pygame

#tworzymy klasę i okno do odliczania czsu
class Minutnik:

    def __init__(self):

        self.minutnik = tk.Tk()

        self.minutnik.title("MINUTNIK")

        self.minutnik.geometry("400x400+500+300")

        self.minutnik.resizable(0, 0)

        self.minutnik.configure(background="seashell2")


            #zmienna dla label
        funkcje = '''Wybierz czas do odmierzenia i kliknij "Start"
    H- godzina  M- minuty  S- sekundy'''

            #label informujący o tym co jest w menu
        self.label_funkcje = tk.Label( self.minutnik, background= "seashell2", foreground= "Black",
                                       font= "Arial 12 bold", text= funkcje)
        self.label_funkcje.place(x= 30, y=10)

            #label HMS
        self.label_HMS = tk.Label(self.minutnik, background= "seashell2", foreground= "red",
                                font= "Arial 12 bold underline", text= "H           M           S" )
        self.label_HMS.place(x= 120, y=70)


        #tworzymy trzy spinboxy które odpowiadają za wybór czasu
        spin_values_H = ("0", "1", "2", "3", "4", "5", "6")

        spin_values_S = ("0", "10", "20", "30", "40", "50")

        self.godzina = tk.Spinbox(self.minutnik, values= spin_values_H, width= 3, bd= 2, font="Arial 12")

        self.godzina.place(x= 110, y= 100)

        self.minuta = tk.Spinbox(self.minutnik, from_= 0, to= 59, width= 3, bd= 2, font="Arial 12")

        self.minuta.place(x= 170, y= 100)

        self.sekunda = tk.Spinbox(self.minutnik, values= spin_values_S, width= 3, bd= 2, font= "Arial 12")

        self.sekunda.place(x= 230, y=100)


        #przycisk start
        self.button_start = tk.Button(self.minutnik, background="dodger blue", foreground= "light goldenrod",
                                      font="Arial 12 bold", bd= 4, text= "START", command=self.start_odliczanie)
        self.button_start.place(x= 150, y= 140)

        #label, który wyświetli odliczanie czasu
        self.label_czas = tk.Label(self.minutnik, background= "seashell2", foreground= "red",
                                   font= "Arial 20 bold")
        self.label_czas.place(x= 130, y= 200)

        #przycisk zatrzymuje czas
        self.button_stop = tk.Button(self.minutnik, background="dodger blue", foreground= "light goldenrod",
                                     font= "Arial 12 bold", bd= 4, text= "STOP", command= self.zatrzymaj_odliczanie)
        self.button_stop.place(x= 155, y= 280)

            #informacja czy odliczanie jest aktywne
        self.odliczanie_aktywne = False

        self.dzwiek_plik = "D:\\Projekt\\Ksiazka\\Alarm.wav"

        pygame.mixer.init()

        self.minutnik.mainloop()

    def start_odliczanie(self):

        if not self.odliczanie_aktywne:
            # Pobieramy wartości z spinboxów
            godzina = int(self.godzina.get())

            minuta = int(self.minuta.get())

            sekunda = int(self.sekunda.get())

            # Przeliczamy na sekundy
            czas_w_sekundach = godzina * 3600 + minuta * 60 + sekunda

            # odliczanie aktywne
            self.odliczanie_aktywne = True

            # Uruchamiamy odliczanie
            self.odliczaj_czas(czas_w_sekundach)


    def odliczaj_czas(self, czas_w_sekundach):

        while czas_w_sekundach >= 0 and self.odliczanie_aktywne:
                # Przeliczamy pozostały czas na godziny, minuty i sekundy
            pozostałe_godziny, reszta = divmod(czas_w_sekundach, 3600)

            pozostałe_minuty, pozostałe_sekundy = divmod(reszta, 60)

                # Aktualizujemy label z czasem
            czas_str = f"{pozostałe_godziny:02d}:{pozostałe_minuty:02d}:{pozostałe_sekundy:02d}"

            self.label_czas.config(text=czas_str)

            self.minutnik.update()

                # Odczekujemy jedną sekundę
            self.minutnik.after(1000)

                # Zmniejszamy liczbę sekund
            czas_w_sekundach -= 1

        if  self.odliczanie_aktywne:

            # Po zakończeniu odliczania ustawiamy na labelu "Czas!" lub inną informację
            self.label_czas.config(text="CZAS!")

        #odtwarzamy dzwiek
            pygame.mixer.music.load(self.dzwiek_plik)

            pygame.mixer.music.play()

        #ustawiamy odliczanie nieaktywne
            self.odliczanie_aktywne = False

    def zatrzymaj_odliczanie(self):

        #pygame.mixer.music.stop()

        self.odliczanie_aktywne = False

if __name__ == "__main__":
    minutnik = Minutnik()


#wersja angielska

class MinutnikE:

    def __init__(self):
        self.minutnik = tk.Tk()

        self.minutnik.title("TIMER")

        self.minutnik.geometry("400x400+500+300")

        self.minutnik.resizable(0, 0)

        self.minutnik.configure(background="seashell2")


        funkcje = '''Choose the time to measure and click "Start"
    H- hours  M- minutes  S- seconds'''

        self.label_funkcje = tk.Label(self.minutnik, background="seashell2", foreground="Black",
                                      font="Arial 12 bold", text=funkcje)
        self.label_funkcje.place(x=30, y=10)


        self.label_HMS = tk.Label(self.minutnik, background="seashell2", foreground="red",
                                  font="Arial 12 bold underline", text="H           M           S")
        self.label_HMS.place(x=120, y=70)


        spin_values_H = ("0", "1", "2", "3", "4", "5", "6")
        spin_values_S = ("0", "10", "20", "30", "40", "50")

        self.godzina = tk.Spinbox(self.minutnik, values=spin_values_H, width=3, bd=2, font="Arial 12")
        self.godzina.place(x=110, y=100)

        self.minuta = tk.Spinbox(self.minutnik, from_=0, to=59, width=3, bd=2, font="Arial 12")
        self.minuta.place(x=170, y=100)

        self.sekunda = tk.Spinbox(self.minutnik, values=spin_values_S, width=3, bd=2, font="Arial 12")
        self.sekunda.place(x=230, y=100)


        self.button_start = tk.Button(self.minutnik, background="dodger blue", foreground="light goldenrod",
                                      font="Arial 12 bold", bd=4, text="START", command=self.start_odliczanie)
        self.button_start.place(x=150, y=140)


        self.label_czas = tk.Label(self.minutnik, background="seashell2", foreground="red", font="Arial 20 bold")
        self.label_czas.place(x=130, y=200)


        self.button_stop = tk.Button(self.minutnik, background="dodger blue", foreground="light goldenrod",
                                     font="Arial 12 bold", bd=4, text="STOP", command=self.zatrzymaj_odliczanie)
        self.button_stop.place(x=155, y=280)


        self.odliczanie_aktywne = False

        self.dzwiek_plik = "C:\\Users\\trapi\\Documents\\Ksiazka\\Alarm.wav"

        pygame.mixer.init()

        self.minutnik.mainloop()


    def start_odliczanie(self):

        if not self.odliczanie_aktywne:

            godzina = int(self.godzina.get())

            minuta = int(self.minuta.get())

            sekunda = int(self.sekunda.get())

            czas_w_sekundach = godzina * 3600 + minuta * 60 + sekunda

            self.odliczanie_aktywne = True

            self.odliczaj_czas(czas_w_sekundach)


    def odliczaj_czas(self, czas_w_sekundach):

        while czas_w_sekundach >= 0 and self.odliczanie_aktywne:

            pozostałe_godziny, reszta = divmod(czas_w_sekundach, 3600)

            pozostałe_minuty, pozostałe_sekundy = divmod(reszta, 60)

            czas_str = f"{pozostałe_godziny:02d}:{pozostałe_minuty:02d}:{pozostałe_sekundy:02d}"

            self.label_czas.config(text=czas_str)

            self.minutnik.update()

            self.minutnik.after(1000)

            czas_w_sekundach -= 1

        if  self.odliczanie_aktywne:

            self.label_czas.config(text="TIME!")

            pygame.mixer.music.load(self.dzwiek_plik)

            pygame.mixer.music.play()

            self.odliczanie_aktywne = False


    def zatrzymaj_odliczanie(self):

        self.odliczanie_aktywne = False

if __name__ == "__main__":
    minutnik = Minutnik()