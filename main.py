import copy
import math
import sys
import os

class Ballon:
    def __init__(self):
        self.r = R_DEPART
        self.c = C_DEPART
        self.altitude = 0
        self.actif = True
        self.direction = 0

    def __repr__(self):
        return "<Ballon %d %d>" % (self.r, self.c)

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

                if r < 0 or r >= R:
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

def get_couverture():
    carte_couverture = copy.deepcopy(carte_cibles)

    for cible in cibles:
        for ballon in ballons:
            if ballon.couvre(cible[0], cible[1]):
                carte_couverture[cible[0]][cible[1]] = 'O'

    return carte_couverture

def write_file(score):
    f = open("output_" + str(score) + ".txt", "w")

    for i in range(TOURS):
        s = ''
        for j in range(BALLONS):
            s += '0 '

        f.write(s + '\n')

    f.close()


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
for i in range(TOURS):
    ballons = []

    for j in range(BALLONS):
        ballons.append(Ballon())

    ballons_tours.append(ballons)

############################################


print_map(get_couverture())

score = calcul_score()
write_file(score)

