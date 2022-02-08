#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

stats = [int(sys.argv[i]) for i in range(1, len(sys.argv))]
size = stats[0]
read = stats[1]
length = stats[2]

# create empty list
coverage1 = [0] * size

# make random sequence
seq = ''
for x in range(size):
    r = random.randint(1, 4)
    if r == 1: seq += 'A'
    elif r == 2: seq += 'T'
    elif r == 3: seq += 'G'
    else: seq += 'C'

# read sequence
for y in range(read):
    start = random.randint(0, size - length)
    for z in range(start, start + length):
        coverage1[z] += 1

coverage2 = coverage1[10:size - 10] # ignore first and last 10 base
coverage2.sort()
min = coverage2[0]
max = coverage2[len(coverage2) - 1]
avg = sum(coverage2) / len(coverage2)
print(min, max, f'{avg:.5f}')
