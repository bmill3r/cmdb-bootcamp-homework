*** DAY 3 - LUNCH EXERCISE ***

Lunch Exercise:  - Parsing BLAST output    

Easy: For each alignment in the blast output, print the fly and human sequence name, ratio of identifies, and ratio of gaps, for example:

pho-PA NM_003403 266/351 0/351 
pho-PA NM_206923 215/287 0/287 
pho-PA NR_033658 159/228 2/22

Medium: For each alignment, print the longest stretch of fully aligned bases in that alignment


Preliminary Setup: 

	Made blast database with refMrna.fa data:

	(in ~/data/day3)

		wget http://is.gd/GdXOrf
		mv GdXOrf refMrna.fa.gz  #rename file
		gzip -d refMrna.fa.gz
		makeblastdb -dbtype nucl -in refMrna.fa -out refMrna

			#returns refMrna.nhr, refMrna.nin, refMrna.sq

	Make file of first 15 transcripts in transcripts.fa (~/data/day1?cufflinks_ouput):

		grep -n "^>" transcripts.fa | head -n16  	#see what line the 15th ends
		head -n675 transcripts.fa | less -S		#check to make sure
		head -n675 transcripts.fa > transcripts_15.fa 	#new file with first 15 transcripts

	Make blastn output with blast database and transcripts:

		blastn -db refMrna -query transcripts_15.fa -task blastn | blastout.txt


#### Really struggled with this one.... ####

Strategy:

	First used blast.test.py to see what each line in blastout.txt looks like..

	Rewrite fastaREADER as BLASTreader to pull out desired lines.. (module in blast.py)
		line with fly name
		line with human name
		line with ratio of identities, and
		line with ration of gaps

	to this end, couldn't figure out how to write BLASTreader to do this..


	Assuming blastREADER module worked, use blast_parse.py to print out the needed information


	### Made edits to blast.py 9/7/2014 ###

	### Still doesn't work...blast.py module gives SyntaxError at elif for line 38...but elif isn't even on that line...not sure what's wrong. ###


	###Gave up on blast.py module BLASTreader### 
		Wrote def next() attribute as new blast_parse.py


Answer to Easy:

	blast_parse.py




