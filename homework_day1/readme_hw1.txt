Notes for Homework:

A. First:
	Perform a standard RNA-seq analysis on the male stage 10 embryo (SRR072893) using 	the Tuxedo suite

	Basic Exercises

	1. Quality control the reads using FastQC
        HINT: fastqc

	2. Map and quantitate using TopHat (~60 minutes) and Cufflinks (~10 minutes)
        NOTE 1: for TopHat use the -p -G -o --no-novel-juncs options, as well as setting 	--segment-length 20
        NOTE 2: for Cufflinks use the -p -G -o options
        HINT: pmid 22383036

	3. Push the resulting genes.fpkm_tracking file to your Github repository

	4. Convert the accepted_hits.bam file to the human readable .SAM format
        HINT: samtools view

	STEPS:

	bowtie2-build [options]* <reference_in> <bt2_index_base>
		
		reference_in == dmel-all-chromosome-r5.57.fasta (located in ~/data/genomes)
		bt2_index_base == ~/data/genomes  (directory to store bt2 indices...)  # ~/data/genomes


	 tophat -p 4 -G ~/data/day1/gff/dmel-all-r5.57-removeFASTA.gff -o SRR072893_tophat_out --no-novel-juncs --segment-length 20 ~/data/genomes/dmel-all-chromosome-r5.57 SRR072893.fastq

		tophat [options] <bowtie_index> <reads>  #bowtie2 indices all in genomes directory; SRR072893.fastq in ~/data/fastq as .gz but gunzip and copied to day1 folder

		-p/--num-threads               <int>       [ default: 1                   ]

		-G/--GTF                       <filename>  (GTF/GFF with known transcripts)  #GTF is file with annotated locations of genes/transcripts in genome

		-o/--output-dir                <string>    [ default: ./tophat_out         ]  #contains accepted_hits.bam


	cufflinks -p 4 -G ~/data/day1/gff/dmel-all-r5.57-removeFASTA.gff -o cufflinks_out ~/data/day1/SRR072893_tophat_out/accepted_hits.bam

		cufflinks [options] <hits.sam>      # can take .bam file too

			(output directory is in ~/data/day1)

		#output has:
		gene.fpkm_tracking 	#fpkm values for transcripts
		#transcripts.gtf	#annotated file for transcripts


		#transcripts.fa		#fasta file of transcripts, generated via: gtf_to_fasta



	samtools view accepted_hits.bam > accepted_hits.sam 

		# to convert .bam file in ~/data/day1/SRR072893_tophat_out to .sam file


B. Make edits to bash script:

	Debug this below Bash script to automatically run FastQC/TopHat/Cufflinks on all 24 samples in SRP004442
        HINT 1: look up the samples in NCBI's SRA database
        HINT 2: samples begin with SRR072 (not SRX0311)

### Original Template:

echo "There are around 6 mistakes"

FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
=SRR072

GENOME_DIR=/Users/cmdb/data/genomes
=dmel5
ANNOTATION=dmel-all-r5.57.gff

CORES=4

for i in 893
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat 
  echo cufflinks


