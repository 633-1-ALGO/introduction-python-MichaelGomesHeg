# Problème : Réaliser une table de multiplication de taile 10x10 en utilisant la liste fournie.
# Résultat attendu : un affichage comme ceci :   1  2  3  4  5  6  7  8  9  10
#                                             1  1  2  3  4  5  6  7  8  9  10
#                                             2  2  4  6  8  10 12 14 16 18 20
#                                             . .  .  .  .  .  .  .  .  .  .
# Indication :   L'alignement rectiligne n'est pas une contrainte, tant que la table est visible ligne par ligne c'est ok.
#               Si vous êtes perfectionnistes faites vous plaisir.

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = 0

while num <= len(liste)-1:
    num = liste[num]
    for i in range(1, len(liste) + 1):
        print(num * i, " multiple de ", num)
    print("__________")



#def multiplication(liste):
#    i = 0
#    while i <=10:
#        multiple = i * liste
#        print(multiple)
#        i = i+1

#multiplication(10)



