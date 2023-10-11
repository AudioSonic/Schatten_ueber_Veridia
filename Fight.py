import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *



def Fight(root, parent_frame):
    for widget in parent_frame.winfo_children():
        widget.destroy()
  

    #Erstellt einen Stil f�r die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  


    # Hintergrundbild einfuegen
    Hhle_pfad = Image.open(Hoehle_Vorlunda)
    Hhle_image = ImageTk.PhotoImage(Hhle_pfad)
    Hhle_label = tk.Label(root, image= Hhle_image)
    Hhle_label.place(x=210, y=30)
    

    #Boss HP Balken
    def attack():
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
        text_output.config(state=tk.DISABLED)
        update_progress()
        current_boss_hp = boss_hp.get()
        if player_STM.get() >=10:
            if current_boss_hp > 0:   
                boss_hp.set(current_boss_hp - 10)
                update_progress()
                stamina_attack()
                update_player_stats()
        else:
            if current_boss_hp > 0:     
                text_output.config(state=tk.NORMAL)
                text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                text_output.insert(tk.END, "Not enough stamina for this action recover first")
                text_output.config(state=tk.DISABLED) 
            else:
                update_progress()
               
                
    def counter():
        text_output.config(state=tk.NORMAL)
        text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
        text_output.config(state=tk.DISABLED)
        update_progress()
        current_boss_hp = boss_hp.get()
        if player_STM.get() >=25:
            if current_boss_hp > 0:   
                boss_hp.set(current_boss_hp - 25)
                update_progress()
                stamina_counter()
                update_player_stats()
        else:
            if current_boss_hp > 0:     
                text_output.config(state=tk.NORMAL)
                text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                text_output.insert(tk.END, "Not enough stamina for this action")
                text_output.config(state=tk.DISABLED)    
            else:
                update_progress()
              
                
    def recover():
        update_progress()
        current_boss_hp = boss_hp.get()
        if current_boss_hp > 0:
            stamina = player_STM.get()
            player_STM.set(stamina + 10)
            text_output.config(state=tk.NORMAL)
            text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
            text_output.insert(tk.END, "You restored 10 stamina")
            text_output.config(state=tk.DISABLED)
            update_player_stats()
        

    def update_player_stats():
        show_HP =  f"HP:                  {player_hp.get()}/100"    
        show_STM = f"Stamina:          {player_STM.get()}/30"
        Player_output.config(state=tk.NORMAL)
        Player_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
        Player_output.insert(tk.END, f"{player}\n{show_HP}\n{show_STM}")
        Player_output.config(state=tk.DISABLED)

        
    def update_progress():
        current_boss_hp = boss_hp.get()
        progress_bar["value"] = current_boss_hp

        if current_boss_hp <= 0:
            text_output.config(state=tk.NORMAL)
            text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
            text_output.insert(tk.END, "Victory")
            text_output.config(state=tk.DISABLED) 
   

    def stamina_attack():
        current_stmna = player_STM.get()       
        if current_stmna >= 10:
            player_STM.set(current_stmna - 10)


    def stamina_counter():
        current_stmna = player_STM.get()
        if current_stmna >= 25:
            player_STM.set(current_stmna - 25)
        
       
            
    # Erstelle eine Variable zur Verfolgung der Spieler-HP
    player_hp = tk.IntVar()
    player_hp.set(100)  # Starte mit vollen HP


    # Erstelle eine Variable zur Verfolgung der Spieler-STM
    player_STM = tk.IntVar()
    player_STM.set(30)  # Starte mit voller Stamina
    

    # Erstelle eine Variable zur Verfolgung der Boss-HP
    boss_hp = tk.IntVar()
    boss_hp.set(100)  # Starte mit vollen HP

    # Textfeld fuer die Ausgabe
    gegner_name = tk.Text(root, height=1, width=33, wrap="none")
    gegner_name.place(x = 355, y = 45)
    gegner_name.config(state=tk.DISABLED)  # Sperrt das Textfeld

    gegner_front = ("Times New Roman", 18)
    gegner_name.config(font=gegner_front)
    
    #Einfuegen und aendern des Lauftext
    gegner_name.config(state=tk.NORMAL)
    gegner_name.insert(tk.END, "Vorluna:")
    gegner_name.config(state=tk.DISABLED)
    
    # Erstelle einen determinierten Ladebalken f�r die Boss-HP
    progress_bar = ttk.Progressbar(root, mode="determinate", variable=boss_hp, length=300)
    progress_bar.place(x = 450, y = 50)
   

    #Setzt die Breite der Buttons fest
    button_width = 12
    

    # Button f�r den Spielerangriff
    attack_button = ttk.Button(root, text="Attack", padding=(50, 10), width= button_width, style="TNR.TLabel", command=attack)
    attack_button.place(x=43, y=680)


    #Der "Recover" Button
    recover_button = ttk.Button(root, text="Recover", padding=(50, 10), width=button_width, style="TNR.TLabel", command=recover)
    recover_button.place(x=293, y=680)


    #Der "Counter" Button
    counter_button = ttk.Button(root, text="Counter", padding=(50, 10), width= button_width, style="TNR.TLabel", command=counter)
    counter_button.place(x=543, y=680)


    #Der "Inventory" Button
    aufhbButton = ttk.Button(root, text="Inventory", padding=(50, 10), width=button_width, style="TNR.TLabel")
    aufhbButton.place(x=793, y=680)
    

    #Der "Escape" Button
    aufhbButton = ttk.Button(root, text="Escape", padding=(50, 10), width=button_width, style="TNR.TLabel")
    aufhbButton.place(x=1043, y=680)


    # Player View
    Player_output = tk.Text(root, height=3, width=25, wrap="none")
    Player_output.place(x = 50, y = 375)
    Player_output.config(state=tk.DISABLED)  # Sperrt das Textfeld
    

    #Bearbeitung Name/HP/Stamina
    show_HP =  f"HP:                  {player_hp.get()}/100"
    show_STM = f"Stamina:          {player_STM.get()}/30"
    player =    "Markus"

    Player_output.config(state=tk.NORMAL)
    Player_output.insert(tk.END, f"   {player}\n   {show_HP}\n   {show_STM}")
    Player_output.config(state=tk.DISABLED)
    custom_font = ("Times New Roman", 16)
    Player_output.config(font=custom_font)

    
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





