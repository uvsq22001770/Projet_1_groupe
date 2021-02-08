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

import tkinter as tk
import random
HAUTEUR = 700
LONGUEUR = 1000

racine=tk.Tk()
canvas = tk.Canvas(racine, bg="grey", height=HAUTEUR, width=LONGUEUR)

canvas_eau=tk.Canvas(racine, bg="blue", height=100, width=100)
canvas_foret=tk.Canvas(racine, bg="green", height=100, width=100)
canvas_cendres=tk.Canvas(racine, bg="black", height=100, width=100)
canvas_feu=tk.Canvas(racine, bg="red", height=100, width=100)
canvas_prairie=tk.Canvas(racine, bg="yellow", height=100, width=100)
canvas_cendrestiedes=tk.Canvas(racine, bg="grey", height=100, width=100)

def couleur():
    x = random.randint(0,2)
    if x == 0:
        return "blue"
    elif x == 1:
        return "yellow"
    elif x == 2:
        return "green"       



for i in range(0, 10):
    for j in range(0, 8):
        str(i)+str(j) = canvas.create_rectangle((i*100, j*100), (i*100 + 100, j*100 - 100), fill= couleur())


"""canvas_eau.grid(column=, row=)
canvas_foret.grid(column=, row=)
canvas_cendres.grid(column= , row=)
canvas_feu.grid(column= , row=)
canvas_prairie.grid(column= , row=)
canvas_cendrestiedes.grid(column= , row=)"""



canvas.grid()


racine.mainloop()