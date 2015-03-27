import copy
import math
import sys
import os

original_pizza = []

def tester_part(pizza, R1, C1, R2, C2):
    if R1 >= R2 or C1 >= C2:
        return False

    jambons = 0
    cases = 0

    for i in range(R1, R2+1):
        for j in range(C1, C2+1):
            if pizza[i][j] == 'X':
                return False

            if pizza[i][j] == 'H':
                jambons += 1

            cases += 1

    if jambons >= 3 and cases <= 12:
        return True
    else:
        return False

def partager_pizza(R,C,H,S,i_d,j_d):
    pizza = copy.deepcopy(original_pizza)

    parts = []

    for i in range(i_d, R) + range(0, i_d):
        for j in range(j_d, C) + range(0, j_d):
            R1 = i
            C1 = j

            parts2 = []
            for x in range(12):
                for y in range(12):
                    R2 = i + x
                    C2 = j + y

                    size = (R2-R1+1)*(C2-C1+1)
                    if size >= 3 and size <= 12:
                        if R2 < R and C2 < C:
                            if tester_part(pizza, R1, C1, R2, C2):
                                parts2.append([R1, C1, R2, C2])

            size_max = 0
            part_max = []

            for part in parts2:
                size = (part[2]-part[0]+1)*(part[3]-part[1]+1)
                if size > size_max:
                    size_max = size
                    part_max = part

            if len(parts2) > 0:
                parts.append(part_max)
                write_part(pizza, part_max[0], part_max[1], part_max[2], part_max[3])

    return parts

def write_part(pizza, R1, C1, R2, C2):
    for i in range(R1, R2+1):
        for j in range(C1, C2+1):
            pizza[i] = pizza[i][:j] + 'X' + pizza[i][j+1:]


def output(parts, score):
    f = open('output' + str(score) + '.txt','w')

    f.write(str(len(parts)) + '\n')
    for part in parts:
        f.write("{0} {1} {2} {3}\n".format(part[0], part[1], part[2], part[3]))

def score(parts):
    score = 0
    for part in parts:
        size = (part[2]-part[0]+1)*(part[3]-part[1]+1)
        score += size

    return score


if __name__ == '__main__':

    print "Hash code test round"

    R,C,H,S = [int(i) for i in raw_input().split()]

    print "R:%s, C:%s, H:%s, S:%s" % (R,C,H,S)

    for i in range(R):
        original_pizza.append(raw_input())

    max_score = 0
    best_parts = []
    for i in range(R):
        for j in range(C):
            parts = partager_pizza(R,C,H,S,i,j)
            score_o = score(parts)

            if score_o > max_score:
                max_score = score_o
                best_parts = parts
                print "SCORE:" + str(max_score)
                output(best_parts, max_score)


    for i in range(len(best_parts)):
        print best_parts[i]

    print 'score final:'
    score(best_parts)

