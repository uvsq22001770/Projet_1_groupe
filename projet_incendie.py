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

etape = 0

#########################################
# définition des fonctions
# docstring pour chaque fonction

def clic(event):
    """Reprend les coordonnées de la parcelle sur laquelle on a cliqué en premier"""
    if 0 >= event.x >= LARGEUR and 0 >= event.y >= HAUTEUR :
        i = (int(event.x / 30))
        j = (int(event.y / 30))
        pass######################fonction qui remplace par une case rouge
            ######################

def coordonnes_cellules_proche(i, j):
    coordonnees = []
    if i != 0:
        coordonnees.extend([((i-1), j)])
    if i != 39:
        coordonnees.extend([((i+1), j)])
    if j != 0:
        coordonnees.extend([(i, (j-1))])
    if j != 17:
        coordonnees.extend([(i, (j+1))])
    return coordonnees

def couleur_aleatoire():
    """fonction donnant une couleur aléatoire lors de la création du terrain 
    (couleurs possibles => bleu = "#02079c", vert = "#056608", jaune = "#ff9d00")"""
    x = rd.randint(0,2)
    global couleur

    if x == 0:
        couleur = "#02079c" #bleu
        return couleur
    elif x == 1:
        couleur = "#ff9d00" #jaune
        return couleur
    elif x == 2:
        couleur = "#056608" #vert
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
    

def passer_etape(i,j):
    """fonction qui réduit de 1 le temps dans la fonction chara"""
    global chara
    chara[i][j] = (chara[i][j][0], chara[i][j][1], chara[i][j][2] - 1)
    return chara[i][j][2]

def transformer_terrain(liste) :
    for n in range(0, len(liste)) :
        if liste[n][2] == "red":
            pass######################fonction qui remplace par une case rouge
                ######################
        elif liste[n][2] == "black":
            pass######################fonction qui remplace par une case noire
                ######################
        elif liste[n][2] == "grey":
            pass######################fonction qui remplace par une case grise
                ######################


def proba_feu(x) :
    y = rd.randint(1,10)
    if x >= y :
        return True


def effect_étape():
    global etape 
    changement = []
    etape += 1
    
    for i in range(0,40):
        for j in range(0,18):
            
            #foret
            if "#056608" in chara[i][j] :
                liste = coordonnes_cellules_proche(i, j)
                voisin_feu = 0
                for n in range(0, len(liste)) :
                    if "red" in chara[liste[n][0]][liste[n][1]] :
                        voisin_feu += 1
                if proba_feu(voisin_feu) == True:
                    changement.append([i,j,"red"])
                    
            #feu
            elif "red" in chara[i][j]:
                if passer_etape(i, j) == 0 :
                    changement.append([i,j,"grey"])
                
                liste = coordonnes_cellules_proche(i, j)
                for n in range(0, len(liste)) :
                    if "#ff9d00" in chara[liste[n][0]][liste[n][1]] :
                        changement.append([liste[n][0],liste[n][1],"red"])
            
            
            
            #cendres
            elif "grey" in chara[i][j]:
                if passer_etape(i, j) == 0:
                    changement.append([i,j,"black"])      
    transformer_terrain(changement)


                    
def demar_simulation():
    pass
    
def stop_simulation():
    pass

def acceleration():
    pass

def ralentissement():
    pass

#########################################
# programme principal

racine=tk.Tk()

TERRAIN = tk.Canvas(racine, bg="white", height=HAUTEUR, width=LARGEUR)


#########################################
# définition des widgets

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
TERRAIN.bind("<Button-1>", clic)

racine.mainloop()