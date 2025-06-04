#!/usr/bin/python3
"""My class module"""


def pascal_triangle(n):
    """
    Retourne
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for ligne in range(1, n):
        nouvelle_ligne = [1]
        ligne_precedente = triangle[ligne - 1]
        for colonne in range(1, ligne):
            valeur = ligne_precedente[colonne - 1] + ligne_precedente[colonne]
            nouvelle_ligne.append(valeur)
        nouvelle_ligne.append(1)
        triangle.append(nouvelle_ligne)

    return triangle
