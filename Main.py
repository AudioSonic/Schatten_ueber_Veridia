import tkinter as tk
from tkinter import ttk

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
betrButton.place(x=390, y=680)

#Der "Wahrnehmen" BUtton
whrButton = ttk.Button(root, text="WAHRNEHMEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
betrButton.place(x=650, y=680)

#Der "Aufheben" BUtton
aufhbButton = ttk.Button(root, text="AUFHEBEN", padding=(50, 10), width=button_width, style="TNR.TLabel")
betrButton.place(x=910, y=680)

#Der links Pfeil
linksPfeilBild = tk.PhotoImage(file="")
lnkPfeil = ttk.Button(root, )


root.mainloop()