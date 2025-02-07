import tkinter as tk

## --- CONSTANTES GLOBALES --- ##
WIDTH = 400
HEIGHT = 200
COTE = 40

## --- VARIABLES GLOBALES --- ##
y_haut = HEIGHT/2 - COTE/2
debut_anim = 10
fin_anim = WIDTH - debut_anim

## --- FONCTIONS --- ##
def animer(speed):
    x1, x2 = cadre.coords("mobile")[::2]
    if x1 < debut_anim or x2 > fin_anim:
        speed = -speed
    cadre.move("mobile", speed, 0)
    cadre.after(25, animer, speed)


def changer_couleur(event):
    color = cadre.itemconfigure("mobile", "fill")[-1]
    print(cadre.itemconfigure("mobile", "fill"))
    if color == "red":
        color = "blue"
    else:
        color = "red"
    cadre.itemconfigure("mobile", fill=color)

## --- FENETRE PRINCIPALE --- ##
mainFen = tk.Tk()
cadre = tk.Canvas(mainFen, width=WIDTH, height=HEIGHT, background="ivory")
cadre.pack()

cadre.create_rectangle(debut_anim, y_haut, debut_anim+COTE, y_haut+COTE, fill="blue",
                     outline='', tag="mobile")

cadre.tag_bind("mobile", "<Button-1>", changer_couleur)

animer(speed=3)

mainFen.mainloop()