import tkinter as tk

## --- FONCTIONS --- ##
def suppr(event):
    clic = event.x, event.y
    bord = can.find_closest(*clic)
    print(bord, type(bord))
    can.delete(bord)

def trace():
    for i in range(20):
        for j in range(20):
            can.create_line((i*30, j*30), ((i+1)*30, j*30),
                            fill='red', width=4)
            can.create_line((j*30, i*30), (j*30, (i+1)*30),
                            fill='grey', width=4)    

## --- FENETRE PRINCIPALE --- ##
fen = tk.Tk()
can = tk.Canvas(fen, width=600, height=600, background="ivory")
can.pack()

trace()
can.bind("<Button-1>", suppr)

fen.mainloop()