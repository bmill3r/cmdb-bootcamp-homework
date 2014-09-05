#!/usr/bin/env python

import sys


#def revComp(sequence):
#    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#    seq = sequence[25:]
    #seq = sequence.split(":")[1]
#    rev_seq = seq[::-1]
#    rev_comp = [basecomplement[b] for b in rev_seq]
    
#    return rev_comp
    
def ReverseComp(seq):
    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join([basecomplement[base] for base in seq[::-1])




#simple_list =["A:AAAA", "C:CCCC"]
#longest_sequences = sys.argv[1]

#for i in longest_sequences:
#    print revComp(i)
    


longest_sequences = sys.stdin
print longest_sequences

rev_seq = []
for i in longest_sequences:
    rev_seq.append(ReverseComp(i))

print rev_seq






    