"""
Classe qui encapsule le jeu Quoridor
"""


import networkx as nx


class Quoridor:
    """
    Classe Quoridor
    """
    def __init__(self, joueurs, murs=None):
        """
        Fonction qui initialise la classe
        Arguments:
            joueurs {itérable} -- indique les noms des joueurs.
        Keyword Arguments:
            murs {dict} -- indique l'orientation et le placement des murs
            à l'état initial de la partie. (default: {None})
        """
        if len(joueurs) != 2:
            raise QuoridorError("le nombre de joueurs est invalide")
        # Code à executer si les objets de l'itérable sont des strings
        if isinstance(joueurs[0], str) and isinstance(joueurs[1], str):
            self.joueur1 = joueurs[0]
            self.joueur2 = joueurs[1]
            self.mursj1 = self.mursj2 = 10
            self.posj1 = (5, 1)
            self.posj2 = (5, 9)
            self.murs = murs
        # Code à executer si les objets de l'itérable sont des dictionnaires
        elif isinstance(joueurs[0], dict) and isinstance(joueurs[1], dict):
            self.joueur1 = joueurs[0]['nom']
            self.joueur2 = joueurs[1]['nom']
            self.mursj1 = joueurs[0]['murs']
            self.mursj2 = joueurs[1]['murs']
            self.posj1 = joueurs[0]['pos']
            self.posj2 = joueurs[1]['pos']
            self.murs = murs
        if isinstance(murs, dict):
            for i in murs["horizontaux"]:
                if i[0] < 1 or i[0] > 8 or i[1] < 2 or i[1] > 9:
                    raise QuoridorError("La position d'un mur est invalide.")
            for j in murs["verticaux"]:
                if j[0] < 2 or j[0] > 9 or j[1] < 1 or j[1] > 8:
                    raise QuoridorError("La position d'un mur est invalide.")
            if len(murs["horizontaux"])+len(murs["verticaux"])+\
                self.mursj1 + self.mursj2 != 20:
                raise QuoridorError("Le nombre de murs est différent de 20")
        elif murs is None:
            self.murs = {"horizontaux": [], "verticaux": []}
        else:
            raise QuoridorError("L'argument 'murs' n'est pas un dictionnaire.")
        if 0 >= self.posj1[0] > 9 or 0 >= self.posj1[1] > 9\
            or 0 >= self.posj2[0] > 9 or 0 >= self.posj2[1] > 9\
            or self.posj1 == self.posj2:
            raise QuoridorError("La position d'un joueur est invalide")
        if self.mursj1 > 10 or self.mursj2 > 10:
            raise QuoridorError('le nombre de murs placé par un joueur est suppérieur a 10')
        self.état_partie()


    def __str__(self):
        """
        Réproduit le damier correspondant à l'état actuel de la partie
        """
        # Damier en dictionnaire
        damier = [list(f"Légende: 1={self.joueur1}, 2={self.joueur2}"),
                  list("   -----------------------------------")]
        for j in range(17):
            if j % 2 == 0:
                damier.append(list(f"{str(9 - j // 2)} | .   .   .   .   .   .   .   .   . |"))
            if j % 2 != 0:
                damier.append(list("  |                                   |"))
        damier.append(list("--|-----------------------------------"))
        damier.append(list("  | 1   2   3   4   5   6   7   8   9"))
        # Placer les pions
        pos = {"1": (4*self.posj1[0], 20 - (2*self.posj1[1])),
               "2": (4*self.posj2[0], 20 - (2*self.posj2[1]))}
        for ind, val in pos.items():
            damier[val[1]][val[0]] = ind
        # Placer les murs horizontaux
        for i in self.murs["horizontaux"]:
            ligne = 21 - (2*i[1])
            debut = (4*i[0])-1
            fin = debut + 7
            for j in range(debut, fin):
                damier[ligne][j] = '-'
        # Placer les murs verticaux
        for i in self.murs["verticaux"]:
            colonne = (4*i[0]) - 2
            dbt = 18 - (2*i[1])
            finb = 17 - (2*i[1]) + 4
            for j in range(dbt, finb):
                damier[j][colonne] = '|'
        return '\n'.join(''.join(k for k in ligne) for ligne in damier)+'\n'


    def déplacer_jeton(self, joueur, position):
        """
        Déplace le jeton correspondant au joueur spécifié
        """
        if position[0] > 9 or position[0] < 1 or position[1] > 9 or position[1] < 1:
            raise QuoridorError("la position est invalide (en dehors du damier).")
        graphe = construire_graphe(
            [joueur['pos'] for joueur in self.état['joueurs']],
            self.état['murs']['horizontaux'],
            self.état['murs']['verticaux']
        )
        if joueur == 1:
            move_possible = list(graphe.successors(self.posj1))
            pos_actuelle1 = self.posj1
            for element in move_possible:
                if element == position:
                    self.posj1 = position
            if pos_actuelle1 == self.posj1:
                raise QuoridorError("La position est invalide pour l'état actuelle du jeu")
        elif joueur == 2:
            move_possible = list(graphe.successors(self.posj2))
            pos_actuelle2 = self.posj2
            for element in move_possible:
                if element == position:
                    self.posj2 = position
            if pos_actuelle2 == self.posj2:
                raise QuoridorError("La position est invalide pour l'état actuelle du jeu")
        else:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2")



    def état_partie(self):
        """
        Produit l'état actuel de la partie
        """
        self.état = {'joueurs': [
            {'nom': self.joueur1, 'murs': self.mursj1, 'pos': self.posj1},
            {'nom': self.joueur2, 'murs': self.mursj2, 'pos': self.posj2}
            ],
                     'murs': {
                         'horizontaux': self.murs['horizontaux'],
                         'verticaux': self.murs['verticaux']}}
        return self.état



    def jouer_coup(self, joueur):
        """
        joue automatiquement le meilleur coup possible pour le joueur spécifié
        selon l'état actuel de la partie
        Arguments:
            joueur {int} -- entier spécifiant le numéro du joueur
        """
        graphe = construire_graphe(
            [joueur['pos'] for joueur in self.état['joueurs']],
            self.état['murs']['horizontaux'],
            self.état['murs']['verticaux']
        )
        if self.partie_terminée() != False:
            raise QuoridorError('la partie est terminée')
        elif joueur == 1:
            if len(nx.shortest_path(graphe, self.posj1, "B1")) \
                    <= len(nx.shortest_path(graphe, self.posj2, "B2")):
                self.déplacer_jeton(1, list(nx.shortest_path(graphe, self.posj1))[1])
                print(list(nx.shortest_path(graphe, self.posj1)))
            else:
                self.placer_mur(1, (5, 3), "horizontal")
        elif joueur == 2:
            if len(nx.shortest_path(graphe, self.posj1, "B1")) \
                    >= len(nx.shortest_path(graphe, self.posj2, "B2")):
                self.déplacer_jeton(2, list(nx.shortest_path(graphe, self.posj2))[1])
                print(list(nx.shortest_path(graphe, self.posj2)))
            else:
                self.placer_mur(2, (5, 7), "horizontal")
        else:
            raise QuoridorError('le numero de joueur est invalide')


    def partie_terminée(self):
        """
        Détermine si la partie est terminée
        """
        if self.posj1[1] == 9:
            return self.joueur1
        elif self.posj2[1] == 1:
            return self.joueur2
        else:
            return False


    def placer_mur(self, joueur, position, orientation):
        """
        Place un mur à la position specifiée pour le joueur spécifié
        Arguments:
            joueur {int} -- identifie le joueur
            position {tuple} -- tuple (x, y) qui donne emplacement du mur à placer
            orientation {str} -- chaîne de caractères qu'indique
            l'orientation du mur ('horizontal' ou 'vertical')
        """
        if orientation == "horizontal":
            # Tester si la position est valide
            if position[0] < 1 or position[0] > 8 or position[1] < 2 or position[1] > 9:
                raise QuoridorError("La position est invalide pour cette orientation.")
            état_temp = self.état
            état_temp["murs"]["horizontaux"].append(position)
            graphe_temp = construire_graphe(
                [joueur['pos'] for joueur in état_temp['joueurs']],
                état_temp['murs']['horizontaux'],
                état_temp['murs']['verticaux']
            )
            if not nx.has_path(graphe_temp, self.posj1, 'B1'):
                raise QuoridorError("La position est invalide pour cette orientation.")
            if not nx.has_path(graphe_temp, self.posj2, 'B2'):
                raise QuoridorError("La position est invalide pour cette orientation.")
            # Tester si un mur occupe la position
            for i in self.murs['horizontaux']:
                if (position[0] == i[0]-1 or position[0] == i[0] or position[0] == i[0]+1) \
                    and position[1] == i[1]:
                    raise QuoridorError("Un mur occupe déjà cette position")
            for i in self.murs['verticaux']:
                if i[0] == position[0]+1 and i[1] == position[1]-1:
                    raise QuoridorError("Un mur occupe déjà cette position")
        else:
            # Tester si la position est valide
            if position[0] < 2 or position[0] > 9 or position[1] < 1 or position[1] > 8:
                raise QuoridorError("La position est invalide pour cette orientation.")
            état_temp = self.état
            état_temp["murs"]["verticaux"].append(position)
            graphe = construire_graphe(
                [joueur['pos'] for joueur in self.état['joueurs']],
                self.état['murs']['horizontaux'],
                self.état['murs']['verticaux'])
            if not nx.has_path(graphe_temp, self.posj1, 'B1'):
                raise QuoridorError("La position est invalide pour cette orientation.")
            if not nx.has_path(graphe_temp, self.posj2, 'B2'):
                raise QuoridorError("La position est invalide pour cette orientation.")
            # Tester si un mur occupe la position
            for i in self.murs['horizontaux']:
                if i[0] == position[0]-1 and i[1] == position[1]+1:
                    raise QuoridorError("Un mur occupe déjà cette position")
            for i in self.murs['verticaux']:
                if (position[1] == i[1]-1 or position[1] == i[1] or position[1] == i[1]+1) \
                    and position[0] == i[0]:
                    raise QuoridorError("Un mur occupe déjà cette position")
        if joueur == 1:
            if self.mursj1 == 0:
                raise QuoridorError("Le joueur a déjà placé tous ses murs.")
            if orientation == "horizontal":
                self.murs['horizontaux'].append(position)
            else:
                self.murs['verticaux'].append(position)
            self.mursj1 -= 1
        elif joueur == 2:
            if self.mursj2 == 0:
                raise QuoridorError("Le joueur a déjà placé tous ses murs.")
            if orientation == "horizontal":
                self.murs['horizontaux'].append(position)
            else:
                self.murs['verticaux'].append(position)
            self.mursj2 -= 1
        else:
            raise QuoridorError("Le numéro du joueur est autre que 1 ou 2")



