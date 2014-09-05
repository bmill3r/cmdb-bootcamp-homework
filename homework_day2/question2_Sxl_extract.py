#!/usr/bin/env python

import sys
import csv


SRR072905 = "/Users/cmdb/data/results/SRR072905_clout/genes.fpkm_tracking"
SRR072906 = "/Users/cmdb/data/results/SRR072906_clout/genes.fpkm_tracking"
SRR072907 = "/Users/cmdb/data/results/SRR072907_clout/genes.fpkm_tracking"
SRR072908 = "/Users/cmdb/data/results/SRR072908_clout/genes.fpkm_tracking"
SRR072909 = "/Users/cmdb/data/results/SRR072909_clout/genes.fpkm_tracking"
SRR072911 = "/Users/cmdb/data/results/SRR072911_clout/genes.fpkm_tracking"
SRR072913 = "/Users/cmdb/data/results/SRR072913_clout/genes.fpkm_tracking"
SRR072915 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

file_list = [SRR072905, SRR072906, SRR072907, SRR072908, SRR072909, SRR072911, SRR072913, SRR072915]


sxl_list=[]

for i in file_list:
    with open(i) as df:
        for row in df:
            if "Sxl" in row:
                sxl_list.append(row)
print sxl_list
print len(sxl_list)

list_of_lists = []
for i in sxl_list:
    list_of_fields = []
    fields = i.rstrip("\r\n").split("\t")
    for field in fields:
        list_of_fields.append(field)
    list_of_lists.append(list_of_fields)
    
print list_of_lists

with open("sxl_file.csv", 'wb') as f:
    writer = csv.writer(f, delimiter = '\t')
    writer.writerows(list_of_lists)
    


#df905 = pd.read_table(SRR072905)
#df906 = pd.read_table(SRR072906)
#df907 = pd.read_table(SRR072907)
#df908 = pd.read_table(SRR072908)
#df909 = pd.read_table(SRR072909)
#df911 = pd.read_table(SRR072911)
#df913 = pd.read_table(SRR072913)
#df915 = pd.read_table(SRR072915)

#df_master = [df905, df906, df907, df908, df909, df911, df913, df915]


#f = open(SRR072905)
#line = f.readlines()
#for i in line:
#    if "Sxl" in line:
#        print line

#Sxl in gene_id column