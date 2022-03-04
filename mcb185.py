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
	count = {}
	total = 0
	for c in seq:
		if c not in count:
			count[c] = 0
			count[c] += 1
			total += 1
		else:
			count[c] += 1
			total += 1
	freq = {}
	for c, n in count.items():
		if c not in freq:
			freq[c] = n / total
	return freq

def shannon(num):
	entro = [num[x] * math.log2(num[x]) for x, n in num.items()]
	return -sum(entro)
