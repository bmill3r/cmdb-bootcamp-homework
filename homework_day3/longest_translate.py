#!/usr/bin/env python

import sys
from fasta import FASTAReader

#def ReverseComp(seq):
#    basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
#    return "".join([basecomplement[base] for base in seq[::-1])


basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}




reader = FASTAReader(sys.stdin)

sequence_list = []
for seq_id, sequence in reader:
    sequence_list.append(sequence)    #seq_id[:24] + ":" + sequence

sorted_list = sorted(sequence_list, key=len, reverse=True)
longest_sequences = sorted_list[:100]


test_list = longest_sequences[98:]
#print len(test_list)


#n =0
reverse_comp_sequences = []
for i in test_list:#longest_sequences:
    #print type(i) str
    #seq = i.split(":")[0]
   # print seq
    rev_seq = "".join(i[::-1])
    #print type(rev_seq) str
    #rev_string = "".join(rev_seq)
    #print rev_string
    rev_comp = "".join([basecomplement[base] for base in rev_seq])
    #rev_comp = [basecomplement[b] for b in rev_seq] #rev_comp is list
    #rev_comp_str = "".join(rev_comp)
    reverse_comp_sequences.append(rev_comp)
#print reverse_comp_sequences
   # print rev_comp_str
    #print i
   # rev_comp = []
#    for i in rev_seq:#rev_string:
#        rev_comp.append(basecomplement[i])
#        rev_comp_string = "".join(rev_comp)
        #print rev_comp_string
#        reverse_comp_sequences.append(rev_comp_string)
        #n = n+1
        #print n
    
#print len(reverse_sequences)
#print reverse_comp_sequences[0]
#print longest_sequences[0]


#while i+2 < len(self._data):
#                        if directionality5to3 == True:
#                                codon = self._data[i:i+3]
#                                aminoAcid = self._translation_table[codon]
#                                proteinSeq.append(aminoAcid)
#                                i += 3

