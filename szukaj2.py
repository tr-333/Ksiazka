import tkinter as tk
import os
from tkinter import ttk
from szukaj import*
from PIL import Image, ImageTk
from tkinter import messagebox




class Przepis:

    def __init__(self, file_path = None, szukaj_instance = None):

        self.przepis = tk.Toplevel()          #utworzenie okna

        self.przepis.title("Przepis")

        self.przepis.geometry("700x900+700+50")

        self.przepis.resizable(0, 0)

        self.przepis.configure(background="LightBlue1")


            #sprawdza czy są wartości i wyświetla nagłówek
        if szukaj_instance and szukaj_instance.wartosc_szukaj is not None:

               # utworzenie nagłowka
            self.label_tytul = tk.Label(self.przepis, background="LightBlue1", foreground= "red", anchor = tk.CENTER,
                                    font= "Arial 15 bold", text= f"{szukaj_instance.wartosc_szukaj} :")
            self.label_tytul.pack()



               # Pobranie nazwy z label_tytul, zmniejszenie liter na małe
            nazwa_przepisu = self.label_tytul.cget("text").lower()

               # Usunięcie potencjalnych nieprawidłowych znaków z nazwy przepisu
            nazwa_przepisu = ''.join(c for c in nazwa_przepisu if c.isalnum() or c in ['_', '-'])


            sciezka_do_obrazu = None

            try:

                #odczytujemy sciezke do pliku z pobrana nazwa
                sciezka_do_obrazu = f'C:\\Users\\trapi\\Documents\\Ksiazka\\Obraz\\{nazwa_przepisu}.png'

                   # Wczytaj obraz za pomocą PIL (Pillow)
                obraz = Image.open(sciezka_do_obrazu)

                   # Skaluj obraz, jeśli to konieczne
                obraz = obraz.resize((300, 300), Image.ANTIALIAS)

                   # Przekształć go na format zrozumiały przez Tkinter
                obraz_tk = ImageTk.PhotoImage(obraz)


                   # Dodaj obraz do interfejsu graficznego
                self.obraz_label = tk.Label(self.przepis, image=obraz_tk, relief=tk.SOLID, bd=3)

                self.obraz_label.image = obraz_tk  # Zachowaj referencję do obiektu, aby uniknąć wycieku pamięci

                self.obraz_label.place(x= 355, y= 45)

            except FileNotFoundError:

                    #jesli nie ma obrazu to wyswietl label z napisem brak zdjecia
                self.obraz_label = tk.Label(self.przepis, text="BRAK ZDJECIA", background="gray80", relief=tk.SOLID,
                                            bd= 3, foreground="black", height= 19, width= 40)

                self.obraz_label.place(x = 355, y= 45)

                print(f"Nie znaleziono pliku obrazu: {sciezka_do_obrazu}")

            except Exception as e:

                 # jesli wystapil jakis blad podczas ladowania wyswietl napis brak zdjecia oraz stosowna inf w konsoli
                self.obraz_label = tk.Label(self.przepis, text="BRAK ZDJECIA", background="gray80", relief=tk.SOLID,
                                            bd= 3, foreground="black", height= 19, width= 40)

                self.obraz_label.place(x= 355, y= 45)

                print(f"Wystąpił błąd podczas wczytywania obrazu: {e}")


            # nagłówek skladnik
        self.label_sklad = tk.Label(self.przepis, background= "LightBlue1", foreground= "blue",
                                        font= "Arial 13 bold underline", text= "SKŁADNIKI:")
        self.label_sklad.place(x= 15, y = 30)


            # wyswietla dane z pliku
        self.text_sklad_user = tk.Text(self.przepis, background= "Light Blue1", foreground= "black", font= "Arial 12",
                                       state= tk.NORMAL, height= 14, width= 35, bd= 3)
        self.text_sklad_user.place(x= 15, y= 60)

        #ustawiamy interlinie oraz scrollbar
        self.text_sklad_user.tag_configure("interline", spacing3=7)

        scrollbarx_sklad = tk.Scrollbar(self.przepis, command= self.text_sklad_user.xview, orient="horizontal")

        scrollbarx_sklad.place_configure(x= 15, y= 305, width= 310)

        self.text_sklad_user.config(xscrollcommand= scrollbarx_sklad.set)

        scrollbary_sklad = tk.Scrollbar(self.przepis, command= self.text_sklad_user.yview)

        scrollbary_sklad.place_configure(x= 326, y = 60, height= 260)

        self.text_sklad_user.config(yscrollcommand= scrollbary_sklad.set)


            # nagłowek instrukcji
        self.label_kroki = tk.Label(self.przepis, background= "LightBlue1", foreground= "blue",
                                         font= "Arial 13 bold underline", text= "INSTRUKCJA:")
        self.label_kroki.place( x= 15, y= 320)



        self.text_kroki_user = tk.Text(self.przepis, background= "LightBlue1", foreground= "black", font= "Arial 12",
                                       state= tk.NORMAL, bd= 3, height= 29, width= 73)
        self.text_kroki_user.place(x= 15, y= 350)

            #ustawiamy interlinię oraz scrollbar
        self.text_kroki_user.tag_configure("interline", spacing3=8)

        scrollbarx_kroki = tk.Scrollbar(self.przepis, command= self.text_kroki_user.xview, orient="horizontal")

        scrollbarx_kroki.place_configure(x= 15, y= 873, width= 654)

        self.text_kroki_user.config(xscrollcommand= scrollbarx_kroki.set)

        scrollbary_kroki = tk.Scrollbar(self.przepis, command= self.text_kroki_user.yview)

        scrollbary_kroki.place_configure(x= 669, y = 350, height= 530)

        self.text_kroki_user.config(yscrollcommand= scrollbary_kroki.set)



        if file_path:

            self.odczyt(file_path)


        self.przepis.mainloop()


    def odczyt(self, file_path):          #odczyt wybranego pliku przez uzytkownika

        with open(file_path, "r") as file:


            lines = file.readlines()    #odczytujemy po linii

            skladniki_found = False    #ustalamy do znalezienia słowa klucz

            kroki_found = False

            skladniki_text = " "

            kroki_text = " "


            for line in lines:

                if line.startswith("Skladniki:"):

                    skladniki_found = True

                    kroki_found = False

                elif line.startswith("Przepis:"):

                    skladniki_found = False

                    kroki_found = True

                elif skladniki_found:
                    skladniki_text += line.strip() + "\n"

                elif kroki_found:

                    kroki_text += line.strip() + "\n"


                # usuwanie zbędnych pustych linii
            skladniki_text = "\n".join([line.strip() for line in skladniki_text.split('\n') if line.strip()])

            kroki_text = "\n".join([line.strip() for line in kroki_text.split('\n') if line.strip()])

                #dostosowanie d wyświetlenia danych
            skladniki_lines = skladniki_text.split('\n')

            #pętla dostosowująca interlinie między wczytywanymi liniami
            for line in skladniki_lines:

                self.text_sklad_user.insert("end", line + "\n", "interline")

            self.text_sklad_user.config(state= tk.DISABLED)


            kroki_lines = kroki_text.split('\n')


            for line in kroki_lines:

                # Pogrubianie słów kluczowych w instrukcji (Krok 1, Krok 2, itd.)
                if line.startswith("Krok"):

                    #ustawiamy pogrubienie słów kroki
                    self.text_kroki_user.tag_configure("bold", font=("Arial", 12, "bold"), foreground= "DarkOrange3")

                    krok_numer = line.split(" ", 1)[0]

                    self.text_kroki_user.insert("end",f"{krok_numer} {line.replace(krok_numer, '', 1)}\n", "bold")

                else:

                    self.text_kroki_user.insert("end", line + "\n", "interline")

            self.text_kroki_user.config(state= tk.DISABLED)








