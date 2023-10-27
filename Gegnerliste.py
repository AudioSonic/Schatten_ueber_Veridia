from tkinter import dialog
from Bilder import * 
import Dialoge
import Erkunden_Ebene
import Erkunden_Hoehle
import Erkunden_Kueste
import Erkunden_Sumpf
import Erkunden_Wald
 



# Verschiedne Gegner HP/Schadenszahlen/Bilder/Dialoge/Gegnername/Escapemöglichkeit/Besiegt/Dialogliste/Rückkehrort
Malikar_Boss = [100, 20, 30, 40, Malikar, Dialoge.Malikar_Dialog, "Malikar" ,6 ,1 ,1 ,3 ,9 ]
Varoth_Boss = [100, 15, 20, 30, Varoth, Dialoge.Varoth_Dialog, "Varoth", 7 ,1 ,1 ,7 ,17 ]
Zyrelia_Boss = [100, 10, 15, 25, Zyrelia, Dialoge.Zyrelia_Dialog, "Zyrelia" ,8 ,1 ,1 ,5 , 13]
Malkor_Boss = [100, 5, 15, 40, Malkor, Dialoge.Malkor_Dialog, "Malkor" ,9 ,1 ,1 ,6 , 14]
Dreznar_Boss = [100, 10, 20, 20, Dreznar, Dialoge.Dreznar_Dialog, "Dreznar" ,10 ,1 ,1 ,7 ,17 ]
Vorluna_Boss = [100, 10, 20, 30, Vorluna, Dialoge.Vorluna_Dialog, "Vorluna" ,11 ,1 ,1 ,6 ,15 ]
Gegner_Ebene = [100, 5, 10, 10, Gegner_Ebene, Dialoge.Gegner_Ebene_Dialog, "Wolf" ,5 ,1 ,1 ,10 ,25 ]
Gegner_Hoehle = [100, 10, 15, 20, Gegner_Hoehle, Dialoge.Gegner_Hoehle_Dialog, "Undead" ,4 ,1 ,1 ,14 ,36 ]
Gegner_Kueste = [100, 10, 10, 20, Gegner_Kueste, Dialoge.Gegner_Kueste_Dialog, "Ghoul" ,3 ,1 ,1 ,13 ,31 ]
Gegner_Sumpf = [100, 5, 10, 30, Gegner_Morast, Dialoge.Gegner_Morast_Dialog, "Berserk" ,2 ,1 ,1 ,11 ,28 ]
Gegner_Wald = [100, 10, 20, 20, Gegner_Wald, Dialoge.Gegner_Wald_Dialog, "Rider" ,1 ,1 ,1 ,17 ,42 ]

