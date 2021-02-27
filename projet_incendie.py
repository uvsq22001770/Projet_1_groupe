#########################################
# groupe LDDMP 3
# Ismaël RAIS
# Ines ROSENTHAL
# Hajar ASBAI
# Adrien HANNA
# Quentin ASSIE
# Paula POP
# https://github.com/uvsq22001770/projet_incendie.git
#########################################

#########################################
# import des librairies

import tkinter as tk
import random as rd

#########################################
# définition des constantes

HAUTEUR = 540
LARGEUR = 1200

#########################################
# définition des variables globales

tuiles = []
chara = []

#########################################
# définition des fonctions
# docstring pour chaque fonction

def clic(event):
    """Transforme les parcelles de prairie ou de forêt en parcelles enflamées"""
    pass

def retourner_couleur(i,j):
    """ fonction prenant comme argument les coordonnées d'un objet et renvoie sa couleur"""

    if "blue" in(chara[i][j]):
        return "blue"

    elif "yellow" in(chara[i][j]):
        return "yellow"

    elif "green" in(chara[i][j]):
        return "green"  

    elif "black" in(chara[i][j]):
        return "black" 

    elif "grey" in(chara[i][j]) :
        return "grey"

    elif "red" in(chara[i][j]):
        return "red" 

def couleur_aleatoire():
    """fonction donnant une couleur aléatoire lors de la création du terrain (couleurs possibles = bleu, vert, jaune)"""
    x = rd.randint(0,2)
    global couleur

    if x == 0:
        couleur = "blue"
        return couleur
    elif x == 1:
        couleur = "yellow"
        return couleur
    elif x == 2:
        couleur = "green"
        return couleur


def generer_terrain():
    """ fonction génerant le terrain du debut de jeu et faisant entrer chaque tuile dans la liste "tuiles", les coordonnées(i;j) des triangles sont definies par tuiles[i][j]"""
    global tuiles
    global chara
    
    for i in range(0, 40):
        liste1 = []
        tuiles.append(liste1)

        liste2 = []
        chara.append(liste2)
        for j in range(0, 18):
            tuiles[i].append(TERRAIN.create_rectangle((i*30, j*30), (i*30 + 30, j*30 + 30), fill= couleur_aleatoire()))
            chara[i].append(((i,j), couleur, 0))   
      


def sauver_terrain():
    pass
    
def char_terrain():
    pass
    
def effect_étape():
    pass
    
def demar_simulation():
    pass
    
def stop_simulation():
    pass

def acceleration():
    pass

def ralentissement():
    pass

def demarrer_feu():
    pass

#########################################
# programme principal

racine=tk.Tk()

TERRAIN = tk.Canvas(racine, bg="white", height=HAUTEUR, width=LARGEUR)


#########################################
# définition des widgets

#canvas_eau=tk.Canvas(racine, bg="blue", height=100, width=100)
#canvas_foret=tk.Canvas(racine, bg="green", height=100, width=100)
#canvas_cendres=tk.Canvas(racine, bg="black", height=100, width=100)
#canvas_feu=tk.Canvas(racine, bg="red", height=100, width=100)
#canvas_prairie=tk.Canvas(racine, bg="yellow", height=100, width=100)
#canvas_cendrestiedes=tk.Canvas(racine, bg="grey", height=100, width=100)


GENERER_TERRAIN=tk.Button(racine,text="génerer terrain",font=("helvetica"),command=generer_terrain)
SAUV_TERRAIN=tk.Button(racine,text="sauvegarder terrain",font=("helvetica"),command=sauver_terrain)
CHAR_TERRAIN=tk.Button(racine,text="charger un terrain",font=("helvetica"),command=char_terrain)
EFF_ETAPE=tk.Button(racine,text="effectuer une étape",font=("helvetica"),command=effect_étape)
DEM_SIMU=tk.Button(racine,text="demarrer simulation",font=("helvetica"),command=demar_simulation)
STOP_SIMU=tk.Button(racine,text="stopper la simulation",font=("helvetica"),command=stop_simulation)


TERRAIN.grid(column= 0,row = 2, columnspan = 3)
GENERER_TERRAIN.grid(column = 0,row = 0)
SAUV_TERRAIN.grid(column = 1,row = 0)
CHAR_TERRAIN.grid(column = 2,row = 0)
EFF_ETAPE.grid(column = 0,row = 1)
DEM_SIMU.grid(column = 1,row = 1)
STOP_SIMU.grid(column = 2,row = 1)

#########################################
# définition des évènements

racine.bind("<KeyPress-a>", acceleration)
racine.bind("<KeyPress-r>", ralentissement)
racine.bind("<Button-1>", demarrer_feu)

racine.mainloop()