import tkinter as tk
import os
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showerror
from tkinter import filedialog
import shutil


class Dodaj:

    # ustawienie okna do dodawania i zapisywania przepisu
    def __init__(self):

        self.lista_skladnikow = []   # pusta lista do inicjalizacji dodania składnika

        self.dodanie = tk.Tk()

        self.dodanie.title("DODAJ PRZEPIS")

        self.dodanie.geometry("600x915+700+20")

        self.dodanie.resizable(0, 0)

        self.dodanie.configure(background= "light steel blue")


        # ustawienie naglowka okna
        self.label_naglowek_okna = tk.Label(self.dodanie,text= "Dodaj przepis:", font="Arial 20 bold underline",
                               foreground= "DarkOrchid4", background="light steel blue")
        self.label_naglowek_okna.place(x=220, y=5)


            # opis funkcji jak zapisac przepis
        text_label = '''    1. W lewym oknie wpisz nazwę pliku, używaj _ zamiast spacji!
    2. W drugim oknie wyboru wybierz kategorię, w której zapisać'''

        self.label_tekst_zapisu = tk.Label(self.dodanie, text= text_label ,
                               background="light steel blue", foreground= "gray12", font= "Arial 12", justify=tk.LEFT)
        self.label_tekst_zapisu.place(x=20, y=45)


             # okno do wpisania nazwy przepisu
        self.nazwa_pliku = tk.Entry(self.dodanie, font="Arial 12", width=35)
        self.nazwa_pliku.place(x=30, y=90)


        self.n = tk.StringVar()  #okno wyboru folderu zapisu

            # utworzenie listy rozwijalnej
        self.opcje_zapisu = ttk.Combobox(self.dodanie, width= 15, textvariable= self.n, font="Arial 12")

        self.opcje_zapisu['values'] = ('Ciasta', 'Inne', 'Miesne', 'Nalesniki',
                                'Pierogi', 'Ryby', 'Salatki', 'Slodycze', 'Zapiekanki', 'Zupy')

        self.opcje_zapisu.current()
        self.opcje_zapisu.place(x=360, y=90)



                # instrukcja wpisania produktu
        opis = '''    1. Wpisz nazwę składnika w pierwszym polu tesktowym         
    2. Wybierz potrzebną ilość wpisanego składnika w środkowej opcji wyboru
    3. Wybierz miarę produktu z listy rozwijalnej
    4. Kliknij "Dodaj" by dodać kolejny składnik
    5. Kliknij "Usuń" jeśli widzisz błąd w ostatnim dodanym składniku
    6. Kliknij "Opis" by dodać instrukcję do przepisu'''

        self.label_opis = tk.Label(self.dodanie, background="light steel blue", foreground="gray5", font="Arial 12",
                                   text=opis, justify=tk.LEFT)
        self.label_opis.place(x=20, y=110)


             # pole do wpisania nazwy składnika
        self.skladnik = tk.Entry(self.dodanie, font= "Arial 12", width= 30)
        self.skladnik.place(x=30, y=230)


            # dodanie ilosci do skladnika
        spin_values = ("0", "0.1", "0.15", "0.2", "0.25", "0.3", "0.4", "0.5", "0.6", "0.75",
                       "1.0", "1.25","1.5", "1.75", "2.0", "2.25", "2.5", "2.75", "3.0", "3.5",
                       "4.0", "4.5", "5.0", "6.0", "7.0", "8.0", "9.0", "10.0", "11.0", "12.0", "20", "25",
                       "30", "35", "40", "50", "60", "70", "80", "90", "100", "125", "150", "200", "250",
                       "300", "350", "400", "450", "500", "550", "600", "650", "700", "750", "800", "850", "900")

        self.skladnik_ilosc = tk.Spinbox(self.dodanie, values= spin_values, width= 5, bd= 2, font=" Arial 12")
        self.skladnik_ilosc.place(x=317, y=230)


             # utworzenie listy rozwijalnej miary
        self.k = tk.StringVar()

        self.miary = ttk.Combobox(self.dodanie, width=10, textvariable=self.k, font="Arial 12")

        self.miary['values'] = ('Kg/y', 'Gram/y', 'Dag/y', 'Litr/y', 'Puszka/i', 'Ml/y', 'Łyżka/i', 'słoik/i',
                                 'Łyżeczka/i', 'Sztuk/i/a', 'Szklanka/i', 'Kostka/i', 'Szczypta/y', 'Opakowanie/a')
        self.miary.current(0)

        self.miary.place(x=395, y=230)


            # przycisk dodaj
        self.button_dodawanie = tk.Button(self.dodanie, background= "lawn green", foreground="gray20", font="Arial 12",
                                      text= "DODAJ", command= self.add_dodawanie, bd = 3)
        self.button_dodawanie.place(x=50, y=260)


            # przycisk usun
        self.button_usun_skl = tk.Button(self.dodanie, background="orange3", foreground= "gray20",
                                        font="Arial 12", text= "USUŃ", command= self.minus, bd = 3)
        self.button_usun_skl.place(x=130, y=260)


            #opis krokow przycisk
        self.button_opis = tk.Button(self.dodanie, background= "gold", foreground= "black",
                                     font= "Arial 12", text= "OPIS", bd= 3, command= self.otworz_opis)
        self.button_opis.place(x = 200, y = 260)


            # pole wyświetli dodane składniki
        self.text_skladniki = tk.Text(self.dodanie, state= tk.DISABLED, background= "gray64",
                                      height= 10, width= 35)
        self.text_skladniki.place(x= 15, y= 305)

        scrollbar_texty = tk.Scrollbar(self.dodanie, command= self.text_skladniki.yview)

        scrollbar_texty.place_configure( x = 299, y = 305, width = 14, height = 162)

        self.text_skladniki.config(yscrollcommand= scrollbar_texty.set)


        #zmienna przechowuje zdjecie do czasu zapisu
        self.zdjecie = None

        #tworzymy możliwość dodania zdjęcia do przepisu
        self.button_zdjecie = tk.Button(self.dodanie, background= "PaleGreen4", foreground= "yellow", font= "Arial 13",
                                 text= "ZDJĘCIE", bd= 5, width= 8, height= 2, command=self.dodaj_zdjecie)
        self.button_zdjecie.place(x= 390, y= 280)


            #label informacyjny
        self.label_zdjecie = tk.Label(self.dodanie, background="light steel blue", foreground= "black",
                        font= "Arial 12", text= "Możesz dodać zdjęcie")
        self.label_zdjecie.place(x= 360, y= 345)


        self.label_zdjecie_uwaga = tk.Label(self.dodanie, background="Light steel blue", foreground= "red",
                                            font= "Arial 12 bold", text= "Musi mieć tą samą nazwę co przepis!")
        self.label_zdjecie_uwaga.place(x=313, y= 370)

            #tworzymy text do podglądu opisu przepisu przed zapisaniem wraz ze scrollbarem
        self.text_przepis = tk.Text(self.dodanie, height=23, width=82, font="Arial 10",
                                    background= "gray64", state= tk.DISABLED)
        self.text_przepis.place(x=6, y=480)

        scrollbary = tk.Scrollbar(self.dodanie, command= self.text_przepis.yview)

        scrollbary.place_configure(x= 581, y= 480, height= 370)

        scrollbarx = tk.Scrollbar(self.dodanie, command= self.text_przepis.xview, orient="horizontal")

        scrollbarx.place_configure(x=6, y=850, width=580)

        self.text_przepis.config(yscrollcommand=scrollbary.set)

        self.text_przepis.config(xscrollcommand=scrollbarx.set)


            # przycisk edytuj
        self.button_edytuj = tk.Button(self.dodanie, background= "tomato", foreground= "gray5",
                                       text= "EDYTUJ", font= "Arial 12", command= self.edytowany_opis)
        self.button_edytuj.place(x=235, y= 872)


            # przycisk zapisz przepis
        self.button_zapisz = tk.Button(self.dodanie, background= "snow4", foreground="gray15",
                                 font="Arial 12", text="ZAPISZ", command= self.zapisz)
        self.button_zapisz.place(x=320, y=872)


        self.dodanie.mainloop()


        # metoda dodaje do textbox skladnik i czyści wybrane wartości, funkcja get pobiera wartości
    def add_dodawanie(self):

        skladnik = self.skladnik.get()

        wartosc = self.skladnik_ilosc.get()

        miara = self.miary.get()


            # jeśli są wszystkie wartości podane to dodajemy do listy pobrane wartości
        if skladnik and wartosc and miara:

            self.lista_skladnikow.append(f"{wartosc} {miara}   {skladnik}")  #dodanie do listy

            text=  "\n".join(self.lista_skladnikow)    #dodanie do zmiennej tymczasowej text

            self.text_skladniki.config(state=tk.NORMAL, background= "white")  #ustawienie pola text

            self.text_skladniki.delete(1.0, tk.END)   #usuwa wartość pierwszą z listy w nowej linii

            self.text_skladniki.insert(tk.END, text)     #wyśweitla dodany składnik

            self.text_skladniki.config(state=tk.DISABLED)

        self.skladnik.delete(0, tk.END)     #po dodaniu czyści pola wyboru

        self.skladnik_ilosc.delete(0, tk.END)


        # metoda usuwa skladnik
    def minus(self):


        # jeśli lista nie jest pusta
        if self.lista_skladnikow:

            removed_skladnik = self.lista_skladnikow.pop()

            current_text = self.text_skladniki.get("1.0", tk.END)

            updated_text = current_text.replace(f"{removed_skladnik}\n", "", 1)   #usuwa ostatni składnik

            self.text_skladniki.config(state= tk.NORMAL)

            self.text_skladniki.delete("1.0", tk.END)

            self.text_skladniki.insert(tk.END, updated_text)    #aktualizuje wartość

            self.text_skladniki.config(state= tk.DISABLED)


        #metoda dodajaca zdjęcie
    def dodaj_zdjecie(self):

        #pobieramy plik
        nazwa_pliku = self.nazwa_pliku.get()

            #sprawdzamy czy jest podana nazwa w polu entry
        if not nazwa_pliku:

            messagebox.showwarning("Brak nazwy pliku", "Wprowadź nazwę przed dodaniem zdjęcia!")

            return

            #otwieramy możliwość wyboru zdjęcia z dysku
        try:
            file_path = filedialog.askopenfilename(title="Wybierz zdjęcie",
                                                   filetypes=[("Pliki graficzne", "*.png;*.jpg;*.jpeg")])
                #sprawadzamy czy wybrano plik
            if file_path:

                nazwa_zdjecia = os.path.basename(file_path)

                nazwa_bez_rozszerzenia, rozszerzenie = os.path.splitext(nazwa_zdjecia)


                if nazwa_bez_rozszerzenia == nazwa_pliku:

                    self.zdjecie = file_path

                    messagebox.showinfo("Sukces", "Zdjęcie dodane pomyślnie!")

                else:

                    messagebox.showwarning("Nieprawidłowa nazwa", "Nazwa musi być taka sama jak nazwa pliku!")

            else:

                messagebox.showwarning("Brak pliku", "Nie wybrano pliku zdjęcia!")

        except Exception as e:

            messagebox.showerror("Błąd", f"Wystąpił błąd podcas dodawania zdjęcia: {str(e)}")


        #metoda resetująca text_skladniki i text_przepis do stanu początkowego w metodzie zapisz
    def reset_text(self):

        self.text_skladniki.config(state= tk.NORMAL, background= "gray64")

        self.text_skladniki.delete(1.0, tk.END)

        self.text_skladniki.config(state= tk.DISABLED)

        self.text_przepis.config(state=tk.NORMAL, background="gray64")

        self.text_przepis.delete(1.0, tk.END)

        self.text_przepis.config(state=tk.DISABLED)


        # metoda zapisujaca przepis
    def zapisz(self):

        nazwa = self.nazwa_pliku.get()

        folder = self.opcje_zapisu.get()

        file_path = None  #inicjalizuje file_path jako puste


            # zapis przepisu z nazwa i folderem wybranym przez uzytkownika
        if nazwa and folder:

            file_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka', folder, f'{nazwa}.txt')

            # Sprawdź, czy file_path nie jest puste
            if file_path is not None:

                # Plik o takiej samej nazwie już istnieje
                if os.path.exists(file_path):

                    pytanie = messagebox.askyesno("Plik już istnieje",
                                              "Plik o tej nazwie już istnieje. Czy chcesz go nadpisać?")

                # Użytkownik wybrał anulowanie zapisu i usuwa dane wpisane
                    if not pytanie:

                        self.reset_text()

                        self.nazwa_pliku.delete(0, tk.END)

                        return


                skladniki = self.text_skladniki.get("1.0", tk.END).strip()

                przepis = self.text_przepis.get("1.0", tk.END).strip()

                dane_do_zapisu = f"Skladniki:\n{skladniki}\n\nPrzepis:\n{przepis}"

                #zapisujemy plik
                with open(file_path, "w") as plik:

                    plik.write(dane_do_zapisu)

                    messagebox.showinfo('Informacja', ' Plik został zapisany!')

                 #zapisanie zdjecia

                    if self.zdjecie:


                        nazwa_bez_podkreslnikow = nazwa.replace("_", "")

                        zdjecie_path = os.path.join('C:\\Users\\trapi\\Documents\\Ksiazka\\Obraz',
                                                    f'{nazwa_bez_podkreslnikow}.png')

                        shutil.copyfile(self.zdjecie, zdjecie_path)

                # Wyczyść listę składników po zapisaniu przepisu
                self.lista_skladnikow = []


                self.reset_text()

                self.nazwa_pliku.delete(0, tk.END)



             # wyświetli błąd dla użytkownika
        else:

            messagebox.showerror('Błąd', "Brak nazwy lub folderu zapisu!")


        #metoda wyswietla teskt wpisany przez użytkownika w podglądzie klasy dodaj
    def otworz_opis(self):

        opis_window = Opis(self.text_przepis)

        opis_window.pokaz_opis()


        #dodajemy funkcje edycji opisu tylko gdy wcześniej dodany został opis
    def edytowany_opis(self):

        if not self.text_przepis.get("1.0", tk.END).strip():

            messagebox.showwarning('Brak Instrukcji', "Dodaj najpierw opis do przepisu, by móc go edytować")

            return

        opis_edytuj_window = Opis_edytuj(self.text_przepis)

        opis_edytuj_window.pokaz_opis_edytuj()


    # klasa Opis inicjalizuje okno do wpisania kroków przepisu
