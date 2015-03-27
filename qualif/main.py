import math
import sys
import os

pizza = []

def partager_pizza(R,C,H,S, pizza):

    parts = []

    for i in range(R):
        for j in range(C):
            
            R1 = i
            C1 = j

            for x in range(4):
                for y in range(4):

                    R2 = i + x
                    C2 = j + y

                    size = (R2-R1+1)*(C2-C1+1)

                    if size >= 3 and size <= 12:
                        if tester_part(R1, C1, R2, C2):
                            parts.append([R1, C1, R2, C2])

if __name__ == '__main__':
    print "Hash code test round"

    R,C,H,S = [int(i) for i in raw_input().split()]
    
    print "R:%s, C:%s, H:%s, S:%s" % (R,C,H,S)
    
    for i in range(R):
        pizza.append(raw_input())
        print pizza[i]
