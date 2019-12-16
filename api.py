"""Le module api permet la communication avec le serveur de jeu"""
import requests


URL = 'https://python.gel.ulaval.ca/quoridor/api/'

def lister_parties(idul):
    """demande au serveur la liste des derniers jeux de l'utilisateur"""
    rep = requests.get(URL+'lister/', params={'idul': idul})
    rep = rep.json()
    if "message" in rep:
        raise RuntimeError(rep["message"])
    return rep["parties"]

def débuter_partie(idul):
    """Débute une nouvelle partie dans le serveur de jeu"""
    rep = requests.post(URL+'débuter/', data={'idul': idul})
    rep = rep.json()
    if  "message" in rep:
        raise RuntimeError(rep["message"])
    return (rep['id'], rep['état'])


def jouer_coup(id_partie, type_coup, position):
    """Appelle la requête jouer coup du serveur de jeu"""
    rep = requests.post(URL+'jouer/', data={'id': id_partie, 'type': type_coup, 'pos': position})
    rep = rep.json()
    if "message" in rep:
        raise RuntimeError(rep["message"])
    elif "gagnant" in rep:
        raise StopIteration(rep["gagnant"])
    return rep["état"]
    