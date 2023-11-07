import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager
import Erkunden as Veridia
import Erkunden_ZVeridia

def Endboss(root, parent_frame):
    #Erstellt einen Stil f�r die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    vrd_pfad = Image.open(ZVeridia)
    vrd_image = ImageTk.PhotoImage(vrd_pfad)
    vrd_label = tk.Label(root, image= vrd_image)
    vrd_label.place(x=210, y=30) 
    
    #Leitet den Textboxmanager ein
    Dialog = TextboxManager(parent_frame)

    #Bestimmt bei welchem Charakter welches Bild verwendet werden soll
    values = [Boss_2, Boss_3, Boss_4]

    def dialogmanager(dialog_index):
        global current_index

        if 0 <= dialog_index < len(values):
            value_to_display = values[dialog_index]
            Dialog.update_text(value_to_display)
            current_index = dialog_index
        elif current_index == 0:
            current_index += 1
        else:
            dlg1_Button.place_forget()
            dlg2_Button.place_forget()
            vrd_label.place_forget()
            Erkunden_ZVeridia.zveridia(root, parent_frame)

    dialogmanager(0)    
    button_width = 18
     # Der "Next" Button
    dlg1_Button = ttk.Button(root, text="NEXT DIALOGUE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=lambda: dialogmanager(current_index + 1))
    dlg1_Button.place(x=250, y=680)

    # Der "Back" Button
    dlg2_Button = ttk.Button(root, text="LAST DIALOGUE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=lambda: dialogmanager(current_index - 1))
    dlg2_Button.place(x=750, y=680)

    root.mainloop()
    return root

