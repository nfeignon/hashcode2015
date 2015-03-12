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

def get_capacite_garantie(groupes):
    capa_mini = 100000000000000

    for group in groupes:
        for i in range(len(rangees)):
            capa = 0
            for s in group:
                capa += s.capacite
                j = 0

            while j < len(rangees[i]):
                s = rangees[i][j]
                if not s == '.' and not s == 'x' and s in group:           # it's a server
                    capa -= rangees[i][j].capacite
                    j += rangees[i][j].emplacements

                j += 1

            if capa_mini > capa:
                capa_mini = capa

    return capa_mini

def print_grille(rangees):
    for i in range(len(rangees)):
        for j in range(len(rangees[i])):
            c = rangees[i][j]
            if not c == '.' and not c == 'x':           # it's a server
                print str(c.id) + '',
            else:
                print c + '',
        print '\n'


if __name__ == '__main__':
    print 'Hash code\n\n'

    n_rangees, emplacements, n_indisponibles, n_groupes, n_serveurs = [int(i) for i in raw_input().split()]
    print str(n_groupes) + ' groupes'
    print str(n_serveurs) + ' serveurs'

    indisponibles = []
    serveurs = []
    rangees = []
    groupes = []
    serveurs_object = []

    for i in range(n_rangees):
        rangees.append(['.' for j in range(emplacements)])

    for i in range(n_indisponibles):
        indisponibles.append([int(j) for j in raw_input().split()])
        rangees[indisponibles[i][0]][indisponibles[i][1]] = 'x'

    for i in range(n_serveurs):
        serveurs.append([int(j) for j in raw_input().split()])
        serveurs_object.append(Serveur(i, serveurs[i][0], serveurs[i][1]))

    groupes.append([serveurs_object[0], serveurs_object[1]])
    groupes.append([serveurs_object[3], serveurs_object[4]])
    # groupes.append([serveurs_object[6], serveurs_object[7], serveurs_object[8]])
    # groupes.append([serveurs_object[9], serveurs_object[10], serveurs_object[11]])
    # groupes.append([serveurs_object[12], serveurs_object[13], serveurs_object[14]])

    rangees[0][0] = serveurs_object[0]
    rangees[0][5] = serveurs_object[3]
    # rangees[1][0] = serveurs_object[0]

    serveurs_object[0].print_info()
    serveurs_object[3].print_info()

    print 'Entree :'
    print_grille(rangees)

    # attribuer_emplacement(serveurs_object, rangees)
    print get_capacite_garantie(groupes)

    #print serveurs
