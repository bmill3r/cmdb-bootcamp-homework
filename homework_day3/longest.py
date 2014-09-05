#!/usr/bin/env python
"""
Parses fasta file and returns list of 100 longest sequences

Uses Class FASTAReader made in fasta.py module to parse fasta file

"""
#fasta_file = "/Users/cmdb/data/day1/cufflinks_out/transcripts.fa"


import sys
from fasta import FASTAReader


reader = FASTAReader(sys.stdin)

sequence_list = []
for seq_id, sequence in reader:
    sequence_list.append(seq_id[:24] + ":" + sequence)

sorted_list = sorted(sequence_list, key=len, reverse=True)

longest_sequences = sorted_list[:100]

return longest_sequences
#for i in longest_sequences:
#    print type(i)






#for i in sorted_list:
#    print len(i)





#print len(longest_sequences)
    

#sequence_name = []

#with open(fasta_file) as f:
#    for line in read_line(f):
#        if line == "":
#            break
#        elif line.startswith(">"):
#            sequence_name.append(line[1:24].rstrip("\r\n"))
#        elif line.