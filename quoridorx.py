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
        """
        méthode qui affiche le jeu
        """
        fen = tl.Screen()
        fen.setup(width=800, height=800)
        bacon.speed('fastest')
        bacon.pencolor('blue')
        bacon = tl.Turtle()
        bacon.ht()
        bacon.fillcolor('blue')
        bacon.penup()
        bacon.right(180)
        bacon.forward(300)
        bacon.left(90)
        bacon.forward(300)
        bacon.left(90)
        bacon.pendown()
        bacon.begin_fill()
        bacon.forward(600)
        bacon.left(90)
        bacon.forward(600)
        bacon.left(90)
        bacon.forward(600)
        bacon.end_fill()
        tl.done()
        


        for i in range(9):
            for n in range(9):
                 
            pass
