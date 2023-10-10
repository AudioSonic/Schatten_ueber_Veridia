import tkinter as tk
import pygame
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Erkunden import explore
from Fight import Fight

def mainMenu():
    root = tk.Tk()
    root.title("Main")
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
        FightButton.place_forget() 
        #Starte die "explore" Funktion aus der Erkunden Datei
        explore(root, content_frame)
       
    def FightButtonClicked():
        # Blende den Button nach dem Klicken aus
        FightButton.place_forget() 
        StartButton.place_forget() 
        #Starte die "explore" Funktion aus der Erkunden Datei
        Fight(root, content_frame)

    StartButton = tk.Button(root, text="SPIEL STARTEN", font=("Times New Roman", 16),command=StartButtonClicked)
    StartButton.place(x=550, y=670)
    
    FightButton = tk.Button(root, text="Fight", font=("Times New Roman", 16),command=FightButtonClicked)
    FightButton.place(x=550, y=500)

    root.mainloop()

if __name__ == "__main__":
    mainMenu()

