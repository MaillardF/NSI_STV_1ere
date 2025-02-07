import tkinter as tk

## --- VARIABLES GLOBALES --- ##
identifiants = {'Naruto': 'Ramen', 'Kakashi': "1000Oiseaux", 'Sakura': 'Sasuke'}
user_name = ''
user_pwd = ''

## --- FONCTIONS --- ##
def valide(event):
    user_name = userEntry.get() # Récupération des entrées clavier
    user_pwd = pwdEntry.get()
    # Compléter le reste de la fonction ici !
    pass

## --- FENETRE PRINCIPALE --- ##
mainFen = tk.Tk()

userLbl = tk.Label(mainFen, text='User Last Name :')
userLbl.grid(row=1, sticky=tk.E)

pwdLbl = tk.Label(mainFen, text='Password :')
pwdLbl.grid(row=2, sticky=tk.E)

accueilLbl = tk.Label(mainFen, text='Merci de vous identifier ci-dessous :')
accueilLbl.grid(row=0, sticky=tk.W, columnspan=2)

valideLbl = tk.Label(mainFen, text='Enregistrez-vous !', 
                       width=20, height=3,
                       justify=tk.CENTER, 
                       bg='#fef5e7',
                       bd=5, relief=tk.GROOVE)
valideLbl.grid(row=0, column=2, rowspan=3)

userEntry = tk.Entry(mainFen)
userEntry.grid(row=1, column=1)
userEntry.focus_set()   # Le widget a le focus au demarrage 

pwdEntry = tk.Entry(mainFen, show='*')
pwdEntry.grid(row=2, column=1)
pwdEntry.bind('<Return>', valide) # L'écoute de l'appui sur la touche Entrée
                                  # oblige la fonction valide à avoir un argument



mainFen.mainloop()
