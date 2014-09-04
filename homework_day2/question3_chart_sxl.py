#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt

sxl_df = pd.read_table('/Users/cmdb/cmdb-bootcamp-homework/homework_day2/sxl_file.csv', header=None)


plt.figure()

sxl_df.plot(y=9)
plt.savefig("sxl_plot.png")


#print sxl_df

