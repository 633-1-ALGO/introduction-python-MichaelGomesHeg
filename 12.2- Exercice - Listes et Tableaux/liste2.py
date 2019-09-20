# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]



Max = 0

for grandTab in tab:
    for donneeDansTab in grandTab:
        if Max < donneeDansTab:
            Max = donneeDansTab



print("La valeur maximum est : ", Max, " et elle se trouve à l'indice ")




#a = max(tab[0]);
#b = max(tab[1]);
#c = max(tab[2]);


#Formule max et min : https://emilypython.wordpress.com/2018/11/06/listes-de-nombres-en-python-maximum-et-minimum/