def construire_graphe(joueurs, murs_horizontaux, murs_verticaux):
    """
    Crée le graphe des déplacements admissibles pour les joueurs.

    :param joueurs: une liste des positions (x,y) des joueurs.
    :param murs_horizontaux: une liste des positions (x,y) des murs horizontaux.
    :param murs_verticaux: une liste des positions (x,y) des murs verticaux.
    :returns: le graphe bidirectionnel (en networkX) des déplacements admissibles.
    """
    graphe = nx.DiGraph()

    # pour chaque colonne du damier
    for x in range(1, 10):
        # pour chaque ligne du damier
        for y in range(1, 10):
            # ajouter les arcs de tous les déplacements possibles pour cette tuile
            if x > 1:
                graphe.add_edge((x, y), (x-1, y))
            if x < 9:
                graphe.add_edge((x, y), (x+1, y))
            if y > 1:
                graphe.add_edge((x, y), (x, y-1))
            if y < 9:
                graphe.add_edge((x, y), (x, y+1))

    # retirer tous les arcs qui croisent les murs horizontaux
    for x, y in murs_horizontaux:
        graphe.remove_edge((x, y-1), (x, y))
        graphe.remove_edge((x, y), (x, y-1))
        graphe.remove_edge((x+1, y-1), (x+1, y))
        graphe.remove_edge((x+1, y), (x+1, y-1))

    # retirer tous les arcs qui croisent les murs verticaux
    for x, y in murs_verticaux:
        graphe.remove_edge((x-1, y), (x, y))
        graphe.remove_edge((x, y), (x-1, y))
        graphe.remove_edge((x-1, y+1), (x, y+1))
        graphe.remove_edge((x, y+1), (x-1, y+1))

    # s'assurer que les positions des joueurs sont bien des tuples (et non des listes)
    j1, j2 = tuple(joueurs[0]), tuple(joueurs[1])

    # traiter le cas des joueurs adjacents
    if j2 in graphe.successors(j1) or j1 in graphe.successors(j2):
        # retirer les liens entre les joueurs
        graphe.remove_edge(j1, j2)
        graphe.remove_edge(j2, j1)

        def ajouter_lien_sauteur(noeud, voisin):
            """
            :param noeud: noeud de départ du lien.
            :param voisin: voisin par dessus lequel il faut sauter.
            """
            saut = 2*voisin[0]-noeud[0], 2*voisin[1]-noeud[1]

            if saut in graphe.successors(voisin):
                # ajouter le saut en ligne droite
                graphe.add_edge(noeud, saut)

            else:
                # ajouter les sauts en diagonale
                for saut in graphe.successors(voisin):
                    graphe.add_edge(noeud, saut)

        ajouter_lien_sauteur(j1, j2)
        ajouter_lien_sauteur(j2, j1)

    # ajouter les destinations finales des joueurs
    for x in range(1, 10):
        graphe.add_edge((x, 9), 'B1')
        graphe.add_edge((x, 1), 'B2')

    return graphe


class QuoridorError(Exception):
    """
    Classe d'utilisation d'erreur
    """

