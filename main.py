import tkinter as tk


def main():
    def transform(nombre):
        listChiffreRomain = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"],
                             [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        # tableau des chiffres romains
        # les "doubles" chiffres sont utilisés pour simplifier le programme après

        resultat = []
        compteur = 0

        while nombre != 0:  # on continu tant que le chiffre a convertir n'est pas à 0
            while listChiffreRomain[compteur][0] > nombre:  # on cherche le premier chiffre romain (donc le plus haut)
                compteur += 1

            resultat.append(listChiffreRomain[compteur][1])  # ajout du chiffre romain au résultat
            nombre -= listChiffreRomain[compteur][
                0]  # soustraction du chiffre qui a été ajouter au résultat pour ne plus le prendre en compte

        return resultat

    def check_convertir():  # valider le nombre a convertir
        def restart():  # restart l'app
            window.destroy()
            main()

        frame.pack_forget() # retire les anciens widget
        button.pack_forget()
        label_resultat = tk.Label(window, text=transform(int(entry_nbr.get())), font=("Arial", 12)) # affiche le resultat
        label_resultat.pack()
        button_restart = tk.Button(window, text="Recommencer", font=("Arial", 12), command=restart) # affiche le button de restart
        button_restart.pack()

    window = tk.Tk()    #creation et reglage de la fenetre
    window.title("PyRomain")
    window.geometry("500x300")
    window.resizable(width=False, height=False)

    label_title = tk.Label(window, text="Nombre arabe vers romain", font=("Arial", 20)) # affiche titre
    label_title.pack()

    frame = tk.Frame(window)    # frame pour label et entry du nombre
    label_nbr = tk.Label(frame, text="Nombre à convertir :", font=("Arial", 12))
    label_nbr.grid(row=0, column=0)
    entry_nbr = tk.Entry(frame, font=("Arial", 12))
    entry_nbr.grid(row=0, column=1)
    frame.pack()

    button = tk.Button(window, text="Convertir", font=("Arial", 12), command=check_convertir)   # affiche bouton pour validation
    button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()
