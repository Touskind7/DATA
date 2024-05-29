liste = ['janvier', "fevrier", "mars", "avril", "mai", "juin", "juillet"]
#AJOUTER
liste.append('AOUT')
#supprimer
liste.remove("mai")
#copier
liste.copy()
liste.insert(1, "septembre")
liste.reverse()
liste.sort()
#print(liste.count("mars")


print(liste)
liste.reverse(
)
print(liste)

for index, mois in enumerate(liste):
    print(index, mois)
    if mois != "fevrier":
        print(mois)



while len(liste[4]) == len(liste):
    print(liste)