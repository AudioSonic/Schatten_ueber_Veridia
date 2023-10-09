import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *

def explore(root, parent_frame):  
    for widget in parent_frame.winfo_children():
        widget.destroy()
  
    #Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    bg_pfad = Image.open(Veridia)
    bg_image = ImageTk.PhotoImage(bg_pfad)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=253, y=18)

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
    lp_pfad = Image.open(arrowLeft)
    lp_image = ImageTk.PhotoImage(lp_pfad)
    lp_Button = ttk.Button(root, image=lp_image)
    lp_Button.place(x=18, y=350)

    #Der rechts Pfeil
    rp_pfad = Image.open(arrowRight)
    rp_image = ImageTk.PhotoImage(rp_pfad)
    rp_Button = ttk.Button(root, image=rp_image)
    rp_Button.place(x=1200, y=350)

    #Der front Pfeil
    vp_pfad = Image.open(arrowFront)
    vp_image = ImageTk.PhotoImage(vp_pfad)
    vp_Button = ttk.Button(root, image=vp_image)
    vp_Button.place(x=600, y=20)

    #Der return Pfeil
    rt_pfad = Image.open(arrowReturn)
    rt_image = ImageTk.PhotoImage(rt_pfad)
    rt_Button = ttk.Button(root, image=rt_image)
    rt_Button.place(x=20, y=670)

    #Der Button für die Karte
    mb_pfad = Image.open(KarteButton)
    mb_image = ImageTk.PhotoImage(mb_pfad)
    mb_Button = ttk.Button(root, image=mb_image)
    mb_Button.place(x=1250, y=20)

    # Textfeld fuer die Ausgabe
    text_output = tk.Text(root, height=6, width=90, wrap="none")
    text_output.place(x = 18, y = 470)
    text_output.config(state=tk.DISABLED)  # Sperrt das Textfeld


    #Einfuegen und aendern des Lauftext
    text_output.config(state=tk.NORMAL)
    text_output.insert(tk.END, "A\nB\nC\nD\nF\nG")
    text_output.config(state=tk.DISABLED)      

    custom_font = ("Times New Roman", 20)
    text_output.config(font=custom_font)

    root.mainloop()
    return root






