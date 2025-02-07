#coding: utf-8
## --- Réalisation d'un échiquer --- ##

import tkinter as tk
## --- Variables globales d'environnement -- ##
btn_width = 12

## --- Définition des fonctions
def draw_chess():
    ## Votre code ici ... 
    ## On utilisera la méthode create_rectangle() sur le canvas "can"
    pass
            

def draw_pion(event):
    col_num = (event.x) // 30
    line_num = (event.y) // 30
    print(col_num, line_num)
    can.create_oval(30*col_num + 5, 30*line_num + 5,
                    30*(col_num+1) - 5, 30*(line_num+1) - 5,
                    fill = 'red',
                    tag = 'pion')


def clear_chess():
    can.delete('pion')
    
## --- Fenêtre principale --- ###
mainFen = tk.Tk()
# mainFen.geometry('380x300')
mainFen.title('Echiquier')

## --- Canevas principal
can = tk.Canvas(mainFen,
             width=240, height=240,
             bg='#FEF5E7',)
can.grid(padx=10, pady=10, rowspan=3)
can.bind("<Button-1>", draw_pion)

## --- Boutton pour effacer les pions
clearBtn = tk.Button(mainFen, text='Effacer', command=clear_chess, width=btn_width)
clearBtn.grid(row=1,column=1, padx=10)

## --- Boutton quitter
quitBtn = tk.Button(mainFen, text='Quitter', command=mainFen.destroy, width=btn_width)
quitBtn.grid(row=2, column=1, padx=10)

## --- Dessin de l'échiquier
draw_chess()

## --- Boucle principale
mainFen.mainloop()
