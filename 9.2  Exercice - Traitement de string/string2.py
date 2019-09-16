# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."

nbMot = texte.count("exemple");
print(nbMot);


print(texte[::-1])


#fonction bonus : 1) https://www.journaldev.com/23647/python-reverse-string (Méthode possible)
#                 2) https://www.developpez.net/forums/d1369758/autres-langages/python-zope/general-python/inverser-chaine/ (Solution utilisée)

# Information à propos du [::-1] : https://docs.python.org/release/2.3.5/whatsnew/section-slices.html
