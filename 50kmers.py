#!/usr/bin/env python3
# 50kmers.py

import sys
assert(len(sys.argv) == 3)

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

seq = ''
filename = sys.argv[1]
k = int(sys.argv[2])
count = {}
total = 0

with open(filename, 'r') as fp:
    for line in fp.readlines():
        if line[0] != '>':
            seq += line.rstrip('\n')

for i in range(len(seq) - k + 1):
    kmer = seq[i:i+k]
    if kmer not in count:
        count[kmer] = 0
        count[kmer] += 1
        total += 1
    else:
        count[kmer] += 1
        total += 1

for x, y in sorted(count.items(), key=lambda item: item[0]):
    print(f'{x}\t{y}\t{y/total:.4f}')
