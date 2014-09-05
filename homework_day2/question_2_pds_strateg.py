#!/usr/bin/env python

import pandas

base = "/Users/cmdb/data/results/"

df = pandas.read_csv("samples.csv")   #file with "meta data....see etherpad"

all samples = {}

for sample in df["sample"]:   #header for this column...see meta data
    all_samples[sample] = pandas.read_table(base + sample + "_clout/" + "genes.fpkm_tracking")["FPKM"]  #read each sample file via file path and store in variable ???
    
df = pandas.DataFrame(all_samples) #turn above variable of fpkm data into data frame