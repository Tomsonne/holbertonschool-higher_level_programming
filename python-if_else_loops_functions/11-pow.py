#!/usr/bin/python3
def pow(a, b):
    resultat = 1

    if b == 0:
        return 1
    elif b > 0:
        for _ in range(b):
            resultat *= a
    else:  # si l'exposant est négatif
        for _ in range(-b):
            resultat *= a
        resultat = 1 / resultat

    return resultat
