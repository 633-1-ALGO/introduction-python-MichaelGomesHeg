# Problème : Etant donné un tableau A de "n" nombres réels, on demande la moyenne des nombres du tableau
# Données : un tableau A de n nombre réels
# Résultat attendu : Moyenne des nombres réels du tableau A
A = [1, 5, 15, 25, 10, 55, 50, 35]

somme = 0
cpt = 0
for elementTableau in A:
    somme = somme + elementTableau
    cpt = cpt +1;

moyenne = somme / cpt
print("Moyenne des nombres réels du tableau A :", moyenne)

