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
        fond = tl.Turtle()
        fen = tl.Screen()
        fen.setup(width=800, height=800)
        fond.pencolor('lime')
        fen.delay(0)
        fond.ht()
        fond.fillcolor('lime')
        fond.setpos(-325, -325)
        fond.begin_fill()
        fond.forward(650)
        fond.left(90), fond.forward(650)
        fond.left(90), fond.forward(650)
        fond.end_fill()
        car = tl.Turtle()
        car.pencolor('red')
        car.ht()
        car.fillcolor('yellow')
        for x in range(9):
            for i in range(9):
                car.penup()
                car.setpos(-325+((i*60)+(i+1)*11), -325+((x*60)+(x+1)*11))
                car.pendown()
                car.begin_fill()
                car.forward(60)
                car.left(90)
                car.forward(60)
                car.left(90)
                car.forward(60)
                car.left(90)
                car.forward(60)
                car.left(90)
                car.end_fill()

QuoridorX.afficher()
