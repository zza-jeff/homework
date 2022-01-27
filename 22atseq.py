#!/usr/bin/env python3

import random
# random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

seq = '' # Store sequence
nt = 30
pt = 0 # Store number of AT

for i in range(nt):
    r = random.randint(1, 4)
    if r == 1:
        seq += 'A'
    elif r == 2:
        seq += 'T'
    elif r == 3:
        seq += 'G'
    else:
        seq += 'C'
    nc = seq[i]
    if nc == 'A' or nc == 'T':
        pt += 1
    out = pt / nt # Store AT fraction

print(nt, out, seq)
