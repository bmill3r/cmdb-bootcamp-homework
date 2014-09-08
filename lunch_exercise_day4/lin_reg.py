#!/usr/bin/env python

import pandas
import sys
import matplotlib.pyplot as plot
import statsmodels.api as sm
import math

import ast

from fasta import FASTAReader



reader = FASTAReader(sys.stdin)

#f = open('gc_content.txt', 'w')

#gc_dict = {}
gc_list = []
#id_list = []
for id_sig, sequence in reader:
    #id_list.append(id_sig)
    
    c = sequence.count("C")
    
    g = sequence.count("G")
    length = float(len(sequence))
    #print length
    gc_content = float(c + g)
    #print gc_content
    gc_percent = gc_content/length
    #print gc_percent
    gc_list.append(gc_percent)
    #gc_dict[id_sig] = gc_percent
    

#locus_gc_file = pandas.read_table(sys.stdin, index_col=0) #file containing tuples of locus_id and gc%
#print locus_gc_file

#print gc_dict



#annotated plus in same order as transcripts_500.txt....contains FPKM values....
fpkm_file = "/Users/cmdb/cmdb-bootcamp-homework/lunch_exercise_day4/annotated_plus.txt"
fpkm_data = pandas.read_table(fpkm_file, names=['1','2','3','4','5','6','7','8', '9'])

fpkm_list = []
for i in fpkm_data['9']: #column 9 is string containing info of sequence including fpkm..each piece of info separated by ;
    fpkm = i.split(';')[2] # third info is fpkm
    fpkm = fpkm.split()[1] # remove "fpkm" and keep "value"
    fpkm_value = float(ast.literal_eval(fpkm)) #convert str fpkm value to float fpkm
    if fpkm_value == 0:
        fpkm_list.append(fpkm_value)
    else:
    #print type(fpkm_value)
#        fpkm_value = math.log10(fpkm_value) #if want log of fpkm values
        fpkm_list.append(fpkm_value)
#print fpkm_list



#combine gc content and fpkm values into dataframe. Each transcript should be in same order with respect to annotated_plus/minus.txt and transcripts_plus/minus_500.fa
gc_fpkm_df = pandas.DataFrame(columns = ["GC", "FPKM"])
gc_fpkm_df["GC"] = gc_list
gc_fpkm_df["FPKM"] = fpkm_list

#print gc_fpkm_df




#model = sm.formula.ols(formula="FPKM ~ GC", data=gc_fpkm_df)

#res = model.fit()
#print res.summary()
plot.scatter(gc_fpkm_df["FPKM"], gc_fpkm_df["GC"])
plot.savefig("lm_gc_fpkm_plus_500.png")


#fpkm_gc_list = []
#headers = "locus" + "\t" + "FPKM" + "\t" + "GC%"
#fpkm_gc_list.append(headers)

#for locus in fpkm_data["locus"]:
    #print locus
#    if locus in gc_dict:
#        print found
        #find the row value that corresponds to locus...
#        entry = locus + "\t" + fpkm.loc[[row], ["FPKM"]] + "\t" + gc_dict[locus]
#        fpkm_gc_list.append(entry)
    
#print fpkm_gc_list
        
        
        


#for locus in fpkm_data['locus']:
#    print locus












#df = pandas.read_table(fpkm_file)

#df_fpkm = df.iloc[7:]
#print df_fpkm

#[9] column is FPKM
#[7] column is locus


