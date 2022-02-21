#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

aa = 'ACDEFGHIKLMNPQRSTVWY'
seq = ''
aachain = []
id = []


with open(sys.argv[1], 'r') as fp:
    for line in fp:
        if line[0] == '>':
            id.append(line[1:12]) # store sequence id and amino acid chain separately
            aachain.append(seq)
            seq = ''
        else:
            seq += line.rstrip('\n')
    aachain.append(seq)

aachain = aachain[1:len(aachain)] # delete first empty entry

def kd(seq): # calculate hydrophobicity score
    for a in seq:
        if a == 'I': score.append(4.5)
        elif a == 'V': score.append(4.2)
        elif a == 'L': score.append(3.8)
        elif a == 'F': score.append(2.8)
        elif a == 'C': score.append(2.5)
        elif a == 'M': score.append(1.9)
        elif a == 'A': score.append(1.8)
        elif a == 'G': score.append(-0.4)
        elif a == 'T': score.append(-0.7)
        elif a == 'S': score.append(-0.8)
        elif a == 'W': score.append(-0.9)
        elif a == 'Y': score.append(-1.3)
        elif a == 'P': score.append(-1.6)
        elif a == 'H': score.append(-3.2)
        elif a == 'E': score.append(-3.5)
        elif a == 'Q': score.append(-3.5)
        elif a == 'D': score.append(-3.5)
        elif a == 'N': score.append(-3.5)
        elif a == 'K': score.append(-3.9)
        elif a == 'R': score.append(-4.5)

def helix(score, s, threshold1, h, threshold2):
    sp = 0 # sp = signal peptide
    hr = 0 # hr = hydrophobic regions
    phobic = 0 # total KD score
    slice = [] # slice the transmembrane window from score
    for b in range(len(score) - h):
        if b <= 30 - s:
            slice = score[b:b+s]
            if slice.count(-1.6) == 0: # if no Proline, do following:
                phobic = sum(score[b:b+s])
                if phobic > threshold1 * s: sp += 1

        if b > 30:
            slice = score[b:b+h]
            if slice.count(-1.6) == 0:
                phobic = sum(score[b:b+h])
                if phobic > threshold2 * h: hr += 1

    if sp >= 1 and hr >= 1: print(id[i])


for i in range(len(id)):
    seq = ''
    seq = aachain[i]
    score = []
    kd(seq)
    helix(score, 8, 2.5, 11, 2.0)
