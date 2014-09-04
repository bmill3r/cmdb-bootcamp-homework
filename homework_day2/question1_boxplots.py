#!/usr/bin/env python

import pandas as pd

SRR072893 = "/Users/cmdb/data/results/SRR072893_clout/genes.fpkm_tracking"
SRR072915 = "/Users/cmdb/data/results/SRR072915_clout/genes.fpkm_tracking"

df1 = pd.read_table(SRR072893)
df2 = pd.read_table(SRR072915)

sorted_df1 = df1.sort("FPKM")
sorted_df2 = df2.sort("FPKM")

#print df1_fpkm.describe()
#print df2_fpkm.describe()

#print df1_fpkm.tail()
#print df1_fpkm.head()

#15602 values....

fpkm1 = sorted_df1["FPKM"]
fpkm2 = sorted_df2["FPKM"]

fpkm1_bottom = fpkm1[:5201]
fpkm1_middle = fpkm1[5201:10402]
fpkm1_highest = fpkm1[10402:]

fpkm2_bottom = fpkm2[:5201]
fpkm2_middle = fpkm2[5201:10402]
fpkm2_highest = fpkm2[10402:]

#print fpkm2_middle.describe()
#print fpkm2_bottom.describe()



a_list=[]
for i in fpkm1_bottom:
    a_list.append(i)

b_list=[]
for i in fpkm1_middle:
    b_list.append(i)

c_list=[]
for i in fpkm1_highest:
    c_list.append(i)

d_list=[]
for i in fpkm2_bottom:
    d_list.append(i)

e_list=[]
for i in fpkm2_middle:
    e_list.append(i)

f_list=[]
for i in fpkm2_highest:
    f_list.append(i)


master_list=[]
for i in a_list, b_list, c_list, d_list, e_list, f_list:
    master_list.append(i)



#print d_list[:100]
#print e_list[:100]

import matplotlib.pyplot as plt

plt.figure()
plt.boxplot(master_list)
plt.axis([0,7,0,100])
plt.savefig("boxplot.png")

#plt.boxplot(a_list)
#plt.savefig("boxplot_fpkm893_male_bottom.png")

#plt.boxplot(b_list)
#plt.savefig("boxplot_fpkm893_male_middle.png")

#plt.boxplot(c_list)
#plt.savefig("boxplot_fpkm893_male_highest.png")

#plt.boxplot(d_list)
#plt.savefig("boxplot_fpkm915_female_bottom.png")

#plt.boxplot(e_list)
#plt.savefig("boxplot_fpkm915_female_middle.png")

#plt.boxplot(f_list)
#plt.savefig("boxplot_fpkm915_female_highest.png")


#print fpkm1_bottom.describe()

#plt.boxplot(fpkm1_bottom)
#plt.savefig("boxplot.png")





    