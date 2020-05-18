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
            nombre -= listChiffreRomain[compteur][0]    # soustraction du chiffre qui a été ajouter au résultat pour ne plus le prendre en compte

        return resultat

    print(transform(int(input("Nombre a traduire : "))))


if __name__ == '__main__':
    main()
