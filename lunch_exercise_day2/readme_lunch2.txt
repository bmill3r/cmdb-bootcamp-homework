*** DAY 2 - LUNCH EXERCISE ***

Explore .SAM file generated during last night's homework (accepted_hits.sam)

	/Users/cmdb/data/day1/SRR072893_tophat_out/accepted_hits.sam

Basic Exercises

NOTE: place all your Python code into a file and add it to your Github repository

1. Count number of alignments
  - HINT: counter variable

	count_alignments.py > question_1.out

2. Count number of alignments that match perfectly to the genome
  - HINT: google sam format optional fields

	count_alignments_perfect_match.py > question_2.out

		#used "NM:i:0" values in .sam file

3. Count number of reads that map to exactly one location in the genome
  - HINT: number of hits

	unique_match.py > question_3.py

		#used "NH:i:1" values in .sam file

4. Extract just the column indicating which chromosome read aligns too
  - HINT: .split()

	chromosome_column.py



#### Did not get to 5, 6, or 7... ####


