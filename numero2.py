
def liste_lego_couleur(liste_legos: list, couleur: str): #-> pourcentage_blocs:
    """
    Fonction qui reçoit une liste de legos et une couleur et
    qui retourne le pourcentage de blocs de cette couleur
    :param liste_legos: la liste de legos
    :param couleur: une couleur
    :return: pourcentage_blocs
    """
    pourcentage = 0
    for i in range(len(liste_legos)):
        pourcentage = liste_legos.count(couleur) * 100 // len(liste_legos)

    return pourcentage






"""
plan de test
| couleur | pourcentage | resultat attendue | resultat obtenue |
| bleu    | 25          |   25              |   25             |
| vert    | 90          |   90              |   90             |
| rouge   | 40          |   40              |   40             |
"""