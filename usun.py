import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror
from tkinter import simpledialog

class Usun:

    def __init__(self):         #utworzenie okna usun

        self.usun = tk.Tk()

        self.usun.title("USUŃ")

        self.usun.geometry("400x250+700+250")

        self.usun.resizable(0, 0)

        self.usun.configure(background="dark sea green")


             # teskst
        opis_label = '''1. Wybierz folder
        2. Wybierz przepis do usunięcia'''

        self.label_opis = tk.Label(self.usun,background= "dark sea green", foreground= "red4", font= "Arial 14 bold",
                                   text= opis_label)
        self.label_opis.place(x= 25, y=5)


            # okno wyboru folderu do usunięcia oraz utworzenie listy rozwijalnej
        self.u_folder = tk.StringVar()

        self.opcje_folder_usun = ttk.Combobox(self.usun, width= 15, textvariable= self.u_folder, font="Arial 13")

        self.opcje_folder_usun['values'] = ('Ciasta', 'Inne', 'Miesne', 'Nalesniki',
                                'Pierogi', 'Ryby', 'Salatki', 'Slodycze', 'Zapiekanki', 'Zupy')

        self.opcje_folder_usun.bind("<<ComboboxSelected>>", self.pobierz_dostepne_przepisy_usun)

        self.opcje_folder_usun.place(x= 120, y=60)


        label_folder = tk.Label(self.usun, foreground= "red4", background= "dark sea green", font= "Arial 12",
                                text= "Folder:")
        label_folder.place(x= 50, y= 60)


        #okno wyboru przepisu do usuniecia
        self.u_przepis = tk.StringVar()

        self.opcje_przepis_usun = ttk.Combobox(self.usun, width= 25, textvariable= self.u_przepis, font= "Arial 13")

        self.opcje_przepis_usun.place(x= 120, y= 110)


        label_przepis = tk.Label(self.usun, background= "dark sea green", foreground='red4', font= "Arial 12",
                                 text= "Przepis:")
        label_przepis.place(x=50, y= 110)


                # przycisk usun
        self.button_usun = tk.Button(self.usun, background= "red", foreground= "gray3",
                                     font= "Arial 15", text= "Usuń", bd=5, command= self.usuwa)
        self.button_usun.place(x=130, y= 160)


            # przycisk anuluj
        self.button_anuluj = tk.Button(self.usun, background= "yellow", foreground= "gray3",
                                       font= "Arial 15", text="Anuluj", bd=5, command= self.usun.destroy)
        self.button_anuluj.place(x=210, y=160)


        self.usun.mainloop()

    def pobierz_dostepne_przepisy_usun(self, event):

        selected_folder = self.opcje_folder_usun.get()

        if selected_folder:

            folder_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', selected_folder)

            if os.path.exists(folder_path):

                dostepne_przepisy = [file.replace('.txt',
                                                    '') for file in os.listdir(folder_path) if file.endswith('.txt')]

                self.opcje_przepis_usun['values'] = dostepne_przepisy

                self.opcje_przepis_usun.set('')

            else:

                self.opcje_przepis_usun['values'] = ()

        else:

            self.opcje_przepis_usun['values'] = ()


        # pobieramy wartosci od uzytkownika oraz w przypadku braku info pusty plik
    def usuwa(self):

        usuniecie = self.opcje_przepis_usun.get()

        folder = self.opcje_folder_usun.get()

        file_path = None

            # odwolanie sie do scieżki przepisu z nazwa i folderem wybranym przez uzytkownika
        if usuniecie and folder:

            file_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', folder, f'{usuniecie}.txt')

            if file_path is not None:   # Sprawdź, czy file_path nie jest puste

                if os.path.exists(file_path):     # Plik o takiej samej nazwie już istnieje

                    result = messagebox.askokcancel("Uwaga",
                                    f"Uwaga usuwasz trwale plik {usuniecie}.txt. Czy na pewno chcesz kontynuować?",
                                                    icon=messagebox.WARNING)


                    if result:             #jesli tak usun

                        os.remove(file_path)

                        messagebox.showinfo('Informacja', f'Plik {usuniecie}.txt został usunięty.')

                        self.opcje_przepis_usun.delete(0, tk.END)

                    else:                          #nie, pozostaw

                        self.opcje_przepis_usun.delete(0, tk.END)

                else:      #informacja przy braku znalezienia pliku

                    messagebox.showinfo('Ostrzeżenie', f'Brak pliku o nazwie {usuniecie}.txt',
                                        icon = messagebox.WARNING)

        else:                     #brak podania nazwy lub folderu

            messagebox.showerror('Błąd', "Brak nazwy lub folderu zapisanego pliku!")


    #wersja angielska
