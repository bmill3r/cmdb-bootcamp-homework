#!/usr/bin/env python

f = open("/Users/cmdb/data/day1/SRR072893_th_out/accepted_hits.sam")

n = 0
for line in f:
    if "NH:i:1" in line:
        n = n+1
print n

#"NH:i:1" means only aligned to one location in reference