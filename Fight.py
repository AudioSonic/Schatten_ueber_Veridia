from ctypes import FormatError
from os import name
import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from turtle import delay
from typing import Callable
from PIL import Image, ImageTk
from Bilder import *
import Gegnerliste
import Erkunden
import random
import Dialoge
import Erkunden_Wald
import Erkunden_Ebene
import Erkunden_Hoehle
import Erkunden_Kueste
import Erkunden_Sumpf
import Main
import Boss_Intro
import Ending_1
import Erkunden_ZVeridia


def Fight(root, parent_frame, gegner):
    
    for widget in parent_frame.winfo_children():
        widget.destroy()
    

    #Erstellt einen Stil f�r die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  


    # Hintergrundbild einfuegen
    gegner_pfad = Image.open(gegner[4])
    gegner_image = ImageTk.PhotoImage(gegner_pfad)
    gegner_label = tk.Label(root, image= gegner_image)
    gegner_label.place(x=210, y=30)
    
    def del_obj():
        gegner_label.place_forget()
        attack_button.place_forget()
        recover_button.place_forget()
        progress_bar.place_forget()
        counter_button.place_forget()
        potion_button.place_forget()
        escape_button.place_forget()
        gegner_name.place_forget()
        Player_output.place_forget()
        text_output.place_forget()
       
    def Gegner_Wald():
        del_obj()
        Erkunden_Wald.forest(root, parent_frame)
        
        
    def Gegner_Ebene():
        del_obj()
        Erkunden_Ebene.plain(root, parent_frame)
    
    def Gegner_Kueste():
        del_obj()
        Erkunden_Kueste.coast(root, parent_frame)
       
        
    def Gegner_Sumpf():
        del_obj()
        Erkunden_Sumpf.swamp(root, parent_frame)
       
    def Gegner_Hoehle():
        del_obj()
        Erkunden_Hoehle.cave(root, parent_frame)
    
    def Zyrelia_Boss():
        del_obj()
        Erkunden_Wald.forest(root, parent_frame)
        
    def Varoth_Boss():
        del_obj()
        Erkunden_Ebene.plain(root, parent_frame)
        
    def Dreznar_Boss():
        del_obj()
        Erkunden_Kueste.coast(root, parent_frame)
        

    def Malkor_Boss():
        del_obj()
        Erkunden_Sumpf.swamp(root, parent_frame)
       
    def Vorluna_Boss():
        del_obj()
        Erkunden_Hoehle.cave(root, parent_frame)
    
    def Malikar_Boss():
        del_obj()
        Erkunden_ZVeridia.zveridia(root, parent_frame)
        
    def Respawn():
        if Gegnerliste.Vorluna_Boss[8] == 0 and Gegnerliste.Varoth_Boss[8] == 0 and Gegnerliste.Zyrelia_Boss[8] == 0 and Gegnerliste.Malkor_Boss[8] == 0 and Gegnerliste.Dreznar_Boss[8] == 0:
            del_obj()
            Boss_Intro.Boss_Intro(root, parent_frame)
        else:
            del_obj()
            Erkunden.explore(root, parent_frame)
        
    
    # Druck des Attack Button
    def attack():
        update_progress()
        current_boss_hp = boss_hp.get()
        player_hp_anzeige = player_hp.get()
        if player_hp_anzeige >0:
            if player_STM.get() >=10:
                if current_boss_hp > 0:
                    text_output.config(state=tk.NORMAL)
                    text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                    text_output.insert(tk.END, random.choice(Dialoge.attacktext))
                    text_output.config(state=tk.DISABLED)
                    boss_hp.set(current_boss_hp - gegner[9])
                    update_progress()
                    stamina_attack()
                    boss_attack()
                    update_player_stats()
                    update_progress()
               
            else:
                text_output.config(state=tk.NORMAL)
                text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                text_output.insert(tk.END, "Not enough stamina for this action recover first")
                text_output.config(state=tk.DISABLED)
                update_progress()
        else:
            GAME_OVER()
               
    # Druck des Counter Button            
    def counter():
        update_progress()
        current_boss_hp = boss_hp.get()
        player_hp_anzeige = player_hp.get()
        if player_hp_anzeige >0:
            if player_STM.get() >=25:        
                if current_boss_hp >= 0:   
                    text_output.config(state=tk.NORMAL)
                    text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                    text_output.insert(tk.END,  random.choice(Dialoge.countertext))
                    text_output.config(state=tk.DISABLED)
                    boss_hp.set(current_boss_hp - gegner[10])
                    update_progress()
                    stamina_counter()
                    boss_attack_counter()
                    update_player_stats()
                    update_progress()
               
            else:
             text_output.config(state=tk.NORMAL)
             text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
             text_output.insert(tk.END, "Not enough stamina for this action")
             text_output.config(state=tk.DISABLED)
             update_progress()
                   
        else: GAME_OVER()        
     
    # Druck des Recover Button
    def recover():
        player_hp_anzeige = player_hp.get()
        update_progress()
        current_boss_hp = boss_hp.get()
        stamina = player_STM.get()
        if player_hp_anzeige >0:                    
            if current_boss_hp > 0:
                if stamina <= 20: 
                    player_STM.set(stamina + 10)
                    text_output.config(state=tk.NORMAL)
                    text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                    text_output.insert(tk.END, "You restored stamina and the enemy hit´s you")
                    text_output.config(state=tk.DISABLED)
                    boss_attack()
                    update_player_stats()
                    update_progress()
                else:
                    text_output.config(state=tk.NORMAL)
                    text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                    text_output.insert(tk.END, "You can not restore more stamina")
                    text_output.config(state=tk.DISABLED)
                    update_progress()
        else:
            player_hp.set(0)
            GAME_OVER()
            
    # Druck des Potioin Button
    def potion():
        current_player_hp = player_hp.get()
        if current_player_hp >0: 
            if current_player_hp <60:
               text_output.config(state=tk.NORMAL)
               text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
               text_output.insert(tk.END, "You healed up")
               text_output.config(state=tk.DISABLED)
               player_hp.set(current_player_hp+60)
               update_player_stats()
               
                
            else: 
                text_output.config(state=tk.NORMAL)
                text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                text_output.insert(tk.END, "Es ist noch zu früh einen Tank zu nehmen")
                text_output.config(state=tk.DISABLED)
                update_progress()
        else:
            GAME_OVER()
            
    def escape():
        if gegner[7] in range(6,12):
            text_output.config(state=tk.NORMAL)
            text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
            text_output.insert(tk.END, "There is no Escape")
            text_output.config(state=tk.DISABLED)
            
        elif gegner[7] == 1:
            del_obj()
            Gegner_Wald()
            
        elif gegner[7] == 2:
            del_obj()
            Gegner_Sumpf()
            
        elif gegner[7] == 3:
            del_obj()
            Gegner_Kueste()
            
        elif gegner[7] == 4:
            del_obj()
            Gegner_Hoehle()
            
        elif gegner[7] == 5:
            del_obj()
            Gegner_Ebene()
            
    def back():
        if gegner[6] == "Malikar":
            del_obj()
            Ending_1.Ending(root, parent_frame)
            
        elif Gegnerliste.Vorluna_Boss[8] == 0 and Gegnerliste.Varoth_Boss[8] == 0 and Gegnerliste.Zyrelia_Boss[8] == 0 and Gegnerliste.Malkor_Boss[8] == 0 and Gegnerliste.Dreznar_Boss[8] == 0:
            del_obj()
            Boss_Intro.Boss_Intro(root, parent_frame)
            
        else:
            if gegner[7] == 6:
                del_obj()
                Malikar_Boss()
            
            elif gegner[7] == 7:
                del_obj()
                Varoth_Boss()
            
            elif gegner[7] == 8:
                del_obj()
                Zyrelia_Boss()
            
            elif gegner[7] == 9:
                del_obj()
                Malkor_Boss()
            
            elif gegner[7] == 10:
                del_obj()
                Dreznar_Boss()
            

            elif gegner[7] == 11:
                del_obj()
                Vorluna_Boss()
            
            elif gegner[7] == 1:
                del_obj()
                Gegner_Wald()
            
            elif gegner[7] == 2:
                del_obj()
                Gegner_Sumpf()
            
            elif gegner[7] == 3:
                del_obj()
                Gegner_Kueste()
            
            elif gegner[7] == 4:
                del_obj()
                Gegner_Hoehle()
            
            elif gegner[7] == 5:
                del_obj()
                Gegner_Ebene()

    
    def update_player_stats():
        show_HP =  f"HP:                  {player_hp.get()}/120"    
        show_STM = f"Stamina:          {player_STM.get()}/30"
        Player_output.config(state=tk.NORMAL)
        Player_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
        Player_output.insert(tk.END, f"{player}\n{show_HP}\n{show_STM}")
        Player_output.config(state=tk.DISABLED)

        
    def update_progress():
        current_boss_hp = boss_hp.get()
        progress_bar["value"] = current_boss_hp
        current_player_hp = player_hp.get()
        if current_player_hp <= 0:
            GAME_OVER()
            update_player_stats()
            
        else: 
            if current_boss_hp <= 0:
  
                text_output.config(state=tk.NORMAL)
                text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
                text_output.insert(tk.END, "Victory")
                text_output.config(state=tk.DISABLED)
                gegner[8] = 0
                recover_button.place_forget()
                counter_button.place_forget()
                potion_button.place_forget()
                escape_button.place_forget()
                attack_button.config(text = "Back to start", command=back)
                
    #Der "Back" Button          
    
   
    def GAME_OVER():
       
       text_output.config(state=tk.NORMAL)
       text_output.delete(1.0, tk.END)  # L�scht den aktuellen Text
       text_output.insert(tk.END, "GAME OVER")
       text_output.config(state=tk.DISABLED)
       player_hp.set(0)
       update_player_stats()
       recover_button.place_forget()
       counter_button.place_forget()
       potion_button.place_forget()
       escape_button.place_forget()
       attack_button.config(text = "Respawn", command=Respawn)
       
    
    def stamina_attack():
        current_stmna = player_STM.get()       
        if current_stmna >= 10:
            player_STM.set(current_stmna - 10)


    def stamina_counter():
        current_stmna = player_STM.get()
        if current_stmna >= 25:
            player_STM.set(current_stmna - 25)
        
    def boss_attack():
        dmg = [gegner[1], gegner[2], gegner[3]]
        random_dmg = random.choice(dmg)
        current_player_hp = player_hp.get()
        if current_player_hp > 0:
          player_hp.set(current_player_hp - random_dmg)
          
          if current_player_hp <= 0:
              GAME_OVER()
       
            
    def boss_attack_counter():
        dmg = [gegner[1], gegner[2], gegner[3]]
        random_dmg = random.choice(dmg)
        current_player_hp = player_hp.get()
        if current_player_hp > 0:
           player_hp.set(current_player_hp - (random_dmg + random_dmg))
           
           if current_player_hp <= 0:
               GAME_OVER()
               
    
        
    # Erstelle eine Variable zur Verfolgung der Spieler-HP
    player_hp = tk.IntVar()
    player_hp.set(120)  # Starte mit vollen HP


    # Erstelle eine Variable zur Verfolgung der Spieler-STM
    player_STM = tk.IntVar()
    player_STM.set(30)  # Starte mit voller Stamina
    
     
    
    # Textfeld fuer die Ausgabe
    gegner_name = tk.Text(root, height=1, width=33, wrap="none")
    gegner_name.place(x = 355, y = 45)
    gegner_name.config(state=tk.DISABLED)  # Sperrt das Textfeld

    gegner_front = ("Times New Roman", 18)
    gegner_name.config(font=gegner_front)
    
    #Einfuegen und aendern des Lauftext
    gegner_name.config(state=tk.NORMAL)
    gegner_name.insert(tk.END, gegner[6])
    gegner_name.config(state=tk.DISABLED) 
    
    # Erstelle eine Variable zur Verfolgung der Boss-HP
    boss_hp = tk.IntVar()
    boss_hp.set(10) # Starte mit vollen HP
    
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
    potion_button = ttk.Button(root, text= "Potion", padding=(50, 10), width= button_width, style="TNR.TLabel", command=potion)
    potion_button.place(x=793, y=680)
    
    

    #Der "Escape" Button
    escape_button = ttk.Button(root, text= "Escape", padding=(50, 10), width=button_width, style="TNR.TLabel", command=escape)
    escape_button.place(x=1043, y=680)


    # Player View
    Player_output = tk.Text(root, height=3, width=25, wrap="none")
    Player_output.place(x = 50, y = 375)
    Player_output.config(state=tk.DISABLED)  # Sperrt das Textfeld
    

    #Bearbeitung Name/HP/Stamina
    show_HP =  f"HP:                  {player_hp.get()}/120"
    show_STM = f"Stamina:          {player_STM.get()}/30"
    player =   "Max"

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
    text_output.insert(tk.END, gegner[5])
    text_output.config(state=tk.DISABLED)      


    custom_font = ("Times New Roman", 20)
    text_output.config(font=custom_font)


    root.mainloop()
    return root






