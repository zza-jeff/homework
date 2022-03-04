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

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('--f', required=True, type=str,
	metavar='<str>', help='require a string for file')
parser.add_argument('--w', required=True, type=int,
	metavar='<int>', help='require integer for window size')
parser.add_argument('--e', required=True, type=float,
	metavar='<float>', help='require floating point for entropy threshold')
arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.f):
    for i in range(0, len(seq) - arg.w + 1):
        window = seq[i:i+arg.w]
        num = mcb185.compos(window)
        if mcb185.shannon(num) < arg.e:
        	seq = seq.replace(window, window.lower())
    print(f'{name}\n{seq}')