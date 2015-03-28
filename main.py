import copy
import math
import sys
import os

class Ballon:
    def __init__():
        self.r = R_DEPART
        self.c = C_DEPART

    def print_ballon():
        print "Ballon %d %d" % (self.r, self.c)

def calcul_score():
    score = 0

    for c in cibles:
        for b in ballons:
            if b.r == c[0] and b.c == c[1]:
                score += 1

    print "SCORE: " + str(score)

    return score

if __name__ == '__main__':

    print "Hash code final round"

