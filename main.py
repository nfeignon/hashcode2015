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

class Pathing:
    def __init__(self):
        self.graph = None

        self.came_from = {}
        self.start = None
        self.bfs_count = 0

    def bfs(self, start):
        self.bfs_count += 1

        self.came_from = {}
        self.start = start
        queue = collections.deque()
        queue.append(start)
        self.came_from[start] = None

        while len(queue):
            current = queue.popleft()
            for next in self.graph.neighbors(current):
                if next not in self.came_from:
                    queue.append(next)
                    self.came_from[next] = current

    def get_path(self, target):
        current = target
        path = [current]
        while current != self.start:
            try:
               current = self.came_from[current]
               path.append(current)
            except KeyError:
                return None

        return path[::-1]

    def get_distance(self, target):
        path = self.get_path(target)
        if path:
            return len(self.get_path(target)) - 1
        else:
            return float("inf")

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
        if self.altitude < ALTITUDES:
            self.altitude += 1
            self.direction = 1
            self.maj_position()

    def move_down(self):
        if self.altitude > 1:
            self.altitude -= 1
            self.direction = -1
            self.maj_position()

    def couvre(self, r, c):
        if self.actif == False:
            return False

        isCouvert = ((self.r - r)**2 + (min(abs(self.c-c), COLUMNS-abs(self.c-c)))**2) <= RAYON**2
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
                if ballon.actif and ballon.altitude != 0 and ballon.couvre(c[0], c[1]):
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

        b.direction = 0
        b.move_up()
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


>>>>>>> f50326deabaf3c7a837ea504f366e2af741ccbc5

score = calcul_score()
write_file(score)

