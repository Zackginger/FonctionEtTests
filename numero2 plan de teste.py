from numero2 import liste_lego_couleur

def test1():
    listecouleur=["bleu","vert","vert","rouge"]
    couleur="bleu"
    resulatattendu=25

    resultaobtenu=liste_lego_couleur(listecouleur,couleur)

    assert resulatattendu == resultaobtenu


def test2():
    listecouleur = ["vert", "vert", "vert", "rouge","vert","vert","vert","vert","vert","vert"]
    couleur = "vert"
    resulatattendu = 90

    resultaobtenu = liste_lego_couleur(listecouleur, couleur)

    assert resulatattendu == resultaobtenu


def test3():
    listecouleur = ["bleu", "vert", "vert", "rouge","rouge"]
    couleur = "rouge"
    resulatattendu = 40

    resultaobtenu = liste_lego_couleur(listecouleur, couleur)

    assert resulatattendu == resultaobtenu