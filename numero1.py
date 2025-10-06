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

