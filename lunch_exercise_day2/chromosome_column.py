#!/usr/bin/env python

f = open("/Users/cmdb/data/day1/SRR072893_tophat_out/accepted_hits.sam")

chromosome=[]
for line in f:
    fields = line.rstrip("\r\n").split("\t")
    chromosome.append(fields[2])
print chromosome


# column 3 in sam file lists chromosome read aligned to