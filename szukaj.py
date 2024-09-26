import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
from szukaj2 import*
from szukaj2E import*


class Szukaj:
    def __init__(self):         #utworzenie okna szukaj

        self.szukaj = tk.Tk()

        self.szukaj.title("SZUKAJ")

        self.szukaj.geometry("400x200+700+250")

        self.szukaj.resizable(0, 0)

        self.szukaj.configure(background="MediumPurple1")

        self.wartosc_szukaj = None




            #dodanie nagłowka menu
        opis_menu ='''1. Wybierz folder
            2. Wybierz dostępny przepis '''

        self.label_opis = tk.Label(self.szukaj, background= "MediumPurple1", foreground= "navy",
                            font= "Arial 14 bold", text= opis_menu)
        self.label_opis.place(x= 10, y=5)


        # okno wyboru folderu, tworzenie listy rozwijalnej
        self.s_folder = tk.StringVar()

        self.opcje_folder = ttk.Combobox(self.szukaj, width= 15, textvariable= self.s_folder, font="Arial 13")

        self.opcje_folder['values'] = ('Ciasta', 'Inne', 'Miesne', 'Nalesniki',
                                'Pierogi', 'Ryby', 'Salatki', 'Slodycze', 'Zapiekanki', 'Zupy')


        self.opcje_folder.bind("<<ComboboxSelected>>", self.pobierz_dostepne_przepisy)

        self.opcje_folder.place(x= 120, y=60)

            #opis combobox
        self.label_folder = tk.Label(self.szukaj, background="MediumPurple1", foreground= "black",
                                     font= "Arial 12", text= "Folder:")
        self.label_folder.place(x= 50, y = 60)


        #okno wyboru przepisu, i utworzenie listy rozwijalnej
        self.s_przepis = tk.StringVar()

        self.opcje_przepis = ttk.Combobox(self.szukaj, width= 25, textvariable= self.s_przepis, font= "Arial 13")

        self.opcje_przepis.place(x= 120, y= 100 )


        self.label_przepis = tk.Label(self.szukaj, background= "MediumPurple1", foreground= "black",
                                      font= "Arial 12", text= "Przepis:")
        self.label_przepis.place(x=50, y= 100)


            # utworzenie przycisku wyświetl
        self.button_szukaj = tk.Button(self.szukaj, background= "OliveDrab1", foreground="brown4", font= "Arial 15",
                                       text= "Wyświetl", bd= 5, command= self.wyswietl_przepis)
        self.button_szukaj.place(x =150, y= 140)


        self.szukaj.mainloop()


        # pobiera przepisy
    def pobierz_dostepne_przepisy(self, event):

        selected_folder = self.opcje_folder.get()

        if selected_folder:

            folder_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', selected_folder)

            if os.path.exists(folder_path):

                dostepne_przepisy = [file.replace('.txt',
                                                  '') for file in os.listdir(folder_path) if file.endswith('.txt')]

                self.opcje_przepis['values'] = dostepne_przepisy

                self.opcje_przepis.set('')

            else:

                self.opcje_przepis['values'] = ()

        else:

            self.opcje_przepis['values'] = ()


    def wyswietl_przepis(self):

        wybrany_przepis = self.opcje_przepis.get()     #pobieramy wartości do szukania

        selected_folder = self.opcje_folder.get()


            # sprawdzamy czy wartości są podane i odwołujemy się do nich
        if wybrany_przepis and selected_folder:

            file_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', selected_folder, f'{wybrany_przepis}.txt')

            if file_path is not None:  #jeśli dane nie są puste

                # plik o takiej nazwie istnieje oraz odczytujemy okno klasy Przepis i zawartość pliku z klasy przepis
                if os.path.exists(file_path):

                    self.wartosc_szukaj = wybrany_przepis.upper().replace("_", " ")

                    przepis_window = Przepis(file_path, self)


                else:              #plik nie istnieje

                    messagebox.showinfo('Ostrzeżenie', f'Brak pliku o nazwie {wybrany_przepis}.txt',
                                        icon=messagebox.WARNING)

        else:       #brak kompletnych danych

            messagebox.showerror('Błąd', "Wybierz nazwę przepisu i folder z listy!")


    #wersja angielska
