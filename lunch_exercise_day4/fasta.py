'''
This is a module that can be imported and used within other .py scripts
    ex: 'from fasta import FASTAReader'
    
Creates a new class called FASTAReader
    Takes a file as input from stdin via command line
    loops through each line, collecting the header (without the > and moves to the next line)
    lines of the sequence concatonated into single string
    
    
    
'''


import sys

class FASTAReader(object):
    def __init__(self, file):
        self.file = file
        self.last_seq_id = None
        
    def next(self):
        if self.last_seq_id is None:
            line = sys.stdin.readline()
            assert line.startswith(">")
            seq_id = line[1:].rstrip("\r\n")
        else:
            seq_id = self.last_seq_id
        
        #loop through each line in file...remember that the break statement kills the while loop, same with StopIter..
        sequences = []
        while True:
            line = sys.stdin.readline()                        #loops through each line in file
            if line == "" and not sequences:                   #checks line, at end of file?
                raise StopIteration                            #stops iteration....module ends  ****
            if line.startswith(">") or line == "":             #checks line, is header?
                self.last_seq_id = line[1:].rstrip("\r\n")     #if header, then makes it seq_id
                break                                          #and breaks the while loop, next starts again?? ****
            else:
                sequences.append(line.strip())                 #otherwise line appended to string

        sequence = "".join(sequences)                          #lines into a single string
        return seq_id, sequence                                #return header (seq_id and sequence)
    
    def __iter__(self):
        return self