class Opis:

    def __init__(self, text_przepis = None):

        self.opis = tk.Toplevel()

        self.opis.title("DODAJ OPIS")

        self.opis.geometry("700x800+700+20")

        self.opis.resizable(0, 0)

        self.opis.configure(background= "LightCyan3")

        self.text_przepis = text_przepis



        inst_uzytkownia = ''' Napisz instrukcję do przepisu w takiej konfiguracji:
    Krok 1 
    instrukcja
    Krok 2 '''

            #informacja dla użytkownika jak ma napisać instrukcję
        self.label_napisz = tk.Label(self.opis, background= "LightCyan3", foreground= "red2",
                                     font= "Arial 12 bold", text= inst_uzytkownia)
        self.label_napisz.place(x= 150, y =10)


        #przycisk zakończ, kończy opis i zamyka okno
        self.button_zakoncz = tk.Button(self.opis, background= "lime green", foreground= "black",
                                        text= "ZAKOŃCZ", font= "Arial 12", bd= 3, command= self.zakoncz)
        self.button_zakoncz.place(x= 320, y= 753)


        #tworzymy textbox do wpisywania
        self.opis_textBox = tk.Text(self.opis, height= 35, width= 75, font= "Arial 12", wrap=tk.NONE)

        self.opis_textBox.place(x= 5, y= 100)

        opis_scrrollbarx = tk.Scrollbar(self.opis, command= self.opis_textBox.xview, orient= "horizontal")

        opis_scrrollbarx.place_configure(x= 6, y= 730, width= 680)

        self.opis_textBox.config(xscrollcommand= opis_scrrollbarx.set)

        opis_scrrollbary = tk.Scrollbar(self.opis, command= self.opis_textBox.yview)

        opis_scrrollbary.place_configure(x = 675, y= 100, width= 18, height= 630)

        self.opis_textBox.config(yscrollcommand= opis_scrrollbary.set)


        self.opis.mainloop()


            #tworzymy metodę, która dodaje przez zamknięciem okna text do podglądu w klasie dodaj
    def zakoncz(self):

        tekst_opisu = self.opis_textBox.get("1.0", tk.END)

        self.text_przepis.config(state=tk.NORMAL, background= "white")

        self.text_przepis.delete(1.0, tk.END)

        self.text_przepis.insert(tk.END, tekst_opisu)

        self.text_przepis.config(state=tk.DISABLED)

        self.opis.destroy()



        #metoda odwolujaca sie do wyswietlenia textu w oknie dodaj
    def pokaz_opis(self):

        self.opis.mainloop()


    # klasa Opis_edytuj inicjalizuje okno do wpisania edycji kroków przepisu
