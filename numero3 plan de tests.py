
from numero3 import liste_blocs_legos



def test2():
    listecouleur = ["vert", "vert", "vert", "rouge","vert","vert","vert","vert","vert","vert"]
    couleur="vert rouge"
    resulatattendu = 5

    resultaobtenu = liste_blocs_legos(listecouleur, couleur)

    assert resulatattendu == resultaobtenu


def test3():
    listecouleur = ["vert", "vert", "rouge","rouge"]
    couleur="vert rouge"
    resulatattendu = 2

    resultaobtenu =liste_blocs_legos(listecouleur, couleur)

    assert resulatattendu == resultaobtenu
def test1():
    listecouleur=["bleu","jaune","vert","rouge"]
    couleur="vert rouge jaune bleu"
    resulatattendu=1

    resultaobtenu=liste_blocs_legos(listecouleur, couleur)

    assert resulatattendu == resultaobtenu

