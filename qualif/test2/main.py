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
    groupe = 0
    rangee_tested = 0


    i = 0
    while i < len(serveurs):


        debut = emplacement_serveur_range(serveurs[i], rangees[rangee])
        rangee_tested += 1

        if debut != -1:
            serveurs[i].placer_serveur(rangee, debut, rangees, groupe)

        rangee += 1

        if rangee == len(rangees):
            rangee = 0


        serveurs[i].print_info();

        i += 1

    etat_groupe = 1

    for serveur in serveurs:

        if serveur.actif == True:
            serveur.placer_groupe(groupe)

            if groupe == n_groupes - 1 and etat_groupe == 1:
                etat_groupe = 2
                continue

            if etat_groupe == 2:
                etat_groupe = 3

            if groupe == 0 and etat_groupe == 3:
                etat_groupe = 4
                continue

            if etat_groupe == 4:
                etat_groupe = 1

            if etat_groupe == 1:
                groupe +=1
            elif etat_groupe == 3:
                groupe -=1






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

    def placer_serveur(self, rangee, position, rangees, groupe):
        self.actif = True
        self.rangee = rangee
        self.position = position
        self.groupe = groupe

        for i in range(self.emplacements):
            rangees[rangee][position + i] = self

    def placer_groupe(self, groupe):
        self.groupe = groupe

def get_capacite_garantie(groupes):
    capa_mini = sys.maxint

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
                print 'o',
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
    rangees_serv = []

    for i in range(n_rangees):
        rangees.append(['.' for j in range(emplacements)])
        rangees_serv.append([])

    for i in range(n_indisponibles):
        indisponibles.append([int(j) for j in raw_input().split()])
        rangees[indisponibles[i][0]][indisponibles[i][1]] = 'x'

    for i in range(n_serveurs):
        serveurs.append([int(j) for j in raw_input().split()])
        serveurs_object.append(Serveur(i, serveurs[i][0], serveurs[i][1]))

    for i in range(n_groupes):
        groupes.append([])

    # groupes.append([serveurs_object[0], serveurs_object[1]])
    # groupes.append([serveurs_object[3], serveurs_object[4]])
    # groupes.append([serveurs_object[6], serveurs_object[7], serveurs_object[8]])
    # groupes.append([serveurs_object[9], serveurs_object[10], serveurs_object[11]])
    # groupes.append([serveurs_object[12], serveurs_object[13], serveurs_object[14]])

    # rangees[0][0] = serveurs_object[0]
    # rangees[0][5] = serveurs_object[3]
    # rangees[1][0] = serveurs_object[0]


    attribuer_emplacement(serveurs_object, rangees)

    for s in serveurs_object:
        if s.groupe != None:
            print s.groupe
            groupes[s.groupe].append(s)
        if s.rangee != None:
            rangees_serv[s.rangee].append(s)



    max_result = 0
    # for s in groupes[0]:
    #     for s2 in groupes[len(groupes)-1]:
    #         i = groupes[0].index(s)
    #         i2 = groupes[len(groupes)-1].index(s2)

    #         groupes[len(groupes)-1].append(groupes[0][i])
    #         groupes[0].append(groupes[len(groupes)-1][i2])

    #         del groupes[0][i]
    #         del groupes[len(groupes)-1][i2]

    #         result = get_capacite_garantie(groupes)

    best_result = get_capacite_garantie(groupes)
    for i in range(40):
        groupes[i].append(groupes[i+1][0])
        groupes[i+1].append(groupes[i][0])
        groupes[i+1][0].groupe = i
        groupes[i][0].groupe = i+1

        del groupes[i][0]
        del groupes[i+1][0]

        result = get_capacite_garantie(groupes)

        if result > best_result:
            best_result = result
            continue

        tmp = groupes[i].pop()
        tmp2 = groupes[i+1].pop()
        tmp.groupe = i + 1
        tmp2.groupe = i

        groupes[i].append(tmp2)
        groupes[i+1].append(tmp)

    for g in groupes:
        capa = 0
        for s in g:
            capa += s.capacite
        print capa

    print 'result = ' + str(get_capacite_garantie(groupes))
    #print get_capacite_garantie2(groupes, rangees_serv)

    print_grille(rangees)
    get_output_file(serveurs_object)

    #print serveurs
