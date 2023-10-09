import tkinter as tk
import pygame
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Erkunden import explore

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
        hgLabel.place_forget()
        pygame.mixer.music.stop()
        #Starte die "explore" Funktion aus der Erkunden Datei
        explore(root, content_frame)

    StartButton = tk.Button(root, text="SPIEL STARTEN", font=("Times New Roman", 16),command=StartButtonClicked)
    StartButton.place(x=550, y=670)
    
    hintergrund = Image.open(Veridia)
    tk_image = ImageTk.PhotoImage(hintergrund)
    hgLabel = tk.Label(root, image=tk_image)
    hgLabel.place(x=250, y=100)

    root.mainloop()

if __name__ == "__main__":
    mainMenu()

