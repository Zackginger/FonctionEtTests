#3. Fonction qui reçoit une liste de legos et
#qui retourne il y a combien de blocs de chaque couleur en moyenne

def liste_blocs_legos(liste_legos, couleur):

    """
    :param liste_legos: le nombre de blocs totales
    :param couleur: les couleurs des blocs
    :return: nombre de blocs de chaque couleur
    """
    liste_couleur=list(couleur.split())

    moyenne= len(liste_legos) / len(liste_couleur)

    return moyenne