#!/usr/bin/env python

f = open("/Users/cmdb/data/day1/SRR072893_th_out/accepted_hits.sam")

n = 0
for line in f:
    if "SRR" in line:
        n = n+1
print n
        