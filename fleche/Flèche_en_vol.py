position_fleche = 0
distance = 30 # en mètre
vitesse_fleche = 2 # en mètre par seconde
for i in range(int(distance/vitesse_fleche)): # le temps = distance/vitesse (en seconde)
    while position_fleche < distance:
        i += 1
        distance -= vitesse_fleche
        print(f"à {i} seconde la flèche est à ", distance , "m de la cible")

