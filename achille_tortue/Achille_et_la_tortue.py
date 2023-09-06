def simulationParadoxe(vitesseAchille, vitesseTortue, distance):
    positionAchille = 0
    positionTortue = distance
    
    while distance  > positionAchille  :
        # Faire avancer Achille et la tortue en fonction de leurs vitesses
        positionAchille += vitesseAchille
        positionTortue += vitesseTortue
        print(f"Achille est à la position {positionAchille:.2f} mètres")
        print(f"La tortue est à la position {positionTortue:.2f} mètres")

# Vitesses en mètres par seconde
vitesseAchille = 9.0
vitesseTortue = 1.0

# Distance initiale entre Achille et la tortue
distance = 20.0

# Appel de la fonction de simulation
simulationParadoxe(vitesseAchille, vitesseTortue, distance)
