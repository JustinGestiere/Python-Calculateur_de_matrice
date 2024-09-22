print ('''
       ---------------------------------------------------------------------------------------------------------
       Nous allons calculer des matrices merci de completer le tableau A et B afinc de calculer les valeurs de C
       ---------------------------------------------------------------------------------------------------------
       ''')

o = 0

while o != 1:
    choixuser = input('''
     ------------------------
     | 1. Calculer          |
     | 2. Sortir            |
     ------------------------                
     ''')
    
    
    if choixuser == "1":
        print("Debut du calcul")


        operateur = input("Entrer un opérateur entre +, - ou * en fonction de si vous voulez additionner, soustraire ou multiplier : ")

        if operateur in ["+", "-", "*"]:
            taille_ligne_A = int(input("Entrer le nombre de ligne du tableau A : "))
            taille_colonne_A = int(input("Entrer le nombre de colonne du tableau A : "))
            taille_ligne_B = int(input("Entrer le nombre de ligne du tableau B : "))
            taille_colonne_B = int(input("Entrer le nombre de colonne du tableau B : "))

            A = []
            B = []
            C = []
            

            for i in range(1, taille_ligne_A + 1):
                ligne = []
                for j in range(1, taille_colonne_A + 1):
                    valeur = int(input("Entrez la valeur du tableau A pour la case [{}, {}] : ".format(i, j)))
                    ligne.append(valeur)
                A.append(ligne)

            for i in range(1, taille_ligne_B + 1):
                ligne = []
                for j in range(1, taille_colonne_B + 1):
                    valeur = int(input("Entrez la valeur du tableau B pour la case [{}, {}] : ".format(i, j)))
                    ligne.append(valeur)
                B.append(ligne)


            # Afficher le tableau rempli par l'utilisateur
            print("\nTableau A :")
            for ligne in A:
                print(ligne)

            print("\nTableau B :")
            for ligne in B:
                print(ligne)


            if operateur == "+":
                # Addition des tableaux A et B pour obtenir C
                for i in range(len(A)):
                    ligne_somme = []
                    for j in range(len(A[0])):
                        somme = A[i][j] + B[i][j]
                        ligne_somme.append(somme)
                    C.append(ligne_somme)
                
                # Affichage du résultat C
                print("\nTableau C (Résultat de l'addition A et B) :")
                for ligne in C:
                    print(ligne)

            
            elif operateur == "-":
                # Addition des tableaux A et B pour obtenir C
                for i in range(len(A)):
                    ligne_somme = []
                    for j in range(len(A[0])):
                        somme = A[i][j] - B[i][j]
                        ligne_somme.append(somme)
                    C.append(ligne_somme)
                
                # Affichage du résultat C
                print("\nTableau C (Résultat de la soustraction A et B) :")
                for ligne in C:
                    print(ligne)

        else :
            print("Erreur vous n'avez pas saisi la bonne valeur, vous devez saisir + , - ou *")


    elif choixuser == "2":
         print("Fin du calcul")
         o += 1


    else:
         print("Erreur vous devez saisir 1 ou 2")
