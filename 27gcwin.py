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
gc = 0

wind = seq[0:w] # Initial Slice

for x in range(w):
    if wind[x] == 'G' or wind[x] == 'C': gc += 1

for i in range(0, len(seq) - w + 1):
    if i == 0: out = gc / w # If i = 0, do nothing.
    else:
        if wind[0] == 'G' or wind[0] == 'C': gc -= 1
        wind = wind[1:w] # Delete 1 letter from the beginning
        wind += seq[i + w - 1] # Add 1 letter to the end
        if wind[w - 1] == 'G' or wind[w - 1] == 'C': gc += 1
        out = gc / w
    print(i, wind, '{:.4f}'.format(out))

# Pro: More logical
# Con: Longer, less easier to code.
