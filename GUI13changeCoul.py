import tkinter as tk

## --- VARIABLE GLOBALE --- ##
colors = ["pink", "lavender"]
index = 0

## --- FONCTIONS GENERALES ---  ##
def change_color():
    global index
    index = (index + 1) % 2
    color = colors[index]
    cadre.itemconfigure(rect, fill=color)    
    cadre.after(1000, change_color)

## --- MAIN WINDOW --- ##
mainFen = tk.Tk()
cadre = tk.Canvas(mainFen, width=200, height=200)
cadre.pack()

rect=cadre.create_rectangle((10, 10), (190, 190), fill="pink", outline='green')
cadre.after(1000, change_color)

print(rect)     # Affichage de l'identifiant numérique
mainFen.mainloop()