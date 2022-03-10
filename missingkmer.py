#!/usr/bin/env python3

import argparse
import itertools
import mcb185


parser = argparse.ArgumentParser(description='find kmer(s) not present')
parser.add_argument('--seq', required=True, type=str,
	metavar='<str>', help='require a string to locate the file')
arg = parser.parse_args()

for name, seq in mcb185.read_fasta(arg.seq):
    result = []
    
    for i in range(len(seq)):
        kmer = {''.join(nt): 0 for nt in itertools.product('ATGC', repeat=i+1)}
        
        for b in range(len(seq) - i):
            frame = seq[b:b+i+1]
            if frame in kmer: kmer[frame] += 1
        
        for mer, k in kmer.items():
            if k == 0: result.append(mer)
        
        if len(result) != 0:
            result.append(f'{"k="}{i+1}')
            break
    
    print(name)
    for a in range(len(result)):
        print(result[a])