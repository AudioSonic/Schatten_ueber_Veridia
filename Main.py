import tkinter as tk
from tkinter import ttk
from Bilder import *
from Erkunden import explore

def main():
    root = tk.Tk()
    root.title("Main")
    root.geometry("1300x750")
    root.resizable(False, False)
    root.configure(bg="#6B6B6B")
    root.attributes("-fullscreen", False)

    # Erstelle ein Frame, um den Inhalt der explore-Funktion anzuzeigen
    content_frame = tk.Frame(root, bg="#6B6B6B")
    content_frame.pack(fill=tk.BOTH, expand=True)

    def ErkundenButtonClicked():
        explore(root, content_frame)
        ErkundungsButton.pack_forget()  # Blende den Button nach dem Klicken aus

    ErkundungsButton = tk.Button(root, text="Erkundung", command=ErkundenButtonClicked)
    ErkundungsButton.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
