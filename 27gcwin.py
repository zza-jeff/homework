#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use no nested loops. Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Describe the pros/cons of this algorith vs. nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
pt = 0
out = 0

wind = seq[0:w] # Initial Slice

for x in range(w):
    if wind[x] == 'G' or wind[x] == 'C':
        pt += 1

for i in range(0, len(seq) - 10):
    if i == 0: out = pt / w # If i = 0, do nothing.
    else:
        if wind[0] == 'G' or wind[0] == 'C':
            pt -= 1
        wind = wind[1:w]
        wind += seq[i+10]
        if wind[10] == 'G' or wind[10] == 'C':
            pt += 1
        out = pt / w
    print(i, wind, '{:.4f}'.format(out))

# Pro: More logical
# Con: Longer, less easier to code.
