print('''
---------------------------------------------------------------------------------------------------------
Nous allons calculer des matrices. Merci de compléter les tableaux A et B afin de calculer les valeurs de C.
---------------------------------------------------------------------------------------------------------
''')

o = 0

while o != 1:
    choixuser = input('''
     ------------------------
     | 1. Calculer          |
     | 2. Sortir            |
     ------------------------
     Choisissez une option : 
     ''')

    if choixuser == "1":
        print("Début du calcul")

        operateur = input("Entrez un opérateur parmi +, - ou * (addition, soustraction ou multiplication) : ")

        if operateur in ["+", "-", "*"]:
            try:
                # Saisie des dimensions des tableaux
                taille_ligne_A = int(input("Entrez le nombre de lignes du tableau A : "))
                taille_colonne_A = int(input("Entrez le nombre de colonnes du tableau A : "))
                taille_ligne_B = int(input("Entrez le nombre de lignes du tableau B : "))
                taille_colonne_B = int(input("Entrez le nombre de colonnes du tableau B : "))

                # Vérification des dimensions selon l'opérateur
                if operateur in ["+", "-"] and (taille_ligne_A != taille_ligne_B or taille_colonne_A != taille_colonne_B):
                    print("Erreur : Pour l'addition et la soustraction, les dimensions des matrices A et B doivent être identiques.")
                    continue
                if operateur == "*" and taille_colonne_A != taille_ligne_B:
                    print("Erreur : Pour la multiplication, le nombre de colonnes de A doit être égal au nombre de lignes de B.")
                    continue

                # Initialisation des matrices
                A = []
                B = []
                C = []

                print("\nRemplissage du tableau A :")
                for i in range(1, taille_ligne_A + 1):
                    ligne = []
                    for j in range(1, taille_colonne_A + 1):
                        valeur = int(input(f"Entrez la valeur du tableau A pour la case [{i}, {j}] : "))
                        ligne.append(valeur)
                    A.append(ligne)

                print("\nRemplissage du tableau B :")
                for i in range(1, taille_ligne_B + 1):
                    ligne = []
                    for j in range(1, taille_colonne_B + 1):
                        valeur = int(input(f"Entrez la valeur du tableau B pour la case [{i}, {j}] : "))
                        ligne.append(valeur)
                    B.append(ligne)

                # Affichage des tableaux remplis
                print("\nTableau A :")
                for ligne in A:
                    print(ligne)

                print("\nTableau B :")
                for ligne in B:
                    print(ligne)

                # Calcul en fonction de l'opérateur
                if operateur == "+":
                    for i in range(len(A)):
                        ligne_somme = []
                        for j in range(len(A[0])):
                            ligne_somme.append(A[i][j] + B[i][j])
                        C.append(ligne_somme)
                    print("\nTableau C (Résultat de l'addition A + B) :")
                
                elif operateur == "-":
                    for i in range(len(A)):
                        ligne_somme = []
                        for j in range(len(A[0])):
                            ligne_somme.append(A[i][j] - B[i][j])
                        C.append(ligne_somme)
                    print("\nTableau C (Résultat de la soustraction A - B) :")
                
                elif operateur == "*":
                    for i in range(len(A)):
                        ligne_produit = []
                        for j in range(len(B[0])):
                            produit = sum(A[i][k] * B[k][j] for k in range(len(B)))
                            ligne_produit.append(produit)
                        C.append(ligne_produit)
                    print("\nTableau C (Résultat de la multiplication A * B) :")

                # Affichage du résultat C
                for ligne in C:
                    print(ligne)

            except ValueError:
                print("Erreur : Vous devez entrer des nombres valides pour les dimensions et les valeurs des tableaux.")
        else:
            print("Erreur : Vous devez entrer un opérateur valide (+, -, *).")

    elif choixuser == "2":
        print("Fin du calcul. Au revoir !")
        o = 1

    else:
        print("Erreur : Vous devez saisir 1 ou 2.")
