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

HAUTEUR = 700
LARGEUR = 1000

#########################################
# définition des variables globales

#########################################
# définition des fonctions
# docstring pour chaque fonction

def clic(event):
    """Transforme les parcelles de prairie ou de forêt en parcelles enflamées"""
    pass

def couleur():
    x = rd.randint(0,2)
    if x == 0:
        return "blue"
    elif x == 1:
        return "yellow"
    elif x == 2:
        return "green"
    
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

### CODE POUR CREER LE QUADRILLAGE ###
for i in range(0, 10):
    for j in range(0, 8):
        TERRAIN.create_rectangle((i*100, j*100), (i*100 + 100, j*100 - 100), fill= couleur())

#########################################
# définition des widgets

canvas_eau=tk.Canvas(racine, bg="blue", height=100, width=100)
canvas_foret=tk.Canvas(racine, bg="green", height=100, width=100)
canvas_cendres=tk.Canvas(racine, bg="black", height=100, width=100)
canvas_feu=tk.Canvas(racine, bg="red", height=100, width=100)
canvas_prairie=tk.Canvas(racine, bg="yellow", height=100, width=100)
canvas_cendrestiedes=tk.Canvas(racine, bg="grey", height=100, width=100)


GENERER_TERRAIN=tk.Button(racine,text="génerer terrain",font=("helvetica"),command=couleur)
SAUV_TERRAIN=tk.Button(racine,text="sauvegarder terrain",font=("helvetica"),command=sauver_terrain)
CHAR_TERRAIN=tk.Button(racine,text="charger un terrain",font=("helvetica"),command=char_terrain)
EFF_ETAPE=tk.Button(racine,text="effectuer une étape",font=("helvetica"),command=effect_étape)
DEM_SIMU=tk.Button(racine,text="demarrer simulation",font=("helvetica"),command=demar_simulation)
STOP_SIMU=tk.Button(racine,text="stopper la simulation",font=("helvetica"),command=stop_simulation)


GENERER_TERRAIN.grid(column=0,row=0)
SAUV_TERRAIN.grid(column=0,row=1)
CHAR_TERRAIN.grid(column=0,row=2)
TERRAIN.grid(column=1,row=0, rowspan=3)
EFF_ETAPE.grid(column=2,row=0)
DEM_SIMU.grid(column=2,row=1)
STOP_SIMU.grid(column=2,row=2)

#########################################
# définition des évènements

racine.bind("<KeyPress-a>", acceleration)
racine.bind("<KeyPress-r>", ralentissement)
racine.bind("<Button-1>", demarrer_feu)

racine.mainloop()