import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager
import Fight
import Gegnerliste 
import Erkunden_Wald as Wald
import Erkunden_Ebene as Ebene
import Erkunden_Hoehle as Hoehle
import Erkunden_Sumpf as Sumpf
import Erkunden_Kueste as Kueste


def zveridia(root, parent_frame):  
    for widget in parent_frame.winfo_children():
        widget.destroy()
  
    # Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    bg_pfad = Image.open(ZVeridia)
    bg_image = ImageTk.PhotoImage(bg_pfad)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=253, y=18)

    # Die TextboxManager aus der Dialogsystem Datei
    Dialog = TextboxManager(parent_frame)
    Dialog.update_text(ZVeridia_4)

    # Die Startposition des Charakters
    pc_loc = [1, 0]
    # Das Gitter-Wörterbuch, das Koordinaten mit Aktionen verknüpft
    grid = {
        (0, 0): ZVeridia_1,
        (0, 1): ZVeridia_2,
        (0, 2): ZVeridia_3,
        (1, 0): ZVeridia_4,
        (1, 1): ZVeridia_5, #Boss Malikar
        (1, 2): ZVeridia_6,
        (2, 0): ZVeridia_7,
        (2, 1): ZVeridia_8,
        (2, 2): ZVeridia_9
    }
    def Edelete():
        betrButton.place_forget() 
        loc.place_forget()
        coord.place_forget()
        untButton.place_forget()
        whrButton.place_forget()
        aufhbButton.place_forget()
        lp_Button.place_forget()
        rp_Button.place_forget()
        vp_Button.place_forget()
        zp_Button.place_forget()
        rt_Button.place_forget()
        bg_label.place_forget()
    
    def examine():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_1_Examine)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_2_Examine)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_3_Examine)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_4_Examine)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Edelete()
            Fight.Fight(root, parent_frame,Gegnerliste.Malikar_Boss)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_6_Examine)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_7_Examine) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_8_Examine) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_9_Examine)            

    def touch():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_1_Touch)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_2_Touch)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_3_Touch)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_4_Touch)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_5_Touch)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_6_Touch)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_7_Touch) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_8_Touch) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_9_Touch) 

    def perceive():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_1_Perceive)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_2_Perceive)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_3_Perceive)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_4_Perceive)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_5_Perceive)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_6_Perceive)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_7_Perceive) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_8_Perceive) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_9_Perceive) 

    def pickup():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_1_PickUp)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_2_PickUp)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_3_PickUp)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_4_PickUp)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_5_PickUp)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_6_PickUp)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(ZVeridia_7_PickUp) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(ZVeridia_8_PickUp) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(ZVeridia_9_PickUp) 

    def vor():
        new_y = pc_loc[1] + 1
        
        if (pc_loc[0], new_y) in grid:
            pc_loc[1] = new_y
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.config(state="normal")
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))         
            coord.config(state="disabled")  
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)
          
    def links():
        new_x = pc_loc[0] - 1
        if (new_x, pc_loc[1]) in grid:
            pc_loc[0] = new_x
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.config(state="normal")
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))    
            coord.config(state="disabled")            
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)        
    
    def rechts():
        new_x = pc_loc[0] + 1
        if (new_x, pc_loc[1]) in grid:
            pc_loc[0] = new_x
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.config(state="normal")
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
            coord.config(state="disabled")
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)
        
    def zurueck():
        new_y = pc_loc[1] - 1
        if (pc_loc[0], new_y) in grid:
            pc_loc[1] = new_y
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.config(state="normal")
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
            coord.config(state="disabled")
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)
        
    def reset():
            pc_loc[1] = 0
            pc_loc[0] = 1
            print(pc_loc)
            if tuple(pc_loc) in grid:
                action = grid[tuple(pc_loc)]
            Dialog.update_text(action)
            coord.config(state="normal")
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
            coord.config(state="disabled")

    # Setzt die Breite der Buttons fest
    button_width = 15
    # Der "Examine" Button
    betrButton = ttk.Button(root, text="EXAMINE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=examine)
    betrButton.place(x=130, y=680)

    # Der "Touch" Button
    untButton = ttk.Button(root, text="TOUCH", padding=(50, 10), width=button_width, style="TNR.TLabel", command=touch)
    untButton.place(x=390, y=680)

    # Der "Perceive" Button
    whrButton = ttk.Button(root, text="PERCEIVE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=perceive)
    whrButton.place(x=650, y=680)

    # Der "PickUp" Button
    aufhbButton = ttk.Button(root, text="PICK UP", padding=(50, 10), width=button_width, style="TNR.TLabel", command=pickup)
    aufhbButton.place(x=910, y=680)

    # Der links Pfeil
    lp_pfad = Image.open(arrowLeft)
    lp_image = ImageTk.PhotoImage(lp_pfad)
    lp_Button = ttk.Button(root, image=lp_image, command=links)
    lp_Button.place(x=125, y=200)

    # Der rechts Pfeil
    rp_pfad = Image.open(arrowRight)
    rp_image = ImageTk.PhotoImage(rp_pfad)
    rp_Button = ttk.Button(root, image=rp_image, command=rechts)
    rp_Button.place(x=1080, y=200)

    # Der front Pfeil
    vp_pfad = Image.open(arrowFront)
    vp_image = ImageTk.PhotoImage(vp_pfad)
    vp_Button = ttk.Button(root, image=vp_image, command=vor)
    vp_Button.place(x=600, y=10)
    
    # Der back Pfeil
    zp_pfad = Image.open(arrowBack)
    zp_image = ImageTk.PhotoImage(zp_pfad)
    zp_Button = ttk.Button(root, image=zp_image, command=zurueck)
    zp_Button.place(x=600, y=380)

    # Der return Pfeil
    rt_pfad = Image.open(arrowReturn)
    rt_image = ImageTk.PhotoImage(rt_pfad)
    rt_Button = ttk.Button(root, image=rt_image, command=reset)
    rt_Button.place(x=20, y=670)

    #Die textbox mit den Koordinaten
    coord = tk.Text(root, width=15, height=1, font=("Times New Roman", 14))
    loc = tk.Text(root, width=18, height=1, font=("Times New Roman", 14))
    loc.insert(tk.END, "Ruined Veridia")
    coord.insert(tk.END, " Location: " + str(pc_loc))
    coord.place(x=20, y=440)    
    loc.place(x=1115, y=440)
    coord.config(state="disabled")
    loc.config(state="disabled")
    root.mainloop()
    return root

