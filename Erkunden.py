import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager



#Der Standort des Spielers. X - Y


def explore(root, parent_frame):  
    for widget in parent_frame.winfo_children():
        widget.destroy()
  
    # Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    bg_pfad = Image.open(Veridia)
    bg_image = ImageTk.PhotoImage(bg_pfad)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=253, y=18)

    # Die TextboxManager aus der Dialogsystem Datei
    # Die TextboxManager aus der Dialogsystem Datei
    Dialog = TextboxManager(parent_frame)
    Dialog.update_text(Einleitung)

    # Die Startposition des Charakters
    pc_loc = [1, 0]

    # Das Gitter-Wörterbuch, das Koordinaten mit Aktionen verknüpft
    grid_actions = {
        (0, 0): Brigitte_1,
        (0, 1): Veridia_6,
        (0, 2): Ulrich_1,
        (0, 3): Veridia_8,
        (1, 0): Veridia_9,
        (1, 1): Miriam_1,
        (1, 2): Veridia_11,
        (1, 3): Veridia_12,
        (2, 0): Veridia_13,
        (2, 1): Veridia_14,
        (2, 2): Gottfried_1,
        (2, 3): Veridia_16,
        (3, 0): Veridia_17,
        (3, 1): Veridia_18,
        (3, 2): Veridia_19,
        (3, 3): Veridia_20
    }

    def examine_1():
        Dialog.update_text(Veridia_1)

    def touch_1():
        Dialog.update_text(Veridia_2)

    def perceive_1():
        Dialog.update_text(Veridia_3)

    def pickup_1():
        Dialog.update_text(Veridia_4)

    def vor():
        pc_loc[1] += 1
        print(pc_loc)
    
        if tuple(pc_loc) in grid_actions:
            action = grid_actions[tuple(pc_loc)]
        Dialog.update_text(action)
        
    def links():
        pc_loc[0] -= 1
        print(pc_loc)
    
        if tuple(pc_loc) in grid_actions:
            action = grid_actions[tuple(pc_loc)]
        Dialog.update_text(action)
    
    def rechts():
        pc_loc[0] += 1
        print(pc_loc)
    
        if tuple(pc_loc) in grid_actions:
            action = grid_actions[tuple(pc_loc)]
        Dialog.update_text(action)
        
    def zurueck():
            pc_loc[1] -= 1
            print(pc_loc)
    
            if tuple(pc_loc) in grid_actions:
                action = grid_actions[tuple(pc_loc)]
            Dialog.update_text(action)

        

    # Setzt die Breite der Buttons fest
    button_width = 15
    # Der "Betrachten" Button
    betrButton = ttk.Button(root, text="EXAMINE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=examine_1)
    betrButton.place(x=130, y=680)

    # Der "Untersuchen" Button
    untButton = ttk.Button(root, text="TOUCH", padding=(50, 10), width=button_width, style="TNR.TLabel", command=touch_1)
    untButton.place(x=390, y=680)

    # Der "Wahrnehmen" Button
    whrButton = ttk.Button(root, text="PERCEIVE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=perceive_1)
    whrButton.place(x=650, y=680)

    # Der "Aufheben" Button
    aufhbButton = ttk.Button(root, text="PICK UP", padding=(50, 10), width=button_width, style="TNR.TLabel", command=pickup_1)
    aufhbButton.place(x=910, y=680)

    # Der links Pfeil
    lp_pfad = Image.open(arrowLeft)
    lp_image = ImageTk.PhotoImage(lp_pfad)
    lp_Button = ttk.Button(root, image=lp_image, command=links)
    lp_Button.place(x=18, y=350)

    # Der rechts Pfeil
    rp_pfad = Image.open(arrowRight)
    rp_image = ImageTk.PhotoImage(rp_pfad)
    rp_Button = ttk.Button(root, image=rp_image, command=rechts)
    rp_Button.place(x=1200, y=350)

    # Der front Pfeil
    vp_pfad = Image.open(arrowFront)
    vp_image = ImageTk.PhotoImage(vp_pfad)
    vp_Button = ttk.Button(root, image=vp_image, command=vor)
    vp_Button.place(x=600, y=20)

    # Der return Pfeil
    rt_pfad = Image.open(arrowReturn)
    rt_image = ImageTk.PhotoImage(rt_pfad)
    rt_Button = ttk.Button(root, image=rt_image, command=zurueck)
    rt_Button.place(x=20, y=670)

    # Der Button für die Karte
    mb_pfad = Image.open(KarteButton)
    mb_image = ImageTk.PhotoImage(mb_pfad)
    mb_Button = ttk.Button(root, image=mb_image)
    mb_Button.place(x=1250, y=20)
    
    if pc_loc[0] == [1] and pc_loc[1] ==[1]:
        Dialog.update_text(Veridia_5)
        print("Update")

    root.mainloop()
    return root







