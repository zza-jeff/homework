#!/usr/bin/env python3

# Write a program that computes the GC fraction of a DNA sequence in a window
# Window size is 11 nt
# Output with 4 significant figures using whichever method you prefer
# Use nested loops

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11


for i in range(len(seq)-10):
    pt = 0
    out = 0 # Put them inside the loop so they will be refreshed every cycle.
    wind = seq[i:i + w]
    for x in range(w):
        if wind[x] == 'G' or wind[x] == 'C':
            pt += 1
            out = pt / 11
    print(i, wind, f'{out:.4f}')
