import tkinter as tk
import pygame
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from tkinter import ttk
import Intro
import Ending_1


def mainMenu():
    root = tk.Tk()
    root.title("Schatten ueber Veridia")
    root.geometry("1300x750")
    root.resizable(False, False)
    root.configure(bg="#6B6B6B")
    root.attributes("-fullscreen", False)
    pygame.init()
    
    pygame.mixer.music.load("C:\GitHub\Schatten_ueber_Veridia\Audio\MainMenu.mp3")
    pygame.mixer.music.play(-1)
    
    # Erstelle ein Frame, um den Inhalt der explore-Funktion anzuzeigen
    content_frame = tk.Frame(root, bg="#6B6B6B")
    content_frame.pack(fill=tk.BOTH, expand=True)

    def StartButtonClicked():
        global Spielername  # Verwenden Sie 'global', um die globale Variable zu aktualisieren
        Spielername = Eingabe.get()  # Setze den Spielernamen
        # Blende den Button nach dem Klicken aus
        StartButton.place_forget()
        NameText.place_forget()
        Eingabe.place_forget()
        # Starte die "explore" Funktion aus der Erkunden Datei
        pygame.mixer.music.stop()
        Intro.Intro(root, content_frame)  # Stellen Sie sicher, dass Intro und content_frame definiert sind

    # Eingabefeld und Label erstellen
    NameText = tk.Label(text="ENTER YOUR NAME", bg="#6B6B6B", font=("Times New Roman", 12))
    NameText.place(x=545, y=570)
    Eingabe = tk.Entry()
    Eingabe.place(x=560, y=600)
    
    # Startbutton erstellen, der zuerst deaktiviert ist
    StartButton = tk.Button(root, text="START GAME", font=("Times New Roman", 16), command=StartButtonClicked)
    StartButton.place(x=550, y=650)
    StartButton.config(state="disabled")

    # Funktion zum Überprüfen des Eingabefelds
    def check_input():
        Spielername = Eingabe.get()
        if Spielername == "":
            StartButton.config(state="disabled")
        else:
            StartButton.config(state="active")
        return Spielername  # Den eingegebenen Spielernamen zurückgeben

    # Eingabefeld-Bindung hinzufügen, um bei Eingabe zu prüfen
    Eingabe.bind("<KeyRelease>", lambda event: check_input())
    
    # Tkinter-Fenster ausführen
    root.mainloop()
    
if __name__ == "__main__":
    Spielername = mainMenu()
