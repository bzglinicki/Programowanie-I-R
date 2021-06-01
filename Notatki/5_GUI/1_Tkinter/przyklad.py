# Programowanie I R
# Graficzny interfejs użytkownika: Tkinter - przykład

#***********************************************************************************
# Importujemy niezbędne moduły
#***********************************************************************************

# Pakiet Tkinter: podstawowa funkcjonalność
from tkinter import *

# Pakiet Tkinter: współcześnie wyglądające kontrolki
from tkinter.ttk import *

# Pakiet Tkinter: okno MessageBox
from tkinter import messagebox


#***********************************************************************************
# Projektujemy główne okno aplikacji
#***********************************************************************************

# Główne okno aplikacji.
MainForm = Tk()
MainForm.title("Tkinter - przykład")
MainForm.geometry("300x100")

# Kontrolka 1.: etykieta.
lblInfo = Label(MainForm, text = "Wpisz jakiś tekst: ")
lblInfo.grid(column = 0, row = 0)

# Kontrolka 2.: pole do wprowadzania tekstu.
txtText = Entry(MainForm, width = 30)
txtText.grid(column = 1, row = 0)

# Kontrolka 3.: etykieta.
lblTextInfo = Label(MainForm, text = "Wpisany tekst: ")
lblTextInfo.grid(column = 0, row = 1)

# Kontrolka 4.: etykieta.
lblText = Label(MainForm, text = "(brak)")
lblText.grid(column = 1, row = 1)

# Kontrolka 5.: przycisk.
def btnOK_Clicked():   # Metoda wywoływana w chwili kliknięcia przycisku btnOK.
    # Zmieniamy napis na etykiecie lblText.
    # Metoda txtText.get() zwraca tekst wpisany do pola txtText.
    lblText.configure(text = txtText.get())
    
    # Wyświetlamy okno MessageBox.
    messagebox.showinfo("Tkinter - przykład", txtText.get())

btnOK = Button(MainForm, text = "OK", command = btnOK_Clicked)
btnOK.grid(column = 1, row = 2)


#***********************************************************************************
# Przekazujemy "sterowanie" aplikacją do jej okna głównego
#***********************************************************************************

MainForm.mainloop()