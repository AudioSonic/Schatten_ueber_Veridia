from tkinter import dialog
from Bilder import * 
import Dialoge
import Erkunden_Ebene
import Erkunden_Hoehle
import Erkunden_Kueste
import Erkunden_Sumpf
import Erkunden_Wald


def mobs(root, parent_frame):
    
    def Wolf():
        Erkunden_Ebene.plain(root, parent_frame)
        Erkunden_Ebene.reset()
    
    def Gouhl():
        Erkunden_Kueste.coast(root, parent_frame)
        Erkunden_Kueste.reset()
    
    def Berserk():
        Erkunden_Sumpf.swamp(root, parent_frame)
        Erkunden_Sumpf.reset()
    
    def Rider():
        Erkunden_Wald.forest(root, parent_frame)
        Erkunden_Wald.reset()
    
    def Undead():
        Erkunden_Hoehle.cave(root, parent_frame)
        Erkunden_Hoehle.reset()
    return Undead, Rider, Gouhl, Wolf, Berserk


# Verschiedne Gegner
Malikar_Boss = [300, 20, 30, 40, Malikar, Dialoge.Malikar_Dialog, "Malikar",0]
Varoth_Boss = [150, 15, 20, 30, Varoth, Dialoge.Varoth_Dialog, "Varoth",0]
Zyrelia_Boss = [200, 10, 15, 25, Zyrelia, Dialoge.Zyrelia_Dialog, "Zyrelia",0]
Malkor_Boss = [175, 5, 15, 40, Malkor, Dialoge.Malikar_Dialog, "Malkor",0]
Dazenar_Boss = [150, 10, 20, 20, Dazenar, Dialoge.Dazenar_Dialog, "Dazenar",0]
Vorluna_Boss = [170, 10, 20, 30, Vorluna, Dialoge.Vorluna_Dialog, "Vorluna",0]
Gegner_Ebene = [100, 5, 10, 10, Gegner_Ebene, Dialoge.Gegner_Ebene_Dialog, "Wolf", mobs(None, None)[3]]
Gegner_Hoehle = [70, 10, 15, 20, Gegner_Hoehle, Dialoge.Gegner_Hoehle_Dialog, "Undead", mobs(None, None)[0]]
Gegner_Kueste = [80, 10, 10, 20, Gegner_Kueste, Dialoge.Gegner_Kueste_Dialog, "Gouhl", mobs(None, None)[2]]
Gegner_Morast = [90, 5, 10, 30, Gegner_Morast, Dialoge.Gegner_Morast_Dialog, "Berserk", mobs(None, None)[4]]
Gegner_Wald = [60, 10, 20, 20, Gegner_Wald, Dialoge.Gegner_Wald_Dialog, "Rider", mobs(None, None)[1]]