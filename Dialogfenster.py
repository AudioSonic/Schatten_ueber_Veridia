import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Bilder import *
from Dialoge import *
from Dialogsystem import TextboxManager

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
        for widget in parent_frame.winfo_children():
            widget.destroy()
    
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

    rt_pfad = Image.open(arrowReturn)
    rt_image = ImageTk.PhotoImage(rt_pfad)
    rt_Button = ttk.Button(root, image=rt_image, command = back)
    rt_Button.place(x=1160, y=670)

    root.mainloop()
    return root
