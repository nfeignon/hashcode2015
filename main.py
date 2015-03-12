import math
import sys
import os

class Groupe:
    pass


class Serveur:
    def __init__(self, id, emplacements, capacite):
        self.id = id
        self.emplacements = emplacements
        self.capacite = capacite
        self.x = 0
        self.y = 0


if __name__ == '__main__':
    print 'Hash code\n\n'

    n_rangees, emplacements, n_indisponibles, n_groupes, n_serveurs = [int(i) for i in raw_input().split()]
    print str(n_groupes) + ' groupes'

    indisponibles = []
    serveurs = []
    rangees = []

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
