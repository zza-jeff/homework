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
parser.add_argument('--r1', required=True, type=str,
	metavar='<str>', help='require a string')
parser.add_argument('--r2', required=True, type=int,
	metavar='<int>', help='require integer')
parser.add_argument('--r3', required=True, type=float,
	metavar='<float>', help='require floating point')
arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.r1):
    for i in range(0, len(seq) - arg.r2 + 1, arg.r2):
        window = seq[i:i+arg.r2]
        num = mcb185.compos(window)
        if mcb185.shannon(num, limit = 20) < arg.r3:
            seq = seq.replace(window, window.lower())
    print(name, seq)
