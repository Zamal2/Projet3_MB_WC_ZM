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


ARGUMENTS = analyser_commande()

# Affiche la liste des dernières parties ou prends l'input
# if ARGUMENTS.lister:
#     print(api.lister_parties(ARGUMENTS.idul))
# else:
#     IDPARTIE = api.débuter_partie(ARGUMENTS.idul)[0]
#     PARTIE = api.débuter_partie(ARGUMENTS.idul)[1]
#     EXP = True
#     while EXP:
#         try:
#             afficher_damier_ascii(PARTIE)
#             print("Déplacer le pion(D), placer un mur horizontal(MH), placer un mur vertical(MV)")
#             TYPECOUP = input()
#             print("À quelle position horizontale?")
#             POSH = input()
#             print("À quelle position verticale?")
#             POSV = input()
#             PARTIE = api.jouer_coup(IDPARTIE, TYPECOUP, (POSH, POSV))
#         except StopIteration as err:
#             print(f"La partie est terminée, {err} est vainqueur!")
#             break


if ARGUMENTS.automatique and not ARGUMENTS.graphique:
    PARTIE = api.débuter_partie(ARGUMENTS.idul)
    IDPARTIE = PARTIE[0]
    ÉTAT = PARTIE[1]
    EXP = True
    while EXP:
        try:
            JEU = qr.Quoridor(PARTIE[1])
            print(JEU)
            JEU.jouer_coup("1")
            print(JEU)
            api.jouer_coup()

#            PARTIE = api.jouer_coup(IDPARTIE, TYPECOUP, (POSH, POSV))
#        except StopIteration as err:
#            print(f"La partie est terminée, {err} est vainqueur!")
#            break