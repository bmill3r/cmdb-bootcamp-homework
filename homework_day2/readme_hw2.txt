*** DAY 2 - HOMEWORK ***

NOTE: place all your Python code into a file and add it to your Github repository

Basic Exercises

1. Make boxplot of top/middle/bottom 1/3rd-ish FPKMs for SRR072893, SRR072915
  - HINT: pass plt.boxplot() a 3-element ** list **

	question1_boxplots.py

		Workflow:
		
		A. created dataframes from genes.fpkm_tracking files
		B. sorted dataframes by FPKM values
		C. stored the sorted FPKM values from each dataframe
		D. separated each series of FPKM values into thirds
			(6 series total b/c two files split into thirds..)
		E. For some reason, boxplot would only take values in list..so converted series into lists
		F. appended each list into a master list
		G. plotted via matplotlib.boxplot and adjusted y-axis values to improve visualization

		
	see: boxplot.png

	
2. Extract Sxl expression for female 10/11/12/13/14A/14B/14C/14D
  - HINT: create a file called sample metadata to use in a for loop

sample,sex,stage
SRR072893,male,10
SRR072894,male,11
SRR072895,male,12
SRR072896,male,13
SRR072897,male,14A
SRR072899,male,14B
SRR072901,male,14C
SRR072903,male,14D
SRR072905,female,10
SRR072906,female,11
SRR072907,female,12
SRR072908,female,13
SRR072909,female,14A
SRR072911,female,14B
SRR072913,female,14C
SRR072915,female,14D


	question2_Sxl_extract.py

		Strategy:
			Pull out the line containing "Sxl" from gene.fpkm_tracking file for each desired female sample
			and write these lines to new .csv file (only one "Sxl" per gene.fpkm_tracking file)

		Workflow:

		A. Make a list of each file
		B. Open each file
		C. Check if "Sxl" in each line, and if it is, append to a list

		D. For each "Sxl" line, split values on '\t' into fields
		E. append these values to a list
		F. append this list of fields to a 'master list' (list_of_lists)
		G. Write each item (list of fields) from list_of_lists to as a new tab delimited line in sxl_file.csv

	see: sxl_file.csv
			

### Realize now that could have just appended each Sxl line in list (at step C) to the file..Didn't need to split..


3. Chart female Sxl expression
  - HINT 1: .append() values extracted in #2 to a list and pass to plt.plot()
  - HINT 2: pmid 21346796 fig 3B

	question3_chart_sxl.py

		Workflow:
	
		A. Read sxl_file.csv as dataframe (make sure first line is not read as header)
			#(each '\t' in file would separate fields into columns..)
		B. plot column 9 in dataframe
			(contains FPKM value)

	see: sxl_plot.png

	



