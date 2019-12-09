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

    def afficher(self):
        """
        méthode qui affiche le jeu
        """
        posj1 = self.posj1
        posj2 = self.posj2
        fond = tl.Turtle()
        fen = tl.Screen()
        fen.setup(width=800, height=800)
        fond.pencolor('lime')
        fen.delay(0)
        fond.ht()
        fond.fillcolor('lime')
        fond.penup()
        fond.setpos(-325, -325)
        fond.pendown()
        fond.begin_fill()
        fond.forward(650)
        fond.left(90)
        fond.forward(650)
        fond.left(90)
        fond.forward(650)
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
                car.left(90), car.forward(60)
                car.left(90), car.forward(60)
                car.left(90), car.forward(60)
                car.left(90)
                car.end_fill()
        j1 = tl.Turtle()
        j1.ht()
        j1.pencolor('red')
        j1.fillcolor('red')
        j1.penup()
        j1.setpos(-325+(((posj1[0]-1)*60)+((posj1[0]-1)+1)*11)+30, -325+(((posj1[1]-1)*60)+((posj1[1]-1)+1)*11)+5)
        j1.pendown()
        j1.begin_fill()
        j1.circle(25)
        j1.end_fill()
        j2 = tl.Turtle()
        j2.ht()
        j2.pencolor('blue')
        j2.fillcolor('blue')
        j2.penup()
        j2.setpos(-325+(((posj2[0]-1)*60)+((posj2[0]-1)+1)*11)+30, -325+(((posj2[1]-1)*60)+((posj2[1]-1)+1)*11)+5)
        j2.pendown()
        j2.begin_fill()
        j2.circle(25)
        j2.end_fill()
        mh = tl.Turtle()
        mh.ht()
        mh.pencolor('black')
        mh.fillcolor('gray')
        for h in self.état['murs']['horizontaux']:
            mh.penup()
            mh.setpos(-325+(((h[0]-1)*60)+((h[0]-1)+1)*11), -325+(((h[1]-1)*60)+((h[1]-1)+1)*11)-8)
            mh.pendown()
            mh.begin_fill()
            mh.forward(131)
            mh.left(90), mh.forward(5)
            mh.left(90), mh.forward(131)
            mh.left(90), mh.forward(5)
            mh.left(90)
            mh.end_fill()
        mv = tl.Turtle()
        mv.ht()
        mv.pencolor('black')
        mv.fillcolor('gray')
        for v in self.état['murs']['verticaux']:
            mv.penup()
            mv.setpos(-325+(((v[0]-1)*60)+((v[0]-1)+1)*11)-8, -325+(((v[1]-1)*60)+((v[1]-1)+1)*11))
            mv.pendown()
            mv.begin_fill()
            mv.forward(5)
            mv.left(90), mv.forward(131)
            mv.left(90), mv.forward(5)
            mv.left(90), mv.forward(131)
            mv.left(90)
            mv.end_fill()
        tl.done()

a = QuoridorX(('penis', 'vagin'))
a.afficher()