class Opis_edytuj:

    def __init__(self, text_przepis = None):

        self.opis_edytuj = tk.Toplevel()

        self.opis_edytuj.title("EDYTUJ OPIS")

        self.opis_edytuj.geometry("700x800+700+20")

        self.opis_edytuj.resizable(0, 0)

        self.opis_edytuj.configure(background= "LightCyan3")

        self.text_przepis = text_przepis


        inst_uzytkownia = ''' Edytuj opis z zachowaniem poniższej zasady:
    Krok 1 
    instrukcja
    Krok 2 '''

            #informacja dla użytkownika jak ma napisać instrukcję
        self.label_napisz = tk.Label(self.opis_edytuj, background= "LightCyan3", foreground= "red2",
                                     font= "Arial 12 bold", text= inst_uzytkownia)
        self.label_napisz.place(x= 150, y =10)


        #przycisk zakończ, kończy opis i zamyka okno
        self.button_zakoncz = tk.Button(self.opis_edytuj, background= "lime green", foreground= "black",
                                        text= "Zakończ Edycje", font= "Arial 12", bd= 3, command= self.zakoncz_edytuj)
        self.button_zakoncz.place(x= 270, y= 753)


            #pobieramy wartość opsiu z textbox klasy dodaj do edycji
        przypisz_tekst = self.text_przepis.get("1.0", tk.END)


        #tworzymy textbox do wpisywania
        self.opis_textBox = tk.Text(self.opis_edytuj, height= 35, width= 75, font= "Arial 12", wrap=tk.NONE,)

        self.opis_textBox.place(x= 5, y= 100)

        self.opis_textBox.insert(tk.END, przypisz_tekst)   #przypisujemy tekst do wyswietlenia by edytować

        opis_scrrollbarx = tk.Scrollbar(self.opis_edytuj, command= self.opis_textBox.xview, orient= "horizontal")

        opis_scrrollbarx.place_configure(x= 6, y= 730, width= 680)

        self.opis_textBox.config(xscrollcommand= opis_scrrollbarx.set)

        opis_scrrollbary = tk.Scrollbar(self.opis_edytuj, command= self.opis_textBox.yview)

        opis_scrrollbary.place_configure(x = 675, y= 100, width= 18, height= 630)

        self.opis_textBox.config(yscrollcommand= opis_scrrollbary.set)


        self.opis_edytuj.mainloop()


            #tworzymy metodę, która dodaje przez zamknięciem okna text do podglądu w klasie dodaj
    def zakoncz_edytuj(self):

        if self.text_przepis:

            tekst_opisu = self.opis_textBox.get("1.0", tk.END)

            self.text_przepis.config(state=tk.NORMAL, background= "white")

            self.text_przepis.delete(1.0, tk.END)

            self.text_przepis.insert(tk.END, tekst_opisu)

            self.text_przepis.config(state=tk.DISABLED)

            self.opis_edytuj.destroy()


        #metoda odwolujaca sie do wyswietlenia textu w oknie dodaj
    def pokaz_opis_edytuj(self):

        self.opis_edytuj.mainloop()
