# coding: utf-8
## --- Utilisation des fenêtres Tkinter pour un dessin inter-actif --- ##
import tkinter as tk
from random import choice

## VARIABLES GLOBALES ##
init = (10, 190, 190, 10)
x1, x2, y1, y2 = init     # Initialisation des coordonnées des extrémités des lignes
palette = ["cyan", "purple", "maroon", "green", "red", 
           "blue", "orange", "yellow", "dark green"]
line_color = ""        # Instantiation de la variable

## DEFINITION DES FONCTIONS ##
def drawLine():
    '''Tracé d'une linge dans le canevas can1'''
    global x1, y1, x2, y2, line_color
    dessinCan.create_line(x1, y1, x2, y2, width=2, fill=line_color)
    y1 = y1-10 if y1>10 else 190  # Bien comprendre ces deux lignes (conditions ternaires)
    y2 = y2+10 if y1<190 else 10

def changeCouleurAlea():
    '''Changement aléatoire de la couleur du tracé'''
    global line_color
    line_color = choice(palette)

def remplisDessin():
    ''' Remplissage complet avec des couleurs aléatoires de la zone de dessin'''
    # Completer la fonction 

def clear():
    ''' Nettoyage du canevas'''
    dessinCan.delete(tk.ALL)

## --- MAIN PROGRAM --- ##
changeCouleurAlea()         # Initialisation de la couleur de la lignes

# Initialisation de la fenetre graphique
mainFen = tk.Tk()
mainFen['bg'] = "#9E9E9E"
mainFen.geometry('400x200')
mainFen.title("Traceur aleatoire de lignes")

# Initialisation du canevas
dessinCan = tk.Canvas(mainFen, bg='#EEEEEE', height=200, width=200,
                      bd=0, highlightthickness=0)   # Rechercher le rôle de highlightthickness
# dessinCan['borderwidth'] = 10        # Tester en décommentant ces 2 lignes
# dessinCan['relief'] = "groove"       # Que peut-on en déduire pour les coordonnées ?
# dessinCan.pack(side=tk.LEFT, padx=5, pady=5) # Même question !
dessinCan.pack(side=tk.LEFT)

# Bouton QUITTER
quitBtn = tk.Button(mainFen,
                 text = "Quitter",
                 width = 15,
                 command = mainFen.destroy)
quitBtn.pack(side=tk.BOTTOM, pady=5)

# Bouton EFFACER
clearBtn = tk.Button(mainFen,
                  text = "Effacer",
                  width = 15,
                  command = clear)
clearBtn.pack(side=tk.BOTTOM, pady=5)

# Bouton TRACER UNE LIGNE
traceBtn = tk.Button(mainFen,
                  text="Nouvelle ligne",
                  width = 15,
                  command=drawLine)
traceBtn.pack(pady=5)

# Bouton CHANGER LA COULEUR
coulBtn = tk.Button(mainFen,
                 text="Autre couleur",
                 width = 15,
                 command=changeCouleurAlea)
coulBtn.pack(pady=5)

# Bouton REMPLIR LE CANEVAS
# Compléter le code ici pour obtenir le visuel et l'effet escompté

mainFen.mainloop()