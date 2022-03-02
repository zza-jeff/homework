# mcb185.py

import sys
import gzip
import math

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

# def other functions...

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
    return a, c, d, e, f, g, h, i, k, l, m, n, p, q, r, s, t, v, w, y

def shannon(num, limit = 20):
	comp = []
	entro = []
	comp = [num[i] / sum(num) for i in range(limit)]
	entro = [comp[x] * math.log2(comp[x]) for x in range(len(comp)) if comp[x] - 0 > 0.0001]
	return -sum(entro)
