# TextboxManager.py
import tkinter as tk

class TextboxManager:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.text_output = None
        self.create_textbox()

    def create_textbox(self):
        # Textfeld für die Ausgabe
        self.text_output = tk.Text(self.parent_frame, height=6, width=90, wrap="none")
        self.text_output.place(x=18, y=470)
        self.text_output.config(state=tk.DISABLED)
        custom_font = ("Times New Roman", 20)
        self.text_output.config(font=custom_font)
        #Fügt eine Verzögerung hinzu, wie lange der Text bleiben soll
    def update_text(self, text, delay=0):
        self.text_output.config(state=tk.NORMAL)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, text)
        self.text_output.config(state=tk.DISABLED)


