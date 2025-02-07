import tkinter as tk
from time import sleep
 
def clic_gauche(event):
    x, y = event.x, event.y
    chaine.configure(text = f"Clic détecté en X = {x} Y = {y}")
    cadre.delete(tk.ALL)
    cadre.create_oval(x-5, y-5, x+5, y+5, outline='red', tag='red_circle')

 
fen = tk.Tk()
cadre = tk.Canvas(fen, width =200, height =150, bg="light yellow")
cadre.bind("<Button-1>", clic_gauche)
cadre.pack()
chaine = tk.Label(fen)
chaine.pack()
 
fen.mainloop()