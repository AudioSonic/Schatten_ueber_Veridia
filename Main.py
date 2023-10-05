import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

#Das Interface
root = tk.Tk()
root.title("Schatten über Veridia")
root.geometry("1300x750")
root.resizable(False, False)
root.configure(bg="#6B6B6B")
root.attributes("-fullscreen", False)

# Erstellen Sie einen Stil für das Widget
style = ttk.Style()

# Ändern Sie die Schriftart im Stil
style.configure("TNR.TLabel", font=("Times New Roman", 14))  # Hier wird die Schriftart auf Helvetica mit Größe 14 gesetzt

#Setzt die Breite der Buttons fest
button_width = 15
#Der "Betrachten" Button
betrButton = ttk.Button(root, text="BETRACHTEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
betrButton.place(x=130, y=680)

#Der "Untersuchen" BUtton
untButton = ttk.Button(root, text="UNTERSUCHEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
untButton.place(x=390, y=680)

#Der "Wahrnehmen" BUtton
whrButton = ttk.Button(root, text="WAHRNEHMEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
whrButton.place(x=650, y=680)

#Der "Aufheben" BUtton
aufhbButton = ttk.Button(root, text="AUFHEBEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
aufhbButton.place(x=910, y=680)

#Der links Pfeil
linksPfeilBild = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Main\\Arrow_Left.png")
lnkPfeil = ttk.Button(root, image=linksPfeilBild)
lnkPfeil.place(x=18, y=350)

#Der rechts Pfeil
rechtsPfeilBild = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Main\\Arrow_Right.png")
rchtsPfeil = ttk.Button(root, image=rechtsPfeilBild)
rchtsPfeil.place(x=1200, y=350)

#Der front Pfeil
vorPfeilBild = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Main\\Arrow_Front.png")
vorPfeil = ttk.Button(root, image=vorPfeilBild)
vorPfeil.place(x=600, y=20)

#Der return Pfeil
returnPfeilBild = Image.open("C:\\GitHub\\Schatten_ueber_Veridia\\Main\\Arrow_Return.png")
photo = ImageTk.PhotoImage(returnPfeilBild)
returnPfeil = ttk.Button(root, image=photo)
returnPfeil.place(x=20, y=670)

#Die Karte
MapImage = tk.PhotoImage(file="C:\\GitHub\\Schatten_ueber_Veridia\\Main\\Map.png")
Map = ttk.Button(root, image=MapImage)
Map.place(x=1250, y=20)

root.mainloop()