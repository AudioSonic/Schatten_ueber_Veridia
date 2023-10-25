from tkinter import dialog
from Bilder import * 
import Dialoge
import Erkunden_Ebene
import Erkunden_Hoehle
import Erkunden_Kueste
import Erkunden_Sumpf
import Erkunden_Wald
 
 


# Verschiedne Gegner
Malikar_Boss = [300, 20, 30, 40, Malikar, Dialoge.Malikar_Dialog, "Malikar",0]
Varoth_Boss = [150, 15, 20, 30, Varoth, Dialoge.Varoth_Dialog, "Varoth",0]
Zyrelia_Boss = [200, 10, 15, 25, Zyrelia, Dialoge.Zyrelia_Dialog, "Zyrelia",0]
Malkor_Boss = [175, 5, 15, 40, Malkor, Dialoge.Malikar_Dialog, "Malkor",0]
Dazenar_Boss = [150, 10, 20, 20, Dazenar, Dialoge.Dazenar_Dialog, "Dazenar",0]
Vorluna_Boss = [170, 10, 20, 30, Vorluna, Dialoge.Vorluna_Dialog, "Vorluna",0]
Gegner_Ebene = [100, 5, 10, 10, Gegner_Ebene, Dialoge.Gegner_Ebene_Dialog, "Wolf",5]
Gegner_Hoehle = [70, 10, 15, 20, Gegner_Hoehle, Dialoge.Gegner_Hoehle_Dialog, "Undead",4]
Gegner_Kueste = [80, 10, 10, 20, Gegner_Kueste, Dialoge.Gegner_Kueste_Dialog, "Gouhl",3]
Gegner_Morast = [90, 5, 10, 30, Gegner_Morast, Dialoge.Gegner_Morast_Dialog, "Berserk",2]
Gegner_Wald = [60, 10, 20, 20, Gegner_Wald, Dialoge.Gegner_Wald_Dialog, "Rider", 1]