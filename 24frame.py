#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

"""
# Simple loop
frame = 0

for i in range(len(dna)):
    if i % 3 == 0: frame = 0
    elif i % 3 == 1: frame = 1
    else: frame = 2
    print(i, frame, dna[i])
"""
# Nested loops
n = -1

for i in range(0, len(dna) -2, 3):
    for frame in range(3):
        codon = dna[i:i+3]
        n += 1
        print(n, frame, codon[frame])
