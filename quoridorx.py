"""
Classe qui ajoute de nouvelles fonctionnalitées et qui hérite de la classe Quoridor 
"""


import quoridor as qr
import turtle as tl


class QuoridorX(Quoridor):
    """
    Nouvelle Classe
    """
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs=None)

    def afficher():
        fenetre = tl.Screen('black')
        fenetre.setup(width=600, height=600)
        curseur = tl.Turtle()
        tl.speed("fastest")
        
        for i in range(9):
            for n in range(9):
                curseur