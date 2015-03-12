import math
import sys
import os

if __name__ == '__main__':
    print 'Hash code'

    rangees, emplacements, n_indisponibles, groupes, n_serveurs = [int(i) for i in raw_input().split()]

    indisponibles = []
    serveurs = []

    for i in range(n_indisponibles):
        indisponibles.append([int(j) for j in raw_input().split()])

    for i in range(n_serveurs):
        serveurs.append([int(j) for j in raw_input().split()])

    print indisponibles
    print serveurs
