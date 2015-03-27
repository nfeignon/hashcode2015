import math
import sys
import os

if __name__ == '__main__':
    print "Hash code test round"

    R,C,H,S = [int(i) for i in raw_input().split()]
    
    print "R:%s, C:%s, H:%s, S:%s" % (R,C,H,S)
    pizza = []
    
    for i in range(R):
        pizza.append(raw_input())
        print pizza[i]
