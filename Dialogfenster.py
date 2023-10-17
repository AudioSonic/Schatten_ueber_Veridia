import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager


current_index = 0
#character = ""

def Dialogfenster(root, parent_frame, character):
    for widget in parent_frame.winfo_children():
        widget.destroy()
    values = ["9", "8"]
    #Erstellt einen Stil für die Schrift. In dem Fall Times New Roman
    style = ttk.Style()
    style.configure("TNR.TLabel", font=("Times New Roman", 14))  

    # Hintergrundbild einfuegen
    vrd_pfad = Image.open(Brigitte)
    vrd_image = ImageTk.PhotoImage(vrd_pfad)
    vrd_label = tk.Label(root, image= vrd_image)
    vrd_label.place(x=210, y=30) 
    
    if character == "Brigitte":
        values = [Brigitte_2, Brigitte_3, Miriam_1, Ulrich_1]
        char_image = PhotoImage(file=Brigitte)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
        
    elif character == "Miriam":
        values = [Miriam_1, Brigitte_3, Miriam_1, Ulrich_1]
        char_image = PhotoImage(file=Miriam)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
    elif character == "Ulrich":
        char_image = PhotoImage(file=Ulrich)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
    elif character == "Gottfried":
        char_image = PhotoImage(file=Gottfried)
        vrd_label.config(image=char_image)
        vrd_label.image = char_image
        vrd_label.place(x=210, y=30)
    
    Dialog = TextboxManager(parent_frame)
    Dialog.update_text(Einleitung)

    def dialogmanager(dialog_index):
        
        global current_index

        if 0 <= dialog_index < len(values):
            value_to_display = values[dialog_index]
            Dialog.update_text(value_to_display)
            current_index = dialog_index
        else:
            print("Falscher Dialogindex")

            
    """       

    
        new_image = PhotoImage(file=Morast)
        vrd_label.config(image=new_image)
        vrd_label.image = new_image
        vrd_label.place(x=210, y=30)
        dlg1_Button.configure(text="Anders")
       
        
        print("test")
        """
        
    button_width = 18
     # Der "Next" Button
    dlg1_Button = ttk.Button(root, text="NEXT DIALOGUE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=lambda: dialogmanager(current_index + 1))
    dlg1_Button.place(x=250, y=680)

    # Der "Back" Button
    dlg2_Button = ttk.Button(root, text="LAST DIALOGUE", padding=(50, 10), width=button_width, style="TNR.TLabel", command=lambda: dialogmanager(current_index - 1))
    dlg2_Button.place(x=750, y=680)

    rt_pfad = Image.open(arrowReturn)
    rt_image = ImageTk.PhotoImage(rt_pfad)
    rt_Button = ttk.Button(root, image=rt_image)
    rt_Button.place(x=1160, y=670)

    root.mainloop()
    return root
