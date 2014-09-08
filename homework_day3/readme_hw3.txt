*** DAY 3 - HOMEWORK ***

 - Extract the 100 longest assembled transcripts from your cufflinks output (transcripts.gtf) into FASTA format
 - Find ORFS in these transcripts and print all ORFs found, translated to peptide sequence using the standard genetic code


final_longest_translate.py


Strategy:


PART 1: 100 LONGEST SEQUENCES

Use FASTAReader module to parse transcripts.fa file and return sequences

append each sequence asitem in list

sort items in list by length

make new list with longest 100 items (aka longest sequences)




PART 2: TRANSLATE SEQUENCES IN 6 READING FRAMES
***Because it takes an incredible amount of time to process entire long list, made test list with 2 shortest sequences from the list of 100.***


Made a new list of reverse complements of each sequence, used dictionary of complement bases

Wrote new function translate, which uses a codon:aminoacid dictionary to translate each sequences. Can also designate the reading frame (1, 2 or 3)

To deal with the six possible reading frames (3 in the 5'->3' and 3 in the 3'->5'), created 6 lists (3 for list of original sequences and 3 for the reverse complement sequences):

Translate function was performed on each sequence in either the original sequence list or reverse complement sequence list for each reading frame and the resulting amino acid sequences were appended one one of the six appropriate lists.




PART 3: FINDING OPEN READING FRAMES FOR GIVEN LIST OF TRANSLATED SEQUENCES
***Because only one of the six previous lists can be fed into this portion of the script during a single run, the script must be rerun for each list of translated sequences***


Use regular expression to find positions of each M (methionine) in a sequences

Use start positions to make sub-sequences beginning at each M in original sequence

	Split these subsequences on the stop codon ( ".") to create the open reading frame (orf)
	
	Create a threshold (only take orf longer than 10 characters)

	Use sequence of orf as a regular expression to find its end position in the original sequence

	Append the start and stop positions as well as the orf as a tuple to a list





