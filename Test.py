import tkinter as tk

from tkinter import PhotoImage

from PIL import Image, ImageTk

 

def Kampf():

    global photo_kampf  # Globale Variable, um die Referenz auf das PhotoImage-Objekt zu speichern

 

    # Löschen Sie zuerst den aktuellen Inhalt des Hauptfensters

    for widget in root.winfo_children():

        widget.destroy()

 

    root.title("Urnacht-Wald")

 

    # Laden Sie das Bild und konvertieren Sie es in ein PhotoImage-Objekt

    image = Image.open("C:\GitHub\Schatten_ueber_Veridia\\Bilder\\Monster.png")

    photo_kampf = ImageTk.PhotoImage(image)

 

    label = tk.Label(root, image=photo_kampf)

    label.pack()

 

    MainButton = tk.Button(root, text="Main", command=Main)

    MainButton.pack()

 

def Dialog():

    global photo_dialog

    for widget in root.winfo_children():

        widget.destroy()

 

    root.title("Veridia")

 

    image = Image.open("C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\Miriam_Wiesenhein.png")

    photo_dialog = ImageTk.PhotoImage(image)

 

    label = tk.Label(root, image=photo_dialog)

    label.pack()

 

    MainButton = tk.Button(root, text="Main", command=Main)

    MainButton.pack()

 

def Erkundung():

    global photo_erkundung

    for widget in root.winfo_children():

        widget.destroy()

 

    root.title("Salziges Ufer")

 

    image = Image.open("C:\GitHub\Schatten_ueber_Veridia\Bilder\Veridia.png")

    photo_erkundung = ImageTk.PhotoImage(image)

 

    label = tk.Label(root, image=photo_erkundung)

    label.pack()

 

    MainButton = tk.Button(root, text="Main", command=Main)

    MainButton.pack()

 

def Main():

    for widget in root.winfo_children():

        widget.destroy()

 

    root.title("Main")

 

    KampfButton = tk.Button(root, text="Kampf", command=Kampf)

    KampfButton.pack()

 

    DialogButton = tk.Button(root, text="Dialog", command=Dialog)

    DialogButton.pack()

 

    ErkundungsButton = tk.Button(root, text="Erkundung", command=Erkundung)

    ErkundungsButton.pack()

 

# Erstellen Sie das Hauptfenster

root = tk.Tk()

root.geometry("750x600")

Main()

 

# Starten Sie die Tkinter-Haupt-Schleife

root.mainloop()

 