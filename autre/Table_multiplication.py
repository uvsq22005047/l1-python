"""
programme des tables des multiplications:
"""

#1ere méthode:

m = int(input("Pour quel entier voulez-vous voir la table de multiplication ? "))
print("voici la table de", m,":","\n", list(range(0,m*10+1,m)))

#2de méthode:

m = int(input("Pour quel entier voulez-vous voir la table de multiplication ? "))
print(list(m*i for i in range(11)))