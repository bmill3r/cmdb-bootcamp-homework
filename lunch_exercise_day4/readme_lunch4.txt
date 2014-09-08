FINAL EXERCISE:

take sample 893

(transcripts from cufflinks_ouput)


determine GC content of 500 bp region around each transcription start site

build regression model of fpkm ~ gc     (maybe log it to make it easier for regression)

plots with regression line




PART 1:
Used Awk and grep to generate files containing only transcripts either from the plus strand or the minus strand:

awk '$3 == "transcript"' transcripts.gtf | grep '+' > transcripts_plus.csv
awk '$3 == "transcript"' transcripts.gtf | grep '-' > transcripts_minus.csv


PART 2:
Change the start and stop positions in the transcripts_plus/minus.csv files to positions 250bp to the left and 250 bp to the right of the start position:

transcripts.py (to return annotated_plus.txt or annotated_minus.txt)


***So far only have done this for transcripts_plus.csv***


PART 3:
Used bedtools getfasta to return sequences of the 250bp regions flanking the left and 250bp region flanking the right of the start site for each transcript (so far only used annotated_plus.txt)

bedtools getfasta -fi /Users/cmdb/data/genomes/dmel-all-chromosome-r5.57.fasta -bed annotated_plus.txt -fo transcripts_plus_500.fa



PART 4:

lin_reg.py

FASTAReader from fasta.py to pull out each sequence in transcripts_plus_500.fa (stdin)

	./lin_reg.py < transcripts_plus_500.fa




annotated_plus.txt in same order as transcripts_plus_500.fa

	(will need to change file path to annotated_minus.txt for minus strand transcripts)

FPKM value in annotated_plus.txt is in 9th column and third piece of information separated by ;

	read annotated_plus.txt to dataframe and parse out this FPKM value, convert to float and append to list

Calculate GC% using sequences in transcripts_plus_500.fa and append to list

Add FPKM values and GC% values to columns in new dataframe

Perform linear regression and plot values using scatterplot


With log FPKM values:

  OLS Regression Results                            
==============================================================================
Dep. Variable:                   FPKM   R-squared:                       0.005
Model:                            OLS   Adj. R-squared:                  0.005
Method:                 Least Squares   F-statistic:                     78.16
Date:                Sun, 07 Sep 2014   Prob (F-statistic):           1.04e-18
Time:                        21:39:55   Log-Likelihood:                -34771.
No. Observations:               16854   AIC:                         6.955e+04
Df Residuals:                   16852   BIC:                         6.956e+04
Df Model:                           1                                         
==============================================================================
                 coef    std err          t      P>|t|      [95.0% Conf. Int.]
------------------------------------------------------------------------------
Intercept      0.6978      0.101      6.880      0.000         0.499     0.897
GC            -2.1235      0.240     -8.841      0.000        -2.594    -1.653
==============================================================================
Omnibus:                     8044.280   Durbin-Watson:                   1.762
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            44834.489
Skew:                          -2.296   Prob(JB):                         0.00
Kurtosis:                       9.538   Cond. No.                         19.2
==============================================================================


For graphs: 

	lm_gc_fpkm_log_plus_500.png 	#log(FPKM) vs. gc%

	lm_gc_FPKM_plus_500.png 	#FPKM vs. gc%
