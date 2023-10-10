import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *

def Fight(root, parent_frame):
    for widget in parent_frame.winfo_children():
        widget.destroy()
  
    #Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    Hhle_pfad = Image.open(Hoehle_Vorlunda)
    Hhle_image = ImageTk.PhotoImage(Hhle_pfad)
    Hhle_label = tk.Label(root, image= Hhle_image)
    Hhle_label.place(x=210, y=30)
    
    #Boss HP Balken

    def attack():
        current_hp = boss_hp.get()
        if current_hp > 0:
            boss_hp.set(current_hp - 10)
            update_progress()

    def update_progress():
        current_hp = boss_hp.get()
        progress_bar["value"] = current_hp

        if current_hp <= 0:
            status_label.config(text="Boss besiegt!")

    # Erstelle eine Variable zur Verfolgung der Boss-HP
    boss_hp = tk.IntVar()
    boss_hp.set(100)  # Starte mit vollen HP

    # Erstelle einen determinierten Ladebalken für die Boss-HP
    progress_bar = ttk.Progressbar(root, mode="determinate", variable=boss_hp, length=300)
    progress_bar.place(x = 400, y = 50)

    # Button für den Spielerangriff
    attack_button = ttk.Button(root, text="Angreifen", command=attack)
    attack_button.place(x = 400, y = 75)

    # Label zur Anzeige des Status
    status_label = ttk.Label(root, text="Boss noch nicht besiegt")
    status_label.place(x = 400, y = 100)

   
    #Setzt die Breite der Buttons fest
    button_width = 12
    #Der "Attack" Button
    betrButton = ttk.Button(root, text="Attack", padding=(50, 10), width=button_width, style="TNR.TLabel")
    betrButton.place(x=43, y=680)

    #Der "Defense" Button
    untButton = ttk.Button(root, text="Defense", padding=(50, 10), width=button_width, style="TNR.TLabel")
    untButton.place(x=293, y=680)

    #Der "Counter" Button
    whrButton = ttk.Button(root, text="Counter", padding=(50, 10), width=button_width, style="TNR.TLabel")
    whrButton.place(x=543, y=680)

    #Der "Inventory" Button
    aufhbButton = ttk.Button(root, text="Inventory", padding=(50, 10), width=button_width, style="TNR.TLabel")
    aufhbButton.place(x=793, y=680)
    
    #Der "Escape" Button
    aufhbButton = ttk.Button(root, text="Escape", padding=(50, 10), width=button_width, style="TNR.TLabel")
    aufhbButton.place(x=1043, y=680)

    # Player View
    Player_output = tk.Text(root, height=3, width=35, wrap="none")
    Player_output.place(x = 50, y = 375)
    Player_output.config(state=tk.DISABLED)  # Sperrt das Textfeld
    
    #Bearbeitung Name/HP/Stamina
    Player_output.config(state=tk.NORMAL)
    Player_output.insert(tk.END, "Player\nHP\nStamina")
    Player_output.config(state=tk.DISABLED)     
    custom_font = ("Times New Roman", 16)
    Player_output.config(font=custom_font) 
    
    # Support View
    Support_output = tk.Text(root, height=3, width=35, wrap="none")
    Support_output.place(x = 850, y = 375)
    Support_output.config(state=tk.DISABLED)  # Sperrt das Textfeld
    
    #Bearbeitung Name/HP/Stamina (Support)
    Support_output.config(state=tk.NORMAL)
    Support_output.insert(tk.END, "NPC\nHP\nStamina")
    Support_output.config(state=tk.DISABLED) 
    custom_font = ("Times New Roman", 16)
    Support_output.config(font=custom_font) 


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






