#!/usr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments

filename = sys.argv[1]
pattern = sys.argv[2]

seq = ''
seq1 = ''
site = []
extract = '(\s)([acgt]+)(\s*)([acgt]+)(\s*)([acgt]+)(\s*)([acgt]+)(\s*)([acgt]+)(\s*)([acgt]+)(\s*)'

with open(filename, 'r') as fp:
    for line in fp.readlines():
        match = re.search(extract, line)
        if match: seq += match.group()

seq = seq.split()
for i in range(len(seq)):
    seq1 += seq[i]

site.append(0)
for cut in re.finditer(pattern, seq1):
    site.append(cut.start())
site.append(len(seq1))

for x in range(len(site) - 1):
    print(site[x+1] - site[x])
