import tkinter as tk
from tkinter import Toplevel, ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager
import Erkunden_Wald as Wald
import Erkunden_Ebene as Ebene
import Erkunden_Hoehle as Hoehle
import Erkunden_Sumpf as Sumpf
import Erkunden_ZVeridia as ZVeridia
import Erkunden_Kueste as Kueste

def explore(root, parent_frame):
    # Erstellt einen Stil für die Schrift. In diesem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))

    # Hintergrundbild einfügen
    bg_pfad = Image.open(Veridia)  # Stellen Sie sicher, dass 'Veridia' definiert ist
    bg_image = ImageTk.PhotoImage(bg_pfad)
    bg_label = tk.Label(root, image=bg_image)
    bg_label.place(x=253, y=18)

    # Die TextboxManager aus der Dialogsystem-Datei
    Dialog = TextboxManager(parent_frame)
    Dialog.update_text(Veridia_4)

    # Die Startposition des Charakters
    pc_loc = [1, 0]

    # Das Grid-Wörterbuch, das Koordinaten mit Aktionen verknüpft
    grid = {
        (0, 0): Veridia_1, #Brigitte
        (0, 1): Veridia_2,
        (0, 2): Veridia_3, #Ulrich
        (1, 0): Veridia_4,
        (1, 1): Veridia_5, #Miriam
        (1, 2): Veridia_6,
        (2, 0): Veridia_7,
        (2, 1): Veridia_8,
        (2, 2): Veridia_9 #Gottfried
    }
    def EDelete():
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
        
    def examine():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            EDelete()
            Dialogfenster(root, parent_frame, character="Brigitte")
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_2_Examine)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            EDelete()
            Dialogfenster(root, parent_frame, character="Ulrich")   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_4_Examine)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            EDelete()
            Dialogfenster(root, parent_frame, character="Miriam")  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Veridia_6_Examine)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_7_Examine) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_8_Examine) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            EDelete()
            Dialogfenster(root, parent_frame, character="Gottfried")

    def touch():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            EDelete()
            Dialogfenster(root, parent_frame, character="Brigitte")
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_2_Touch)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            EDelete()
            Dialogfenster(root, parent_frame, character="Ulrich")     
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_4_Touch)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            EDelete()
            Dialogfenster(root, parent_frame, character="Miriam")    
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Veridia_6_Touch)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_7_Touch) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_8_Touch) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            EDelete()
            Dialogfenster(root, parent_frame, character="Gottfried")

    def perceive():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_1_Perceive)
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_2_Perceive)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            Dialog.update_text(Veridia_3_Perceive)   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_4_Perceive)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_5_Perceive)  
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Veridia_6_Perceive)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_7_Perceive) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_8_Perceive) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            Dialog.update_text(Veridia_9_Perceive) 

    def pickup():
        if pc_loc[0] == 0 and pc_loc[1] == 0:
            EDelete()
            Dialogfenster(root, parent_frame, character="Brigitte")
        elif pc_loc[0] == 0 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_2_PickUp)
        elif pc_loc[0] == 0 and pc_loc[1] == 2:
            EDelete()
            Dialogfenster(root, parent_frame, character="Ulrich")   
        elif pc_loc[0] == 1 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_4_PickUp)   
        elif pc_loc[0] == 1 and pc_loc[1] == 1:
            EDelete()
            Dialogfenster(root, parent_frame, character="Miriam") 
        elif pc_loc[0] == 1 and pc_loc[1] == 2:
            Dialog.update_text(Veridia_6_PickUp)  
        elif pc_loc[0] == 2 and pc_loc[1] == 0:
            Dialog.update_text(Veridia_7_PickUp) 
        elif pc_loc[0] == 2 and pc_loc[1] == 1:
            Dialog.update_text(Veridia_8_PickUp) 
        elif pc_loc[0] == 2 and pc_loc[1] == 2:
            EDelete()
            Dialogfenster(root, parent_frame, character="Gottfried")

    def vor():
        new_y = pc_loc[1] + 1
        
        if (pc_loc[0], new_y) in grid:
            pc_loc[1] = new_y
            action = grid[(pc_loc[0], pc_loc[1])]
            Dialog.update_text(action)
            coord.delete(1.0, tk.END)
            coord.insert(tk.END, " Location: " + str(pc_loc))
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
        
        def WaldButton(root, parent_frame):
            EDelete()
            Map.destroy()
            Wald.forest(root, parent_frame)
           
        def SumpfButton(root, parent_frame):
            EDelete()
            Map.destroy()
            Sumpf.swamp(root, parent_frame)


            
        def HoehleButton(root, parent_frame):
            EDelete()
            Map.destroy()
            Hoehle.cave(root, parent_frame)

        def EbeneButton(root, parent_frame):
            EDelete()
            Map.destroy()
            Ebene.plain(root, parent_frame)
            
        def ZVeridiaButton(root, parent_frame):
            EDelete()
            Map.destroy()
            ZVeridia.zveridia(root, parent_frame)
            
        def KuesteButton(root, parent_frame):
            EDelete()
            Map.destroy()
            Kueste.coast(root, parent_frame)
        
        Wald_Button = tk.Button(Map, text="Forest", command=lambda: WaldButton(root, parent_frame))
        Wald_Button.place(x=370, y=300) 
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
    # Der "Betrachten" Button
    betrButton = ttk.Button(root, text="EXAMINE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=examine)
    betrButton.place(x=130, y=680)

    # Der "Untersuchen" Button
    untButton = ttk.Button(root, text="TOUCH", padding=(50, 10), width=button_width, style="TNR.TLabel", command=touch)
    untButton.place(x=390, y=680)

    # Der "Wahrnehmen" Button
    whrButton = ttk.Button(root, text="PERCEIVE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=perceive)
    whrButton.place(x=650, y=680)

    # Der "Aufheben" Button
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
    loc.insert(tk.END, "Veridia")
    coord.place(x=20, y=440)    
    loc.place(x=1115, y=440)
    root.mainloop()
    return root

current_index = -1

def Dialogfenster(root, parent_frame, character):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    #Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    vrd_pfad = Image.open(Brigitte)
    vrd_image = ImageTk.PhotoImage(vrd_pfad)
    vrd_label = tk.Label(root, image= vrd_image)
    vrd_label.place(x=210, y=30) 
    
    def back():
        dlg1_Button.place_forget()
        dlg2_Button.place_forget()
        vrd_label.place_forget()
        rt_Button.place_forget()
        explore(root, parent_frame)
    
    #Leitet den Textboxmanager ein
    Dialog = TextboxManager(parent_frame)

    #Bestimmt bei welchem Charakter welches Bild verwendet werden soll
    if character == "Brigitte":
        values = [Brigitte_1, Brigitte_2, Brigitte_3, Brigitte_4, Brigitte_5, Brigitte_6]
        char_image = PhotoImage(file=Brigitte)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
        
    elif character == "Miriam":
        values = [Miriam_1, Miriam_2, Miriam_3, Miriam_4, Miriam_5]
        char_image = PhotoImage(file=Miriam)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
    elif character == "Ulrich":
        values = [Ulrich_1, Ulrich_2, Ulrich_3, Ulrich_4, Ulrich_5, Ulrich_6, Ulrich_7, Ulrich_8, Ulrich_9]
        char_image = PhotoImage(file=Ulrich)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
    elif character == "Gottfried":
        values = [Gottfried_1, Gottfried_2, Gottfried_3, Gottfried_4, Gottfried_5, Gottfried_6]
        char_image = PhotoImage(file=Gottfried)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)

    def dialogmanager(dialog_index):
        
        global current_index

        if 0 <= dialog_index < len(values):
            value_to_display = values[dialog_index]
            Dialog.update_text(value_to_display)
            current_index = dialog_index
        else:
            print("Falscher Dialogindex")

    dialogmanager(0)    
    button_width = 18
     # Der "Next" Button
    dlg1_Button = ttk.Button(root, text="NEXT DIALOGUE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=lambda: dialogmanager(current_index + 1))
    dlg1_Button.place(x=250, y=680)

    # Der "Back" Button
    dlg2_Button = ttk.Button(root, text="LAST DIALOGUE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=lambda: dialogmanager(current_index - 1))
    dlg2_Button.place(x=750, y=680)

    #Der Return Button
    rt_pfad = Image.open(arrowReturn)
    rt_image = ImageTk.PhotoImage(rt_pfad)
    rt_Button = ttk.Button(root, image=rt_image, command = back)
    rt_Button.place(x=1160, y=670)

    root.mainloop()
    return root