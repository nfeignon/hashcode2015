import math
import sys
import os

class Groupe:
    pass


def emplacement_serveur_range(serveur, rangee):

    taille = serveur.emplacements

    debut = -1
    count = 0


    for i in range(len(rangee)):
        if rangee[i] == '.':
            count += 1
            if debut == -1:
                debut = i

            if count == taille:
                return debut
        else:
            count = 0
            debut = -1

        #print "i %d debut %d count %d" %(i, debut, count)

    return -1


def get_output_file(serveurs):

    serveurs.sort(key = lambda x: x.id)

    f = open('output.txt','w')

    for serveur in serveurs:
        if serveur.actif == False:
            f.write('x')
        else:
            f.write("{0} {1} {2}".format(serveur.rangee, serveur.position, serveur.groupe))
        f.write('\n')

    f.close()

def attribuer_emplacement(serveurs, rangees):

    serveurs.sort(key = lambda x: x.capacite, reverse=True)
    rangee = 0

    for i in range(len(serveurs)):
        debut = emplacement_serveur_range(serveurs[i], rangees[rangee])

        if debut != -1:
            serveurs[i].placer_serveur(rangee, debut, rangees)

        rangee += 1

        if rangee == len(rangees):
            rangee = 0


        #print emplacement_serveur_range(serveurs[i], rangees[0])
        serveurs[i].print_info();

    for r in rangees:
        for c in r:
            print c + '',
        print '\n'

class Serveur:
    def __init__(self, id, emplacements, capacite):
        self.id = id
        self.emplacements = emplacements
        self.capacite = capacite
        self.x = 0
        self.position = None
        self.actif = False
        self.rangee = None
        self.groupe = None

    def print_info(self):
        print "id:{0}, emplacements:{1}, capacite:{2}, rangee:{3}, position:{4}, groupe:{5}".format(self.id, self.emplacements, self.capacite, self.rangee, self.position, self.groupe)

    def placer_serveur(self, rangee, position, rangees):
        self.actif = True
        self.rangee = rangee
        self.position = position

        for i in range(self.emplacements):
            rangees[rangee][position + i] = 'o'

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
    get_output_file(serveurs_object)

    #print serveurs
