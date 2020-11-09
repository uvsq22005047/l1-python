#temps = (4,3,5,7)
#seconde = temps[3]
#print(seconde)

#temps[0] : jours, temps[1]: minutes, temps[2]: minutes, temps[3]: secondes

def tempsEnSeconde(jour, heure, minute, seconde):
    #""" Renvoie la valeur en seconde de temps donné comme jour, heure, minute, seconde."""
    print(jour * 86400 + heure * 3600 + minute * 60 + seconde)


tempsEnSeconde(1,3,46,40)

def secondeEnTemps(seconde):
    #"""Renvoie le temps (jour, heure, minute, seconde) qui correspond au nombre de seconde passé en argument"""
    jour = seconde // 86400
    heure = (seconde % 86400) // 3600
    minute = ((seconde % 86400) % 3600) // 60
    seconde = ((seconde % 86400) % 3600) % 60
    print(jour, heure, minute, seconde)
    
secondeEnTemps(100000)



def afficheTemps(temps):
    if temps[0] > 1 :
        print(temps[) 
        
    if temps[1] > 1 :
        print("cs")
        
    if temps[2] > 1 :
        print("c")


print (temps[0], temps[1], temps[2], temps[3])

jour = "jour"
heure = "heure"
minnute = "minute"




afficheTemps((3,0,14,23))  