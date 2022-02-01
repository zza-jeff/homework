#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
s = len(dna)
anti = ""

for i in range(s - 1, -1, -1):
    codon = dna[i]
    if codon == "A":
        anti += 'T'
    elif codon == 'T':
        anti += 'A'
    elif codon == 'G':
        anti += 'C'
    else:
        anti += 'G'

print(anti)
