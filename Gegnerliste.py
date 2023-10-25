from tkinter import dialog
from Bilder import * 
import Dialoge
import Erkunden_Ebene
import Erkunden_Hoehle
import Erkunden_Kueste
import Erkunden_Sumpf
import Erkunden_Wald
from Main import root
from Main import parent_frame





# Verschiedne Gegner
Malikar = [300, 20, 30, 40, Malikar, Dialoge.Malikar_Dialog, "Malikar",0]
Varoth = [150, 15, 20, 30, Varoth, Dialoge.Varoth_Dialog, "Varoth",0]
Zyrelia = [200, 10, 15, 25, Zyrelia, Dialoge.Zyrelia_Dialog, "Zyrelia",0]
Malkor = [175, 5, 15, 40, Malkor, Dialoge.Malikar_Dialog, "Malkor",0]
Dazenar = [150, 10, 20, 20, Dazenar, Dialoge.Dazenar_Dialog, "Dazenar",0]
Vorluna = [170, 10, 20, 30, Vorluna, Dialoge.Vorluna_Dialog, "Vorluna",0]
Gegner_Ebene = [100, 5, 10, 10, Gegner_Ebene, Dialoge.Gegner_Ebene_Dialog, "Wolf", Gegner_Ebene()]
Gegner_Hoehle = [70, 10, 15, 20, Gegner_Hoehle, Dialoge.Gegner_Hoehle_Dialog, "Undead", Erkunden_Hoehle()]
Gegner_Kueste = [80, 10, 10, 20, Gegner_Kueste, Dialoge.Gegner_Kueste_Dialog, "Gouhl", Erkunden_Kueste()]
Gegner_Morast = [90, 5, 10, 30, Gegner_Morast, Dialoge.Gegner_Morast_Dialog, "Berserk", Erkunden_Sumpf()]
Gegner_Wald = [60, 10, 20, 20, Gegner_Wald, Dialoge.Gegner_Wald_Dialog, "Rider", Erkunden_Wald()]



def Gegner_Ebene():
    Erkunden_Ebene.plain(root, parent_frame)
    Erkunden_Ebene.reset()
    
def Erkunden_Kueste():
    Erkunden_Kueste.coast(root, parent_frame)
    Erkunden_Kueste.reset()
    
def Erkunden_Sumpf():
    Erkunden_Sumpf.swamp(root, parent_frame)
    Erkunden_Sumpf.reset()
    
def Erkunden_Wald():
    Erkunden_Wald.forest(root, parent_frame)
    Erkunden_Wald.reset()
    
def Erkunden_Hoehle():
    Erkunden_Hoehle.cave(root, parent_frame)
    Erkunden_Hoehle.reset()