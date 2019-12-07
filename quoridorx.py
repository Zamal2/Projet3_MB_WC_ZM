"""
Classe qui ajoute de nouvelles fonctionnalitées et qui hérite de la classe Quoridor 
"""


import quoridor as qr
import turtle as tl


class QuoridorX(qr.Quoridor):
    """
    Nouvelle Classe
    """
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs=None)


    def afficher():
        """
        méthode qui affiche le jeu
        """
        bacon = tl.Turtle()
        fen = tl.Screen()
        fen.setup(width=800, height=800)
        bacon.speed('fastest')
        bacon.pencolor('navy')
        bacon.ht()
        bacon.fillcolor('navy')
        bacon.begin_fill()
        bacon.setpos(-300, -300)
        bacon.forward(600)
        bacon.left(90)
        bacon.forward(600)
        bacon.left(90)
        bacon.forward(600)
        bacon.left(90)
        bacon.forward(600)
        bacon.end_fill()
        tl.done()
        


        for i in range(9):
            for n in range(9):
                bacon.penup()
                bacon.foward(15)
                bacon.pendown()
                bacon.foward(50)
                bacon.left(90)
                bacon.foward(50)
                bacon.left(90)
                bacon.fowward(50)
                bacon.left(90)
                bacon.foward(50)
                bacon.fillcolor('white')
                bacon.penup()
                bacon.foward(15)
                
            pass

QuoridorX.afficher()
