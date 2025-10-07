def point_vie(hp,attaque, defence):
    """
    :fonction prend et calcul les points de vie après une attaque
    :param defence: le nombre de defence que le joueur peut prendre
    :param hp:le nombre de point de vie du joueur
    :param attaque: nombre de point d'attaque
    :return: nombre de vie restant
    """
    truedammage= defence-attaque
    hp-=truedammage
    return hp

"""
plan de test
| defense |  attaque |   hp  | resultat attendue | resultat obtenue |
| 55      | 25       |   40  |   25              |   25             |
|         | 90       |       |   90              |   90             |
|         | 40       |       |   40              |   40             |
"""