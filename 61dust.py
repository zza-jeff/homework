#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185


# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Output FASTA format with low entropy masking')
parser.add_argument('--f', required=True, type=str,
	metavar='<str>', help='require a string for file')
parser.add_argument('--w', required=True, type=int,
	metavar='<int>', help='require integer for window size')
parser.add_argument('--e', required=True, type=float,
	metavar='<float>', help='require floating point for entropy threshold')
parser.add_argument('--nmask', action='store_true',
	help='N-based masking')
arg = parser.parse_args()

mask = ''
for n in range(arg.w):
    mask += 'N'

for name, seq in mcb185.read_fasta(arg.f):
	entropy = {}
		
	for i in range(0, len(seq) - arg.w + 1):
	    window = seq[i:i+arg.w]
	    prob = mcb185.compos(window)
	    if i not in entropy: entropy[i] = mcb185.shannon(prob) # store entropy with starting position
	
	for c, cal in entropy.items():
		if entropy[c] < arg.e: # if below threshold starting at position "c", replace sequence
			if arg.nmask: seq = seq.replace(seq[c:c+arg.w], mask)
			else: seq = seq.replace(seq[c:c+arg.w], seq[c:c+arg.w].lower())
	print(f'{name}\n{seq}')