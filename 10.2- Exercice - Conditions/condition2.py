# Problème : Déterminer si une année est bissextile ou non. Pour cela, il faut avoir ces règles en tête :
#                   Si une année n'est pas multiple de 4, on s'arrête là, elle n'est pas bissextile.
#                   Si elle est multiple de 4, on regarde si elle est multiple de 100.
#                       Si c'est le cas, on regarde si elle est multiple de 400.
#                           Si c'est le cas, l'année est bissextile.
#                           Sinon, elle n'est pas bissextile.
#                       Sinon, elle est bissextile.
#
# Résultat attendu : Un message affichant "Année bissextile" ou "Année non bissextile"

année = 200
print(année%4)
print(année%100)
print(année%400)

if(année%4 == 0) :
   if(année%100) == 0 and (année%400) == 0 :
       print("Année bissextile")
   else:
       print("Année non bissextile")
else:
    print("Année non bissextile")




#Modulo = renvoie le reste d'une division. Dans le cas ou le modulo renvoie 0, c'est que le dividende est multiple du diviseur
#Sources : https://openclassrooms.com/forum/sujet/verifier-si-un-nombre-est-entier-ou-decimal-12277

