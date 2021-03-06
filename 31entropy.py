#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

tolorance = 0.001

# First, change input into float, then transfer into a new list
prob = [float(sys.argv[i]) for i in range(1, len(sys.argv))]

if abs(sum(prob) - 1) > tolorance:
    print('Probability sum is not equal to 1, exit.')
    sys.exit()

# Calculate entropy in a new list
entro = [prob[x] * math.log2(prob[x]) for x in range(len(prob))]

shannon = -sum(entro)

print(f'{shannon:.3f}')
