#!/usr/bin/env python3

import argparse
import random
import math
import mcb185

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('--seq', required=True, type=str,
	metavar='<str>', help='require a string to locate the file')
parser.add_argument('--len', required=True, type=int,
	metavar='<int>', help='require integer for null sequence length')
parser.add_argument('--kmer', required=True, type=int,
	metavar='<int>', help='require integer for kmer length')
arg = parser.parse_args()

kmer = {}
nullseq = ''

base = "ATGC"

for i in range(arg.len):
    nullseq += random.choice(base)

for a in range(len(nullseq) - arg.kmer + 1):
    window = nullseq[a:a+arg.kmer]
    if window not in kmer: kmer[window] = 0

for name, seq in mcb185.read_fasta(arg.seq):
    for b in range(len(seq) - arg.kmer + 1):
        frame = seq[b:b+arg.kmer]
        if frame in kmer: kmer[frame] += 1

for poss, n in kmer.items():
    if n == 0: print(poss)