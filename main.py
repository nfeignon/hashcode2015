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

    for c in cibles:
        for b in ballons:
            if b.couvre(c[0], c[1]):
                score += 1

    print "SCORE: " + str(score)

    return score


print "Hash code final round"

ROWS,COLUMNS,ALTITUDES = [int(i) for i in raw_input().split()]
CIBLES,RAYON,BALLONS,TOURS = [int(i) for i in raw_input().split()]
R_DEPART, C_DEPART = [int(i) for i in raw_input().split()]

print "ROWS:%s, COLUMNS:%s, ALTITUDES:%s" % (ROWS, COLUMNS, ALTITUDES)
print "CIBLES:%s, RAYON:%s, BALLONS:%s, TOURS:%s" % (CIBLES, RAYON, BALLONS, TOURS)
print "ROW DEPART:%s, COLUMN DEPART:%s" % (R_DEPART, C_DEPART)

cibles = []

for i in range(CIBLES):
    cibles.append([int(i) for i in raw_input().split()])

altitudes = []

for i in range(ALTITUDES):
    altitude = []
    for j in range(ROWS):
        data = [int(i) for i in raw_input().split()]
        altitude.append(zip(data[0::2], data[1::2]))
    altitudes.append(altitude)

print altitudes[0][0]


ballons = []
for i in range(BALLONS):
    ballons.append(Ballon())

print ballons

calcul_score()