class SzukajE:

    def __init__(self):         #utworzenie okna szukaj

        self.szukaj = tk.Tk()

        self.szukaj.title("SEARCH")

        self.szukaj.geometry("400x200+700+250")

        self.szukaj.resizable(0, 0)

        self.szukaj.configure(background="MediumPurple1")

        self.wartosc_szukaj = None


            #dodanie nagłowka menu
        opis_menu ='''1. Choose folder
            2. Choose an available recipe '''

        self.label_opis = tk.Label(self.szukaj, background= "MediumPurple1", foreground= "navy",
                            font= "Arial 14 bold", text= opis_menu)
        self.label_opis.place(x= 10, y=5)


        # okno wyboru folderu, tworzenie listy rozwijalnej
        self.s_folder = tk.StringVar()

        self.opcje_folder = ttk.Combobox(self.szukaj, width= 15, textvariable= self.s_folder, font="Arial 13")

        self.opcje_folder['values'] = ('Cakes', 'Other', 'Meat', 'Pancakes',
                                            'Pierogi', 'Fish', 'Salads', 'Sweets', 'Casseroles', 'Soups')


        self.opcje_folder.bind("<<ComboboxSelected>>", self.pobierz_dostepne_przepisy)

        self.opcje_folder.place(x= 120, y=60)

        self.label_folder = tk.Label(self.szukaj, background="MediumPurple1", foreground= "black",
                                     font= "Arial 12", text= "Folder:")
        self.label_folder.place(x= 50, y = 60)

        #okno wyboru przepisu, i utworzenie listy rozwijalnej
        self.s_przepis = tk.StringVar()

        self.opcje_przepis = ttk.Combobox(self.szukaj, width= 25, textvariable= self.s_przepis, font= "Arial 13")

        self.opcje_przepis.place(x= 120, y= 100 )


        self.label_przepis = tk.Label(self.szukaj, background= "MediumPurple1", foreground= "black",
                                      font= "Arial 12", text= "Recipe:")
        self.label_przepis.place(x=50, y= 100)


            # utworzenie przycisku wyświetl
        self.button_szukaj = tk.Button(self.szukaj, background= "OliveDrab1", foreground="brown4", font= "Arial 15",
                                       text= "SHOW", bd= 5, command= self.wyswietl_przepis)
        self.button_szukaj.place(x =150, y= 140)


        self.szukaj.mainloop()


        # pobiera przepisy
    def pobierz_dostepne_przepisy(self, event):

        selected_folder = self.opcje_folder.get()

        if selected_folder:

            folder_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', selected_folder)

            if os.path.exists(folder_path):

                dostepne_przepisy = [file.replace('.txt',
                                                  '') for file in os.listdir(folder_path) if file.endswith('.txt')]

                self.opcje_przepis['values'] = dostepne_przepisy

                self.opcje_przepis.set('')

            else:

                self.opcje_przepis['values'] = ()

        else:

            self.opcje_przepis['values'] = ()


    def wyswietl_przepis(self):

        wybrany_przepis = self.opcje_przepis.get()     #pobieramy wartości do szukania

        selected_folder = self.opcje_folder.get()


            # sprawdzamy czy wartości są podane i odwołujemy się do nich
        if wybrany_przepis and selected_folder:

            file_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', selected_folder, f'{wybrany_przepis}.txt')

            if file_path is not None:  #jeśli dane nie są puste

                # plik o takiej nazwie istnieje oraz odczytujemy okno klasy Przepis i zawartość pliku z klasy przepis
                if os.path.exists(file_path):

                    self.wartosc_szukaj = wybrany_przepis.upper().replace("_", " ")

                    przepis_window = PrzepisE(file_path, self)

                else:              #plik nie istnieje

                    messagebox.showinfo('Warning', f'No file with the name {wybrany_przepis}.txt',
                                        icon=messagebox.WARNING)

        else:       #brak kompletnych danych

            messagebox.showerror('Error', "Select the recipe name and folder from the list!")
