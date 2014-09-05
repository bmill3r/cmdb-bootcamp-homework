#!/usr/bin/env python

from fasta import FASTAReader
import sys

reader = FASTAReader(sys.stdin)

f = open('gc_content.txt', 'w')


gc_list = []
id_list = []
for id_sig, sequence in reader:
    id_list.append(id_sig)
    
    c = sequence.count("C")
    
    g = sequence.count("G")
    length = float(len(sequence))
    #print length
    gc_content = float(c + g)
    #print gc_content
    gc_percent = gc_content/length
    #print gc_percent
    gc_list.append(gc_percent)
    
gc_percentage = zip(id_list, gc_list)


for i in gc_percentage:
    print i
    