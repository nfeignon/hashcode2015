import math
import sys
import os

pizza = []

def tester_part(R1, C1, R2, C2):

    jambons = 0
    cases = 0

    for i in range(R1, R2+1):
        for j in range(C1, C2+1):
            if pizza[i][j] == 'H':
                jambons += 1

            print pizza[i][j]

            cases += 1

    print jambons
    print cases

    if jambons >= 3 and cases <= 12:
        return True
    else:
        return False


if __name__ == '__main__':
    print "Hash code test round"

    R,C,H,S = [int(i) for i in raw_input().split()]

    print "R:%s, C:%s, H:%s, S:%s" % (R,C,H,S)

    for i in range(R):
        pizza.append(raw_input())
        print pizza[i]


    print "Parts : "

    tester_part(0, 0, 2, 1)
