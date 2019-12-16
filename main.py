"""Le module main affiche le jeu et analyse la commande donnée par l'utilisateur"""
import argparse
import api
import quoridor as qr
import quoridorx as qrx


def analyser_commande():
    """Définit le parser pour analyser les commandes"""
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 3')
    parser.add_argument(
        'idul', help='IDUL du joueur.', metavar='idul'
    )
    parser.add_argument(
        '-a', '--automatique',
        action='store_true',
        help='Activer le mode automatique.'
    )
    parser.add_argument(
        '-x', '--graphique',
        action='store_true',
        help='Activer le mode graphique.'
    )
    return parser.parse_args()

def manuel(idul):
    print("Cette méthode n'a pas encore été implémentée.")

def manu_graph(idul):
    print("Cette méthode n'a pas encore été implémentée.")

def autonome(idul):
    PARTIE = api.débuter_partie(ARGUMENTS.idul)
    IDPARTIE = PARTIE[0]
    JEU = qr.Quoridor([idul.lower(), "automate"])
    JEU.état = PARTIE[1]
    while True:
        try:
            JEU.jouer_coup(1)
            print(JEU)
            JEU.état = api.jouer_coup(IDPARTIE, JEU.type_coup, JEU.pos_coup)
            JEU.posj2 = JEU.état['joueurs'][1]['pos']
            for i in JEU.état['murs']["horizontaux"]:
                JEU.murs['horizontaux'].append(i)
            for i in JEU.état['murs']["verticaux"]:
                JEU.murs['verticaux'].append(i)
            print(JEU)
        except StopIteration as err:
            print(f"La partie est terminée, {err} est vainqueur!")
            break

def auto_graph(idul):
        PARTIE = api.débuter_partie(ARGUMENTS.idul)
    IDPARTIE = PARTIE[0]
    JEU = qr.Quoridor([idul, "automate"])
    JEU.état = PARTIE[1]
    AFFICHAGE = qrx.QuoridorX([idul.lower(), "automate"])
    while True:
        try:
            JEU.jouer_coup(1)
            AFFICHAGE.afficher()
            JEU.état = api.jouer_coup(IDPARTIE, JEU.type_coup, JEU.pos_coup)
            JEU.posj2 = JEU.état['joueurs'][1]['pos']
            for i in JEU.état['murs']["horizontaux"]:
                JEU.murs['horizontaux'].append(i)
            for i in JEU.état['murs']["verticaux"]:
                JEU.murs['verticaux'].append(i)
            AFFICHAGE.afficher()
        except StopIteration as err:
            print(f"La partie est terminée, {err} est vainqueur!")
            break

ARGUMENTS = analyser_commande()
if ARGUMENTS.automatique and not ARGUMENTS.graphique:
    autonome(ARGUMENTS.idul.lower())
elif ARGUMENTS.automatique and ARGUMENTS.graphique:
    auto_graph(ARGUMENTS.idul.lower())
elif ARGUMENTS.graphique and not ARGUMENTS.automatique:
    manu_graph(ARGUMENTS.idul.lower())
else:
    manuel(ARGUMENTS.idul.lower())