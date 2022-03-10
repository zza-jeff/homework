#!/usr/bin/env python3
# final project: independent and identically distributed

import argparse
import random
import math
import mcb185

parser = argparse.ArgumentParser(description='Brief description of program.')
parser.add_argument('--seq', required=True, type=str,
	metavar='<str>', help='require a string to locate the file')
arg = parser.parse_args()

aa = 'ACDEFGHIKLMNPQRSTVWY'
result = {}

"""
# null sequence (deprecated)
nullseq = ''
for i in range(arg.len):
    nullseq += random.choice(aa)
nullstat = mcb185.compos(nullseq)
"""

for name, seq in mcb185.read_fasta(arg.seq):
	seq = seq.rstrip('*')
	stat = mcb185.compos(seq)
	kldiverge = {x: n * math.log(n / (1 / len(aa))) for x, n in stat.items()}
	# if IID, every letter should have probability of 1/20
	if name not in result: result[name] = sum(kldiverge.values())
	print(f'\n{name}\n{"k-l divergence = "}{result[name]:.6f}\n')
	for l, div in sorted(kldiverge.items()):
	    print(f'{l}\t{div:.6f}')