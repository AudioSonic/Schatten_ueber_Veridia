import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager
from Fight import Fight
from Gegnerliste import Vorluna
import Erkunden_Ebene as Ebene
import Erkunden_Hoehle as Hoehle
import Erkunden_Sumpf as Sumpf
import Erkunden_ZVeridia as ZVeridia
import Erkunden_Kueste as Kueste


def forest(root, parent_frame):  
    for widget in parent_frame.winfo_children():
        widget.destroy()
  
    # Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    bg_pfad = Image.open(Wald)
    bg_image = ImageTk.PhotoImage(bg_pfad)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=253, y=18)

    # Die TextboxManager aus der Dialogsystem Datei
    Dialog = TextboxManager(parent_frame)
    Dialog.update_text(Einleitung)

    # Die Startposition des Charakters
    pc_loc = [1, 0]
    # Das Gitter-Wörterbuch, das Koordinaten mit Aktionen verknüpft
    grid = {
        (0, 0): Wald_1,
        (0, 1): Wald_2,
        (0, 2): Wald_3,
        (1, 0): Wald_4,
        (1, 1): Wald_5,
        (1, 2): Wald_6,
        (2, 0): Wald_7,
        (2, 1): Wald_8,
        (2, 2): Wald_9
    }

    def examine():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(Wald_1_Examine)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Wald_2_Examine)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(Wald_3_Examine)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Wald_4_Examine)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(Wald_5_Examine)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Wald_6_Examine)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Wald_7_Examine) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Wald_8_Examine) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(Wald_9_Examine)            

    def touch():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(Wald_1_Touch)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Wald_2_Touch)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(Wald_3_Touch)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Wald_4_Touch)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(Wald_5_Touch)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Wald_6_Touch)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Wald_7_Touch) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Wald_8_Touch) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(Wald_9_Touch) 

    def perceive():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(Wald_1_Perceive)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Wald_2_Perceive)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(Wald_3_Perceive)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Wald_4_Perceive)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(Wald_5_Perceive)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Wald_6_Perceive)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Wald_7_Perceive) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Wald_8_Perceive) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(Wald_9_Perceive) 

    def pickup():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(Wald_1_PickUp)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Wald_2_PickUp)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(Wald_3_PickUp)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Wald_4_PickUp)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(Wald_5_PickUp)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Wald_6_PickUp)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Wald_7_PickUp) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Wald_8_PickUp) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(Wald_9_PickUp) 
    def kampf():
        if pc_loc[0] == 2 and pc_loc[1] ==2:
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
            mb_Button.place_forget()
            bg_label.place_forget()
            Fight(root, parent_frame, Vorluna)
    def vor():
        new_y = pc_loc[1] + 1
        
        if (pc_loc[0], new_y) in grid:
            pc_loc[1] = new_y
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
            kampf()
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)
          
    def links():
        new_x = pc_loc[0] - 1
        if (new_x, pc_loc[1]) in grid:
            pc_loc[0] = new_x
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))            
            kampf()
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)        
    
    def rechts():
        new_x = pc_loc[0] + 1
        if (new_x, pc_loc[1]) in grid:
            pc_loc[0] = new_x
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
            kampf()
        else:
            Dialog.update_text("You cannot go further in this direction.")
        print(pc_loc)
        
    def zurueck():
        new_y = pc_loc[1] - 1
        if (pc_loc[0], new_y) in grid:
            pc_loc[1] = new_y
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
            kampf()
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
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))

    def MapButton():
        Map = tk.Toplevel(root)
        Map.title("Map")
        Map.geometry("636x592")
        Map.resizable(False, False)
        Map.configure(bg="#6B6B6B")
        Map.attributes("-fullscreen", False)

        m_pfad = Image.open("C:\\GitHub\\Schatten_ueber_Veridia\\Bilder\\WorldMap.png")
        m_image = ImageTk.PhotoImage(m_pfad)
        m_label = tk.Label(Map, image=m_image)
        m_label.image = m_image  # Wichtig: Behalte eine Referenz auf das Bild, um es anzuzeigen.
        m_label.place(x=-1, y=0)
           
        def SumpfButton(root, parent_frame):
                for widget in parent_frame.winfo_children():
                    widget.destroy()
                loc.place_forget()
                coord.place_forget()
                betrButton.place_forget() 
                untButton.place_forget()
                whrButton.place_forget()
                aufhbButton.place_forget()
                lp_Button.place_forget()
                rp_Button.place_forget()
                vp_Button.place_forget()
                zp_Button.place_forget()
                rt_Button.place_forget()
                mb_Button.place_forget()
                bg_label.place_forget()
                Map.destroy()
                Sumpf.swamp(root, parent_frame)
            
        def HoehleButton(root, parent_frame):
                for widget in parent_frame.winfo_children():
                    widget.destroy()
                loc.place_forget()
                coord.place_forget()
                betrButton.place_forget() 
                untButton.place_forget()
                whrButton.place_forget()
                aufhbButton.place_forget()
                lp_Button.place_forget()
                rp_Button.place_forget()
                vp_Button.place_forget()
                zp_Button.place_forget()
                rt_Button.place_forget()
                mb_Button.place_forget()
                bg_label.place_forget()
                Map.destroy()
                Hoehle.cave(root, parent_frame)

        def EbeneButton(root, parent_frame):
                for widget in parent_frame.winfo_children():
                    widget.destroy()
                loc.place_forget()
                coord.place_forget()
                betrButton.place_forget() 
                untButton.place_forget()
                whrButton.place_forget()
                aufhbButton.place_forget()
                lp_Button.place_forget()
                rp_Button.place_forget()
                vp_Button.place_forget()
                zp_Button.place_forget()
                rt_Button.place_forget()
                mb_Button.place_forget()
                bg_label.place_forget()
                Map.destroy()
                Ebene.plain(root, parent_frame)
            
        def ZVeridiaButton(root, parent_frame):
                for widget in parent_frame.winfo_children():
                    widget.destroy()
                loc.place_forget()
                coord.place_forget()
                betrButton.place_forget() 
                untButton.place_forget()
                whrButton.place_forget()
                aufhbButton.place_forget()
                lp_Button.place_forget()
                rp_Button.place_forget()
                vp_Button.place_forget()
                zp_Button.place_forget()
                rt_Button.place_forget()
                mb_Button.place_forget()
                bg_label.place_forget()
                Map.destroy()
                ZVeridia.zveridia(root, parent_frame)
            
        def KuesteButton(root, parent_frame):
                for widget in parent_frame.winfo_children():
                    widget.destroy()
                loc.place_forget()
                coord.place_forget()
                betrButton.place_forget() 
                untButton.place_forget()
                whrButton.place_forget()
                aufhbButton.place_forget()
                lp_Button.place_forget()
                rp_Button.place_forget()
                vp_Button.place_forget()
                zp_Button.place_forget()
                rt_Button.place_forget()
                mb_Button.place_forget()
                bg_label.place_forget()
                Map.destroy()
                Kueste.coast(root, parent_frame)
        
        ZVeridia_Button = tk.Button(Map, text="ZVeridia", command=lambda: ZVeridiaButton(root, parent_frame))
        ZVeridia_Button.place(x=230, y=300) 
        Kueste_Button = tk.Button(Map, text="Coast", command=lambda: KuesteButton(root, parent_frame))
        Kueste_Button.place(x=300, y=110) 
        Sumpf_Button = tk.Button(Map, text="Swamp", command=lambda: SumpfButton(root, parent_frame))
        Sumpf_Button.place(x=50, y=350) 
        Ebene_Button = tk.Button(Map, text="Plain", command=lambda: EbeneButton(root, parent_frame))
        Ebene_Button.place(x=280, y=510) 
        Hoehle_Button = tk.Button(Map, text="Cave", command=lambda: HoehleButton(root, parent_frame))
        Hoehle_Button.place(x=570, y=370)
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

    # Der Button für die Karte
    mb_pfad = Image.open(KarteButton)
    mb_image = ImageTk.PhotoImage(mb_pfad)
    mb_Button = ttk.Button(root, image=mb_image, command=MapButton)
    mb_Button.place(x=1250, y=20)

    #Die textbox mit den Koordinaten
    coord = tk.Text(root, width=15, height=1, font=("Times New Roman", 14))
    loc = tk.Text(root, width=18, height=1, font=("Times New Roman", 14))
    loc.insert(tk.END, "Urnacht-Wald")
    coord.insert(tk.END, " Location: " + str(pc_loc))
    coord.place(x=20, y=440)    
    loc.place(x=1115, y=440)
    root.mainloop()
    return root