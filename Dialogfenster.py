import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager
from Charaktere import Charakter

def Dialogfenster(root, parent_frame):
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
    
    Dialog = TextboxManager(parent_frame)
    Dialog.update_text(Einleitung)
    
    def test():
        brigitte = Charakter("Brigitte", "Willkommen!") 

        new_image = PhotoImage(file=Morast)
        vrd_label.config(image=new_image)
        vrd_label.image = new_image
        vrd_label.place(x=210, y=30)
        dlg1_Button.configure(text="Anders")
        Dialog.update_text(brigitte.einleitung)
        
        print("test")
    
    button_width = 15
     # Der "Dialog_1" Button
    dlg1_Button = ttk.Button(root, text="DIALOGUE_1", padding=(50, 10), width=button_width, style="TNR.TLabel", command=test)
    dlg1_Button.place(x=130, y=680)

    # Der "Dialog_2" Button
    dlg2_Button = ttk.Button(root, text="DIALOGUE_2", padding=(50, 10), width=button_width, style="TNR.TLabel")
    dlg2_Button.place(x=390, y=680)

    # Der "Dialog_3" Button
    dlg3_Button = ttk.Button(root, text="DIALOGUE_3", padding=(50, 10), width=button_width, style="TNR.TLabel")
    dlg3_Button.place(x=650, y=680)

    # Der "Verlassen" Button
    leave_Button = ttk.Button(root, text="LEAVE", padding=(50, 10), width=button_width, style="TNR.TLabel")
    leave_Button.place(x=910, y=680)

    root.mainloop()
    return root