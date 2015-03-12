import math
import sys
import os

class Groupe:
    pass


class Serveur:
    def __init__(self, id, id_groupe):
        self.id = id
        self.id_groupe = id_groupe
        self.x = 0
        self.y = 0

def get_capacite_garantie(groupes):
    capa_mini = int(float(inf))
    for group in groupes:

        capa = 0
        for s in group:
            capa += s.capacite

        for r in rangees:
            for i in range(r):
                if isinstance(r[i], Serveur):
                    capa -= r[i].capacite

                    i += r[i].emplacements - 1

            if capa_mini > capa:
                capa_mini = capa

    return capa_mini




if __name__ == '__main__':
    print 'Hash code\n\n'

    n_rangees, emplacements, n_indisponibles, n_groupes, n_serveurs = [int(i) for i in raw_input().split()]
    print str(n_groupes) + ' groupes'
    print str(n_serveurs) + ' serveurs'

    indisponibles = []
    serveurs = []
    rangees = []
    groupes = []

    for i in range(n_rangees):
        rangees.append(['.' for j in range(emplacements)])

    for i in range(n_indisponibles):
        indisponibles.append([int(j) for j in raw_input().split()])
        rangees[indisponibles[i][0]][indisponibles[i][1]] = 'x'

    for i in range(n_serveurs):
        serveurs.append([int(j) for j in raw_input().split()])

    print 'Entree :'
    for r in rangees:
        for c in r:
            print c + '',
        print '\n'



    print serveurs
