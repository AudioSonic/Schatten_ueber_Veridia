import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *

def explore():  
    root = tk.Tk()
    root.title("Main")
    root.geometry("1300x750")
    root.resizable(False, False)
    root.configure(bg="#6B6B6B")
    root.attributes("-fullscreen", False)

    # Erstellen Sie einen Stil für das Widget
    style = ttk.Style()

    # Ändern Sie die Schriftart im Stil
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  # Hier wird die Schriftart auf Helvetica mit Größe 14 gesetzt

    # Hintergrundbild einfügen
    bg_pfad = Image.open(Veridia)
    bg_image = ImageTk.PhotoImage(bg_pfad)
    image_label = tk.Label(root, image=bg_image)
    image_label.place(x= 253, y = 18)
    """   
    image = Image.open(Veridia)
    label = ImageTk.PhotoImage(image)    
    image_label = tk.Label(root, image=label)
    image_label.pack()
    """
    #Setzt die Breite der Buttons fest
    button_width = 15
    #Der "Betrachten" Button
    betrButton = ttk.Button(root, text="BETRACHTEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
    betrButton.place(x=130, y=680)

    #Der "Untersuchen" Button
    untButton = ttk.Button(root, text="UNTERSUCHEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
    untButton.place(x=390, y=680)

    #Der "Wahrnehmen" Button
    whrButton = ttk.Button(root, text="WAHRNEHMEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
    whrButton.place(x=650, y=680)

    #Der "Aufheben" Button
    aufhbButton = ttk.Button(root, text="AUFHEBEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
    aufhbButton.place(x=910, y=680)

    #Der links Pfeil
    linksPfeilBild = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\Arrow_Left.png")
    lnkPfeil = ttk.Button(root, image=linksPfeilBild)
    lnkPfeil.place(x=18, y=350)

    #Der rechts Pfeil
    rechtsPfeilBild = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\Arrow_Right.png")
    rchtsPfeil = ttk.Button(root, image=rechtsPfeilBild)
    rchtsPfeil.place(x=1200, y=350)

    #Der front Pfeil
    vorPfeilBild = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\Arrow_Front.png")
    vorPfeil = ttk.Button(root, image=vorPfeilBild)
    vorPfeil.place(x=600, y=20)

    #Der return Pfeil
    returnPfeilBild = Image.open("C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\Arrow_Return.png")
    photo = ImageTk.PhotoImage(returnPfeilBild)
    returnPfeil = ttk.Button(root, image=photo)
    returnPfeil.place(x=20, y=670)

    #Die Karte
    MapImage = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\Map_Button.png")
    Map = tk.Button(root, image=MapImage)
    Map.place(x=1250, y=20)

    # Textfeld für die Ausgabe

    text_output = tk.Text(root, height=6, width=90, wrap="none")
    text_output.place(x = 18, y = 470)
    text_output.config(state=tk.DISABLED)  # Sperrt das Textfeld


    #Einfügen und ändern des Lauftext

    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, "A\nB\nC\nD\nF\nG")
    text_output.config(state=tk.DISABLED)      

    custom_font = ("Times New Roman", 20)
    text_output.config(font=custom_font)

    """
    #Funktion um Text zu Ändern im TextBlock
    def update_text():
        new_text = entry.get()
        text_output.config(state=tk.NORMAL)  # Aktiviert das Textfeld für Änderungen
        text_output.delete("1.0", tk.END)    # Löscht den aktuellen Text im Textfeld
        text_output.insert(tk.END, new_text)  # Fügt den neuen Text hinzu
        text_output.config(state=tk.DISABLED)  # Sperrt das Textfeld wieder
     """
    return root
    root.mainloop()



explore()