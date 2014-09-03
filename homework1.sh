#!/bin/bash
#
# Day 1 - Homework: Part 2 - debug this bash script
#
echo "There are around 6 mistakes"
FASTQ_DIR=/Users/cmdb/data/fastq
OUTPUT_DIR=/Users/cmdb/data/day1
SAMPLE_PREFIX=SRR072
GENOME_DIR=/Users/cmdb/data/genomes
GENOME=dmel-all-chromosome-r5.57
ANNOTATION=dmel-all-r5.57.gff
CORES=4
for i in {893..916}
do
  echo fastqc $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz -o $OUTPUT_DIR
  echo tophat -p$CORES -G $OUTPUT_DIR/gff/$ANNOTATION -o $OUTPUT_DIR/th_$i --no-novel-juncs --segment-length 20 $GENOME_DIR/$GENOME $FASTQ_DIR/$SAMPLE_PREFIX$i\.fastq.gz
  echo cufflinks -p$CORES -G $OUTPUT_DIR/gff/$ANNOTATION -o $OUTPUT_DIR/cl_$i $OUTPUT_DIR/th_$i/accepted_hits.bam
done