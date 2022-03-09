#!/usr/bin/env python3
# final project: independent and identically distributed

import argparse
import random
import math
import mcb185

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('--seq', required=True, type=str,
	metavar='<str>', help='require a string to locate the file')
parser.add_argument('--len', required=True, type=int,
	metavar='<int>', help='require integer for null protein length')
arg = parser.parse_args()

aa = 'ACDEFGHIKLMNPQRSTVWY'
aachain = []
nullseq = ''
result = {}

for i in range(arg.len):
    nullseq += random.choice(aa) # picking up a letter from 20 aa each time
nullstat = mcb185.compos(nullseq)
# so the random sequence is made in a IID process, use as null model

for name, seq in mcb185.read_fasta(arg.seq):
	seq = seq.rstrip('*')
	stat = mcb185.compos(seq)
	kldiverge = [stat[x] * math.log2(stat[x] / nullstat[x]) for x, n in stat.items()]
	if name not in result: result[name] = sum(kldiverge)

for k, v in sorted(result.items(), key=lambda item:item[1]):
    print(f'{k}\n{v}')