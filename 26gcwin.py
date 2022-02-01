#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11


for i in range(len(seq) - w + 1):
    gc = 0
    out = 0 # Put them inside the loop as they only be used in it.
    wind = seq[i:i + w]
    for x in range(w):
        if wind[x] == 'G' or wind[x] == 'C':
            gc += 1
            out = gc / w
    print(i, wind, f'{out:.4f}')

# Discussed with Jan
