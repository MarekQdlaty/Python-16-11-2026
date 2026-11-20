import tkinter as tk
from tkinter import filedialog


def wybierz_plik():
    plik = filedialog.askopenfilename(title="Wybierz plik")

    if plik:
        print("Wybrano plik:", plik)
        # Wybrano plik: C:/Users/cscomarch/Documents/dane.txt


root = tk.Tk()
root.withdraw()  # zamyka głowne okno

wybierz_plik()
