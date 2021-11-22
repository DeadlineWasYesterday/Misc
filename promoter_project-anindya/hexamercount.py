# hexamercount.py
# INPUT: FASTA file containing 1kb upstream promoter sequences
# OUTPUT: CSV file of count of all possible hexamers; CSV file of count of selected hexamers

from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
import pandas as pd
import csv

readFile = open('IRGSP-1.0_1kb-upstream_2021-11-11.fasta', 'r')
writeFileName = "hexamer_rawcounts.csv"

seqLen = 1000
shortSeqLen = 6
rawCounts = {}
header = ['Hexamer'] + list(range(-seqLen, 0))
records = SeqIO.parse(readFile, 'fasta')

n = 0

for record in records:
	sequence = str(record.seq)
	for i in range(seqLen - shortSeqLen):
		shortSeq = sequence[i:i+6].upper()
		if shortSeq not in rawCounts:
			rawCounts[shortSeq] = [0]*seqLen
		rawCounts[shortSeq][i] += 1
	n += 1
	print(n, end='\r')

with open(writeFileName, "w", newline="") as writeFile:
	writer = csv.writer(writeFile)
	writer.writerow(header)
	for item in rawCounts:
		writer.writerow([item] + rawCounts[item])

with open("hexamer_rawcounts_selected.csv", 'w', newline='') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerow(header)
	for key in ['CTCTTC', 'GAAGAG', 'CCTTTT', 'CTATAA', 'TTATAG', 'TGGGCC', 'GGCCCA', 'TGAACC', 'TGAGCC']:
		writer.writerow([key] + rawCounts[key])