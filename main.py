import copy
import math
import sys
import os
from time import sleep
import random

def construire_graph():

    graph = []
    queue = []

    depart = Noeud(R_DEPART, C_DEPART, 0)
    graph.append(depart)
    queue.append(depart)


    while queue:
        current = queue.pop()

        if current.altitude < 8:
            vecteur = altitudes[current.altitude][current.row][current.column]

            r = current.row + vecteur[0]
            c = (current.column + vecteur[1])%COLUMNS

            if r >= 0 and r < ROWS:
                monter = Noeud(r, c, current.altitude + 1)
                if monter not in current.voisins:
                    current.voisins.append(monter)
                if monter not in graph:
                    graph.append(monter)
                    queue.append(monter)

        if current.altitude > 1:
            vecteur = altitudes[current.altitude - 2][current.row][current.column]

            r = current.row + vecteur[0]
            c = (current.column + vecteur[1])%COLUMNS

            if r >= 0 and r < ROWS:
                descendre = Noeud(r, c, current.altitude - 1)
                if descendre not in current.voisins:
                    current.voisins.append(descendre)
                if descendre not in graph:
                    graph.append(descendre)
                    queue.append(descendre)



        #print len(graph)
        # print current.voisins




class Noeud:
    def __init__(self, row, column, altitude):
        self.row = row
        self.column = column
        self.altitude = altitude
        self.name = str(row) + "-" + str(column) + "-" + str(altitude)
        self.voisins = []

    def __repr__(self):
        return self.name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return (self.row, self.column, self.altitude) == (other.row, other.column, other.altitude)

class Ballon:
    def __init__(self):
        self.r = R_DEPART
        self.c = C_DEPART
        self.altitude = 0
        self.actif = True
        self.direction = 0

    def __repr__(self):
        return "<Ballon %d %d %d>" % (self.r, self.c, self.altitude)

    def move_up(self):
        self.altitude += 1
        self.direction = 1

    def move_down(self):
        self.altitude -= 1
        self.direction = -1

    def couvre(self, r, c):
        if self.actif == False:
            return False

        isCouvert = (self.r - r)**2 + (min(abs(self.c-c), COLUMNS-abs(self.c-c)))**2 <= RAYON**2
        return isCouvert

    def maj_position(self):
        if self.actif == True:
            if self.altitude > 0 and self.altitude <= ALTITUDES:
                vecteur = altitudes[self.altitude-1][self.r][self.c]

                r = self.r + vecteur[0]
                c = (self.c + vecteur[1])%COLUMNS

                if r < 0 and r >= ROWS:
                    self.actif = False
                else:
                    self.r = r
                    self.c = c

def calcul_score():
    score = 0

    for tour in ballons_tours:
        for c in cibles:
            for ballon in tour:
                if ballon.altitude != 0 and ballon.couvre(c[0], c[1]):
                    score += 1
                break

    print "SCORE: " + str(score)

    return score


def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            sys.stdout.write (map[i][j])
        print

def get_couverture(ballons):
    carte_couverture = copy.deepcopy(carte_cibles)

    for cible in cibles:
        for ballon in ballons:

            if ballon.couvre(cible[0], cible[1]):
                carte_couverture[cible[0]][cible[1]] = 'o'

            if ballon.actif == True:
                carte_couverture[ballon.r][ballon.c] = 'X'
            else:
                carte_couverture[ballon.r][ballon.c] = 'W'

    return carte_couverture

def write_file(score):
    f = open("output_" + str(score) + ".txt", "w")

    for tour in ballons_tours:
        s = ''

        for ballon in tour:
            s += '%d ' % ballon.direction

        f.write(s + '\n')

    f.close()


########################
########################
########################

print "Hash code final round"

ROWS,COLUMNS,ALTITUDES = [int(i) for i in raw_input().split()]
CIBLES,RAYON,BALLONS,TOURS = [int(i) for i in raw_input().split()]
R_DEPART, C_DEPART = [int(i) for i in raw_input().split()]

print "ROWS:%s, COLUMNS:%s, ALTITUDES:%s" % (ROWS, COLUMNS, ALTITUDES)
print "CIBLES:%s, RAYON:%s, BALLONS:%s, TOURS:%s" % (CIBLES, RAYON, BALLONS, TOURS)
print "ROW DEPART:%s, COLUMN DEPART:%s" % (R_DEPART, C_DEPART)

cibles = []
cibles_dict = {}

for i in range(ROWS):
    for j in range(COLUMNS):
        cibles_dict[(i, j)] = False

for i in range(CIBLES):
    cibles.append([int(j) for j in raw_input().split()])
    cibles_dict[(cibles[i][0], cibles[i][1])] = True

altitudes = []

for i in range(ALTITUDES):
    altitude = []
    for j in range(ROWS):
        data = [int(x) for x in raw_input().split()]
        altitude.append(zip(data[0::2], data[1::2]))
    altitudes.append(altitude)

carte_cibles = []

for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        if cibles_dict[(i, j)] == True:
            row.append('.')
        else:
            row.append(' ')
    carte_cibles.append(row)

ballons_tours = []

#construire_graph()

ballons = []
for j in range(BALLONS):
    b = Ballon()
    ballons.append(b)
ballons_tours.append(ballons)

############################################

for i in range(1, TOURS):
    ballons = []

    for j in range(BALLONS):
        b = copy.deepcopy(ballons_tours[i-1][j])

        b.move_up()
        b.maj_position()
        ballons.append(b)

    ballons_tours.append(ballons)

############################################
############################################
############################################

for i in range(TOURS):
    couverture = get_couverture(ballons_tours[i])
    os.system('clear')
    print_map(couverture)
    print "ROUND %s" % (i,)


score = calcul_score()
write_file(score)