class UsunE:

    def __init__(self):  # utworzenie okna usun

        self.usun = tk.Tk()

        self.usun.title("DELETE")

        self.usun.geometry("400x250+700+250")

        self.usun.resizable(0, 0)

        self.usun.configure(background="dark sea green")

        # teskst
        opis_label = '''1. Choose folder
            2. Choose the recipe to delete'''

        self.label_opis = tk.Label(self.usun, background="dark sea green", foreground="red4", font="Arial 14 bold",
                                   text=opis_label)
        self.label_opis.place(x=25, y=5)

        # okno wyboru folderu do usunięcia oraz utworzenie listy rozwijalnej
        self.u_folder = tk.StringVar()

        self.opcje_folder_usun = ttk.Combobox(self.usun, width=15, textvariable=self.u_folder, font="Arial 13")

        self.opcje_folder_usun['values'] = ('Cakes', 'Other', 'Meat', 'Pancakes',
                                            'Pierogi', 'Fish', 'Salads', 'Sweets', 'Casseroles', 'Soups')

        self.opcje_folder_usun.bind("<<ComboboxSelected>>", self.pobierz_dostepne_przepisy_usun)

        self.opcje_folder_usun.place(x=120, y=60)

        label_folder = tk.Label(self.usun, foreground="red4", background="dark sea green", font="Arial 12",
                                text="Folder:")
        label_folder.place(x=50, y=60)

        # okno wyboru przepisu do usuniecia
        self.u_przepis = tk.StringVar()

        self.opcje_przepis_usun = ttk.Combobox(self.usun, width=25, textvariable=self.u_przepis, font="Arial 13")

        self.opcje_przepis_usun.place(x=120, y=110)

        label_przepis = tk.Label(self.usun, background="dark sea green", foreground='red4', font="Arial 12",
                                 text="Recipe:")
        label_przepis.place(x=50, y=110)

        # przycisk usun
        self.button_usun = tk.Button(self.usun, background="red", foreground="gray3",
                                     font="Arial 15", text="DELETE", bd=5, command=self.usuwa)
        self.button_usun.place(x=100, y=160)

        # przycisk anuluj
        self.button_anuluj = tk.Button(self.usun, background="yellow", foreground="gray3",
                                       font="Arial 15", text="CANCEL", bd=5, command=self.usun.destroy)
        self.button_anuluj.place(x=210, y=160)

        self.usun.mainloop()

    def pobierz_dostepne_przepisy_usun(self, event):

        selected_folder = self.opcje_folder_usun.get()

        if selected_folder:

            folder_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', selected_folder)

            if os.path.exists(folder_path):

                dostepne_przepisy = [file.replace('.txt',
                                                  '') for file in os.listdir(folder_path) if file.endswith('.txt')]

                self.opcje_przepis_usun['values'] = dostepne_przepisy

                self.opcje_przepis_usun.set('')

            else:

                self.opcje_przepis_usun['values'] = ()

        else:

            self.opcje_przepis_usun['values'] = ()


        # pobieramy wartosci od uzytkownika oraz w przypadku braku info pusty plik kom
    def usuwa(self):

        usuniecie = self.opcje_przepis_usun.get()

        folder = self.opcje_folder_usun.get()

        file_path = None

            # odwolanie sie do scieki przepisu z nazwa i folderem wybranym przez uzytkownika
        if usuniecie and folder:

            file_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', folder, f'{usuniecie}.txt')


            if file_path is not None:   # Sprawdź, czy file_path nie jest puste

                if os.path.exists(file_path):     # Plik o takiej samej nazwie już istnieje

                    result = messagebox.askokcancel("Attention",
                        f"you are permanently deleting the file {usuniecie}.txt. Are you sure you want to continue?",
                                                    icon=messagebox.WARNING)

                    if result:             #jesli tak usun

                        os.remove(file_path)

                        messagebox.showinfo('Information', f'File {usuniecie}.txt has been deleted.')

                        self.opcje_przepis_usun.delete(0, tk.END)

                    else:                          #nie, pozostaw

                        self.opcje_przepis_usun.delete(0, tk.END)

                else:            #informacja przy braku znalezienia pliku

                    messagebox.showinfo('Warning', f'"File not found {usuniecie}.txt', icon = messagebox.WARNING)

        else:                     #brak podania nazwy lub folderu

            messagebox.showerror('Error', "No filename or saving folder!")

