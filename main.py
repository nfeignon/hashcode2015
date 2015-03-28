import copy
import math
import sys
import os

class Ballon:
    def __init__(self):
        self.r = R_DEPART
        self.c = C_DEPART
        self.altitude = 0

    def __repr__(self):
        return "<Ballon %d %d>" % (self.r, self.c)

    def couvre(self, r, c):
        isCouvert = (self.r - r)**2 + (min(abs(self.c-c), COLUMNS-abs(self.c-c)))**2 <= RAYON**2
        return isCouvert


def calcul_score():
    score = 0
    print ballons

    for tour in ballons_tours:
        for c in cibles:
            for ballon in tour:
                if ballon.couvre(c[0], c[1]):
                    score += 1
                break

    print "SCORE: " + str(score)

    return score


def print_map(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            sys.stdout.write (map[i][j])
        print

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
            row.append('X')
        else:
            row.append('.')
    carte_cibles.append(row)

print_map(carte_cibles)


ballons_tours = []
for i in range(TOURS):
    ballons = []

    for j in range(BALLONS):
        ballons.append(Ballon())

    ballons_tours.append(ballons)


calcul_score()

