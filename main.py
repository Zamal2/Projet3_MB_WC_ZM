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
    """
    Fonction qui permet de jouer en mode manuel.
    """
    partie = api.débuter_partie(ARGUMENTS.idul.lower())
    jeu = qr.Quoridor([idul.lower(), "automate"])
    jeu.état = partie[1]
    print(jeu)
    print("La méthode de jeu manuelle n'a pas encore été implémentée.")

def manu_graph(idul):
    """
    Fonction qui permet de jouer en mode manuel avec une affichage graphique.
    """
    partie = api.débuter_partie(ARGUMENTS.idul.lower())
    jeu = qr.Quoridor([idul.lower(), "automate"])
    jeu.état = partie[1]
    print(jeu)
    print("La méthode de jeu manuelle avec affichage graphique n'a pas encore été implémentée.")

def autonome(idul):
    """
    Fonction qui permet de jouer en mode automatique contre le serveur.
    """
    partie = api.débuter_partie(ARGUMENTS.idul.lower())
    idp = partie[0]
    jeu = qr.Quoridor([idul.lower(), "automate"])
    jeu.état = partie[1]
    print(jeu)
    while True:
        try:
            jeu.jouer_coup(1)
            print(jeu)
            jeu.état = api.jouer_coup(idp, jeu.type_coup, jeu.pos_coup)
            jeu.posj2 = (jeu.état['joueurs'][1]['pos'][0], jeu.état['joueurs'][1]['pos'][1])
            for i in jeu.état['murs']["horizontaux"]:
                jeu.murs['horizontaux'].append(i)
            for i in jeu.état['murs']["verticaux"]:
                jeu.murs['verticaux'].append(i)
            print(jeu)
        except StopIteration as err:
            print(f"La partie est terminée, {err} est vainqueur!")
            break

def auto_graph(idul):
    """
    Fonction qui permet de jouer en mode automatique contre le serveur avec une affichage graphique.
    """
    partie = api.débuter_partie(ARGUMENTS.idul.lower())
    idp = partie[0]
    jeu = qrx.QuoridorX([idul, "automate"])
    jeu.état = partie[1]
    jeu.afficher()

    while True:
        try:
            jeu.jouer_coup(1)
            jeu.afficher()
            jeu.état = api.jouer_coup(idp, jeu.type_coup, jeu.pos_coup)
            jeu.posj2 = (jeu.état['joueurs'][1]['pos'][0], jeu.état['joueurs'][1]['pos'][1])
            jeu.posj2 = (jeu.état['joueurs'][1]['pos'][0], jeu.état['joueurs'][1]['pos'][1])
            for i in jeu.état['murs']["horizontaux"]:
                jeu.murs['horizontaux'].append(i)
                jeu.murs['horizontaux'].append(i)
            for i in jeu.état['murs']["verticaux"]:
                jeu.murs['verticaux'].append(i)
                jeu.murs['verticaux'].append(i)
            jeu.afficher()
        except StopIteration as err:
            print(f"La partie est terminée, {err} est vainqueur!")
            break

ARGUMENTS = analyser_commande()
if ARGUMENTS.automatique and not ARGUMENTS.graphique:
    autonome(ARGUMENTS.idul)
elif ARGUMENTS.automatique and ARGUMENTS.graphique:
    auto_graph(ARGUMENTS.idul)
elif ARGUMENTS.graphique and not ARGUMENTS.automatique:
    manu_graph(ARGUMENTS.idul)
else:
    manuel(ARGUMENTS.idul)
