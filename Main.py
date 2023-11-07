import tkinter as tk
import pygame
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from tkinter import ttk
import Intro
import Ending_1


def mainMenu():
    global Spielername
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
        # Blende den Button nach dem Klicken aus
        StartButton.place_forget()
        # Starte die "explore" Funktion aus der Erkunden Datei
        pygame.mixer.music.stop()
        Intro.Intro(root, content_frame)  # Stellen Sie sicher, dass Intro und content_frame definiert sind
    
    # Startbutton erstellen, der zuerst deaktiviert ist
    StartButton = tk.Button(root, text="START GAME", font=("Times New Roman", 16), command=StartButtonClicked)
    StartButton.place(x=550, y=650)

    # Tkinter-Fenster ausführen 
    root.mainloop()
if __name__ == "__main__":
    mainMenu()
