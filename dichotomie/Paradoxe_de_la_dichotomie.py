# Purpose: Résoudre le paradoxe de la dichotomie
def ParadoxeDichotomie(distance_totale):
    distance = distance_totale # Distance restante à parcourir
    i = 0 # Nombre d'étapes

    while distance > 0.1: 
        """Arrêter lorsque l'étape devient très petite, 
        ce qui signifie que la pierre se rapproche suffisamment de l'arbre
          mais ne l'atteint jamais """
        distance = distance_totale / (2**i)
        print(f"Distance à l'étape {i} : {distance} mètres")
        i += 1

# Appel de la fonction avec un distance_totale de 20.0 mètres
ParadoxeDichotomie(20.0)
