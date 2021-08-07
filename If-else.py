#Python If-Else
#Task
#Given an integer, , perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of  to , print Not Weird
#If n is even and in the inclusive range of  to , print Weird
#If n is even and greater than , print Not Weird
#Input Format

#A single line containing a positive integer, .

#Constraints
# 1 <= n <= 100
#Output Format
#Print Weird if the number is weird. Otherwise, print Not Weird.

#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(raw_input().strip())
if  n % 2 !=0:
    print "Weird"
else:
    if n >= 2 and n <=5:
        print "Not Weird"
    elif n >= 6 and n<=20:
        print "Weird"
    elif n > 20:
        print "Not Weird"
