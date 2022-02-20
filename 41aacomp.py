#!/usr/bin/env python3

import sys
assert(len(sys.argv) == 2)

# Make a program that reports the amino acid composition in a file of proteins

aa = 'WCHMYQFNPTRIDGAKEVLS' # "manually" ordered

seq = ''

with open(sys.argv[1], 'r') as fp:
    for line in fp.readlines():
        if line[0] != '>':
            seq += line

def compos(seq):
    a = seq.count('A')
    c = seq.count('C')
    d = seq.count('D')
    e = seq.count('E')
    f = seq.count('F')
    g = seq.count('G')
    h = seq.count('H')
    i = seq.count('I')
    k = seq.count('K')
    l = seq.count('L')
    m = seq.count('M')
    n = seq.count('N')
    p = seq.count('P')
    q = seq.count('Q')
    r = seq.count('R')
    s = seq.count('S')
    t = seq.count('T')
    v = seq.count('V')
    w = seq.count('W')
    y = seq.count('Y')
    return w, c, h, m, y, q, f, n ,p ,t, r, i, d, g, a, k, e, v, l , s

pro = compos(seq)
comp = [pro[i] / sum(pro) for i in range(len(aa))]


for (amino, num, per) in zip(aa, pro, comp):
    print(amino, num, per)
