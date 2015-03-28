import copy
import math
import sys
import os
from time import sleep
import random

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
        self.direction = 0
        if self.altitude < ALTITUDES:
            self.altitude += 1
            self.direction = 1

    def move_down(self):
        self.direction = 0
        if self.altitude > 1:
            self.altitude -= 1
            self.direction = -1

    def stay(self):
        self.direction = 0

    def couvre(self, r, c):
        if self.actif == False:
            return False

        isCouvert = ((self.r - r)**2 + (min(abs(self.c-c), COLUMNS-abs(self.c-c)))**2) <= RAYON**2
        return isCouvert

    def get_couverture_nb(self):
        nb = 0
        for cible in cibles:
            if self.couvre(cible[0], cible[1]):
                nb += 1
        return nb

    def maj_position(self):
        if self.actif == True:
            if self.altitude > 0 and self.altitude <= ALTITUDES:
                vecteur = altitudes[self.altitude-1][self.r][self.c]

                r = self.r + vecteur[0]
                c = (self.c + vecteur[1])%COLUMNS

                if r < 0 or r >= ROWS:
                    self.actif = False
                else:
                    self.r = r
                    self.c = c

    def can_move_up(self):
        return self.altitude < ALTITUDES
    def can_move_down(self):
        return self.altitude > 1

def calcul_score():
    score = 0


    for tour in ballons_tours:
        done = {}

        for ballon in tour:
            if ballon.actif and ballon.altitude > 0:

                for cov in cover[ballon.r][ballon.c]:

                    if cov not in done:
                        score +=1
                        done[cov] = True


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

cover = []

for i in range(ROWS):
    row = []
    for j in range(COLUMNS):
        row.append([])
    cover.append(row)

for i in range(ROWS):
    for j in range(COLUMNS):

        for x in range(-RAYON, RAYON+1):
            for y in range(-RAYON, RAYON+1):

                r = i + x
                c = (j + y)%COLUMNS

                if r >= 0 and r < ROWS:
                    if cibles_dict[(r,c)] == True:
                        isCouvert = ((i - r)**2 + (min(abs(j-c), COLUMNS-abs(j-c)))**2) <= RAYON**2
                        if isCouvert:
                            cover[i][j].append((r,c))


############################################

for i in range(1, TOURS):
    ballons = []

    for j in range(BALLONS):
        b = copy.deepcopy(ballons_tours[i-1][j])

        print 'old_direction: ' + str(b.direction)

        if b.altitude > 0:
            nb_couv = b.get_couverture_nb()   # nombre de cibles couvertes par ce ballon

            vecteur1 = altitudes[b.altitude-1][b.r][b.c]
            vecteur2 = altitudes[b.altitude-1-1][b.r][b.c]

            if b.altitude < ALTITUDES-1:
                vecteur3 = altitudes[b.altitude+1-1][b.r][b.c]

            if nb_couv < 5:                 # on veut bouger rapidement
                if b.altitude == ALTITUDES-1:
                    vecteur3 = [0, 0]
                if vecteur1[0] >= vecteur2[0] and vecteur1[0] >= vecteur3[0]:
                    b.stay()
                elif vecteur2[0] >= vecteur1[0] and vecteur2[0] >= vecteur3[0]:
                    b.move_down()
                elif vecteur3[0] >= vecteur2[0] and vecteur3[0] >= vecteur1[0]:
                    b.move_up()
            else:                           # on ne veut pas bouger
                if b.altitude == ALTITUDES-1:
                    vecteur3 = [100000, 100000]
                if vecteur1[0] <= vecteur2[0] and vecteur1[0] <= vecteur3[0]:
                    b.stay()
                elif vecteur2[0] <= vecteur1[0] and vecteur2[0] <= vecteur3[0]:
                    b.move_down()
                elif vecteur3[0] <= vecteur2[0] and vecteur3[0] <= vecteur1[0]:
                    b.move_up()
        else:
            b.move_up()

        print 'new_direction: ' + str(b.direction)


        # rd = [0]
        # if b.can_move_up():
        #     rd.append(1)
        # if b.can_move_down():
        #     rd.append(-1)

        # a = random.choice(rd)

        # if a == -1:
        #     b.move_down()
        # elif a == 1:
        #     b.move_up()
        # elif a == 0:
        #     b.stay()

        b.maj_position()

        ballons.append(b)

    ballons_tours.append(ballons)

############################################
############################################
############################################

# for i in range(TOURS):
#     couverture = get_couverture(ballons_tours[i])
#     os.system('clear')
#     print_map(couverture)
#     print ballons_tours[i]
#     print "ROUND %s" % (i,)

score = calcul_score()
write_file(0)

