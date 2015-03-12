import math
import sys
import os

class Groupe:
    pass

def attribuer_emplacement(serveurs, rangees):

    serveurs.sort(key = lambda x: x.capacite)

    for i in range(len(serveurs)):
        serveurs[i].print_info();

class Serveur:
    def __init__(self, id, emplacements, capacite):
        self.id = id
        self.emplacements = emplacements
        self.capacite = capacite
        self.x = 0
        self.y = 0

    def print_info(self):
        print "id:%d, emplacements:%d, capacite:%d" % (self.id, self.emplacements, self.capacite)

if __name__ == '__main__':
    print 'Hash code\n\n'

    n_rangees, emplacements, n_indisponibles, n_groupes, n_serveurs = [int(i) for i in raw_input().split()]
    print str(n_groupes) + ' groupes'

    indisponibles = []
    serveurs = []
    rangees = []
    serveurs_object = []

    for i in range(n_rangees):
        rangees.append(['.' for j in range(emplacements)])

    for i in range(n_indisponibles):
        indisponibles.append([int(j) for j in raw_input().split()])
        rangees[indisponibles[i][0]][indisponibles[i][1]] = 'x'

    for i in range(n_serveurs):
        serveurs.append([int(j) for j in raw_input().split()])
        serveurs_object.append(Serveur(i, serveurs[i][0], serveurs[i][1]))

    print 'Entree :'
    for r in rangees:
        for c in r:
            print c + '',
        print '\n'

    attribuer_emplacement(serveurs_object, rangees)

    #print serveurs
