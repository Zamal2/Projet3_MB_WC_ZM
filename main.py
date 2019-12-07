"""Le module main affiche le jeu et analyse la commande donnée par l'utilisateur"""
import argparse
import api


def analyser_commande():
    """Définit le parser pour analyser les commandes"""
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument(
        '-l', '--lister',
        dest='lister', action='store_true',
        help='Lister les identifiants de vos 20 dernières parties.'
    )
    parser.add_argument(
        'idul', help='IDUL du joueur.', metavar: 'idul'
    )
    return parser.parse_args()


def afficher_damier_ascii(dic):
    """Réproduit le damier tel que l'état envoyé par le serveur"""
    # Damier en dictionnaire
    damier = [list(f"Légende: 1={dic['joueurs'][0]['nom']}, 2={dic['joueurs'][1]['nom']}"),
              list("   -----------------------------------")]
    for j in range(17):
        if j % 2 == 0:
            damier.append(list("{} | .   .   .   .   .   .   .   .   . |".format(str(9 - j // 2))))
        if j % 2 != 0:
            damier.append(list("  |                                   |"))
    damier.append(list("--|-----------------------------------"))
    damier.append(list("  | 1   2   3   4   5   6   7   8   9"))
    # Placer les pions
    pos = {"1": (4*dic["joueurs"][0]["pos"][0], 20 - (2*dic["joueurs"][0]["pos"][1])),
           "2": (4*dic["joueurs"][1]["pos"][0], 20 - (2*dic["joueurs"][1]["pos"][1]))}
    for ind, val in pos.items():
        damier[val[1]][val[0]] = ind
    # Placer les murs horizontaux
    for i in dic["murs"]["horizontaux"]:
        ligne = 21 - (2*i[1])
        debut = (4*i[0])-1
        fin = debut + 7
        for j in range(debut, fin):
            damier[ligne][j] = '-'
    # Placer les murs verticaux
    for i in dic["murs"]["verticaux"]:
        colonne = (4*i[0]) - 2
        dbt = 18 - (2*i[1])
        finb = 17 - (2*i[1]) + 4
        for j in range(dbt, finb):
            damier[j][colonne] = '|'
    print('\n'.join(''.join(k for k in ligne) for ligne in damier)+'\n')


ARGUMENTS = analyser_commande()

# Affiche la liste des dernières parties ou prends l'input
if ARGUMENTS.lister:
    print(api.lister_parties(ARGUMENTS.idul))
else:
    IDPARTIE = api.débuter_partie(ARGUMENTS.idul)[0]
    PARTIE = api.débuter_partie(ARGUMENTS.idul)[1]
    EXP = True
    while EXP:
        try:
            afficher_damier_ascii(PARTIE)
            print("Déplacer le pion(D), placer un mur horizontal(MH), placer un mur vertical(MV)")
            TYPECOUP = input()
            print("À quelle position horizontale?")
            POSH = input()
            print("À quelle position verticale?")
            POSV = input()
            PARTIE = api.jouer_coup(IDPARTIE, TYPECOUP, (POSH, POSV))
        except StopIteration as err:
            print(f"La partie est terminée, {err} est vainqueur!")
            break
