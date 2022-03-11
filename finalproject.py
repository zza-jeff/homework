#!/usr/bin/env python3
# final project: independent and identically distributed
# The program is able to: 1. Compare single protein to null model; 2. Compare single protein with other proteins in file

import argparse
import itertools
import math
import mcb185

parser = argparse.ArgumentParser(description='Validate IID')
parser.add_argument('--seq', required=True, type=str,
	metavar='<str>', help='require a string to locate the file')
arg = parser.parse_args()

letter = 'ACDEFGHIKLMNPQRSTVWY'

"""
# null sequence (deprecated)
nullseq = ''
for i in range(arg.len):
    nullseq += random.choice(aa)
nullstat = mcb185.compos(nullseq)
"""

protein = {name: seq.rstrip('*') for name, seq in mcb185.read_fasta(arg.seq)}

for id, aa in protein.items():
    stat = mcb185.compos(aa)
    nullkldiverage = {x: n * math.log(n / (1 / len(letter))) for x, n in stat.items()}
    print(f'\n\n{id}\n{"k-l divergence to null model = "}{sum(nullkldiverage.values()):.8f}\n')
    for id1, aa1 in protein.items():
        stat1 = mcb185.compos(aa1)
        kldiverage = {x1: n1 * math.log(n1 / stat[x1]) for x1, n1 in stat1.items() if x1 in stat.keys()}
        print(f'{id1[0:11]}\t{"k-l divergence to "}{id[0:11]}{" = "}{sum(kldiverage.values()):.8f}')