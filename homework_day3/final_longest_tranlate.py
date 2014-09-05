#!/usr/bin/env python

#fasta_file = "/Users/cmdb/data/day1/cufflinks_out/transcripts.fa"


import sys
import re
from fasta import FASTAReader

basecomplement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}


reader = FASTAReader(sys.stdin)
#print "reader made"

#list of longest 100 sequences...headers were included but later removed b/c split(":") not working...
sequence_list = []
for seq_id, sequence in reader:
    sequence_list.append(sequence)    #seq_id[:24] + ":" + sequence
sorted_list = sorted(sequence_list, key=len, reverse=True)
longest_sequences = sorted_list[:100]

#test list of last 2 seqs in list b/c takes waaaay too long to run all...
test_list = longest_sequences[98:]
#print "test_list made"

#make list of reverse compliments of sequences (in same order as original list)
reverse_comp_sequences = []
for i in test_list:#longest_sequences:
    rev_seq = "".join(i[::-1])
    rev_comp = "".join([basecomplement[base] for base in rev_seq])
    reverse_comp_sequences.append(rev_comp)
#print "rev comp made"



dna_codon_dict = { "TTT" : "F", "TCT" : "S", "TAT" : "Y", "TGT" : "C", \
"TTC" : "F", "TCC" : "S", "TAC" : "Y", "TGC" : "C", \
"TTA" : "L", "TCA" : "S", "TAA" : ".", "TGA" : ".", \
"TTG" : "L", "TCG" : "S", "TAG" : ".", "TGG" : "W", \
"CTT" : "L", "CCT" : "P", "CAT" : "H", "CGT" : "R", \
"CTC" : "L", "CCC" : "P", "CAC" : "H", "CGC" : "R", \
"CTA" : "L", "CCA" : "P", "CAA" : "Q", "CGA" : "R", \
"CTG" : "L", "CCG" : "P", "CAG" : "Q", "CGG" : "R", \
"ATT" : "I", "ACT" : "T", "AAT" : "N", "AGT" : "S", \
"ATC" : "I", "ACC" : "T", "AAC" : "N", "AGC" : "S", \
"ATA" : "I", "ACA" : "T", "AAA" : "K", "AGA" : "R", \
"ATG" : "M", "ACG" : "T", "AAG" : "K", "AGG" : "R", \
"GTT" : "V", "GCT" : "A", "GAT" : "D", "GGT" : "G", \
"GTC" : "V", "GCC" : "A", "GAC" : "D", "GGC" : "G", \
"GTA" : "V", "GCA" : "A", "GAA" : "E", "GGA" : "G", \
"GTG" : "V", "GCG" : "A", "GAG" : "E", "GGG" : "G" }

def translate(seq, frame):  #frame either 1, 2 or 3
    proteinSeq = []
    i = frame - 1
    while i+2 < len(seq):
        codon = seq[i:i+3]
        aminoacid = dna_codon_dict[codon]
        proteinSeq.append(aminoacid)
        i += 3
    return "".join(proteinSeq)
#print "translate def made"


#Create 6 lists, for either 5'-3' frame 1, 2, or three or 3'-5' frame 1, 2, 3
#could use name of each sequence to help label, but couldn't get .strip(":") to work so had to remove earlier concatenation
#ex: seq = i.split(":")[0]...kept getting syntax error....when attempting to loopthrough elements in longest_sequences list..


frameone_seqs = []
frametwo_seqs = []
framethree_seqs = []

for i in test_list:                        #replace with longest_sequences
    frames = [1, 2, 3]
    frame_one_aa = translate(i, frames[0])
    frame_two_aa = translate(i, frames[1])
    frame_three_aa = translate(i, frames[2])
    
    frameone_seqs.append(frame_one_aa)
    frametwo_seqs.append(frame_two_aa)
    framethree_seqs.append(frame_three_aa)
    #print frame_one_aa
    #print frame_two_aa
    #print frame_three_aa

frameone_seqs_revcomp = []
frametwo_seqs_revcomp = []
framethree_seqs_revcomp = []

for i in reverse_comp_sequences:
    frames = [1, 2, 3]
    frame_one_aa = translate(i, frames[0])
    frame_two_aa = translate(i, frames[1])
    frame_three_aa = translate(i, frames[2])
    
    frameone_seqs_revcomp.append(frame_one_aa)
    frametwo_seqs_revcomp.append(frame_two_aa)
    framethree_seqs_revcomp.append(frame_three_aa)

#could use name of each sequence to help label, but couldn't get .strip(":") to work so had to remove earlier concatenation



#Finding ORFs using regular expression on translated sequences

met = "M"
m = re.compile(met)


for i in frameone_seqs:     #for each translated sequence in given list....
    start_positions = []
    orfs = []
    for match in m.finditer(i):                          #iterate through matches with "M"
        start = match.start()                            #record position of match
        start_positions.append(start)                    #append positions of these "M" matches aka start positions to list
    for orf_start in start_positions:
        rf = i[orf_start:]                               #pull out reading frames starting at each "M"
        orf = rf.split(".", 1)                           #for each rf pulled out, split on "." aka stop codon and take first part
        if len(orf[0]) > 10:                             #check/cutoff for length of a rf (M to .)
            orf_re = re.compile(orf[0])                  #create regex out of extrcted rf
            orf_seq = orf_re.search(i)                   #search original translated file for rf
            orf_end = orf_seq.end()                      #find end position of the rf
            orfs.append((orf_start, orf_end, orf[0]))    #store start, end position as well as sequence in tuple and append to list
    
    print orfs                                           #print orfs (list of tuples) for given translated sequence in a given frame/directionality)






#frameone_seqs = []
#frametwo_seqs = []
#framethree_seqs = []
#for i in test_list:
#    frames = [1, 2, 3]
#    for f in frames:
#        if f == 1:
#            frame_one_aa = translate(i, f)
#            frameone_seqs.append(frame_one_aa)
#        elif f == 2:
#            frame_two_aa = translate(i, f)
#            frametwo_seqs.append(frame_two_aa)
#        elif f == 3:
#            frame_three_aa = translate(i, f)
#            framethree_seqs.append(frame_one_aa)
            
    #frame_one_aa = translate(i, frames[0])
    #frame_two_aa = translate(i, frames[1])
    #frame_three_aa = translate(i, frames[2])
    #print frame_one_aa
    #print frame_two_aa
    #print frame_three_aa












