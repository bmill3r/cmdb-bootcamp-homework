#!/usr/bin/env python

import pandas

transcripts_plus = "/Users/cmdb/cmdb-bootcamp-homework/lunch_exercise_day4/transcripts_plus.csv"
transcripts_minus = "/Users/cmdb/cmdb-bootcamp-homework/lunch_exercise_day4/transcripts_minus.csv"

annotated_file = open('annotated_plus.txt', 'w')
for line in open(transcripts_plus):
    a, b, c, d, e, f, g, h, i = line.split('\t')
    start = int(d) - 250
    if start < 1:
        start = 1
    end = int(d) + 250
    new_line = a + '\t' + b + '\t' + c + '\t' + str(start) + '\t' + str(end) + '\t' + f + '\t' + g + '\t' + h + '\t' + i
    annotated_file.write(new_line)
        
    

    
    
#/Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta    
    

    
    
    #list_line.append(d)
#print list_line
    
    
    
    #list_line.append(line)
#print list_line
    



#df_plus = pandas.read_table(transcripts_plus, names=["1","2","3","4","5","6","7","8","9"])
#df_minus = pandas.read_table(transcripts_minus, names=["1","2","3","4","5","6","7","8","9"])

#print df_plus["4"]
#for i in df_plus[4]:
#    start = i-250
#    end = i+250
#    df_plus["4"] = start
#    df_plus["5"] = end
#print df_plus["4"]
    


#print df_plus