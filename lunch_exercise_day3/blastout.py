'''
***********  BLASTreader module  ***********


This is a module that can be imported and used within other .py scripts
    
Creates a new class called BLASTreader
    Takes a blast.txt file as input from stdin via command line
    
    
'''


import sys

class BLASTreader(object):
    def __init__(self, file):
        self.file = file
        self.last_seq_id = None
 
       
    def next(self):

        fly_id = []
        human_id = []
        identities = []
        gaps = []
        while True:
            line = sys.stdin.readline()
            if line == "":
                raise StopIteration
            elif line.startswith("Query="):
                fly_id.append(line[6:].rstrip("\r\n"))
                break
            elif line.startswith(">"):
                human_sequence.append(line.strip())
                break
            elif 
            elif
            #else:
            #    info.append(line.strip())
        #output = "".join(info)
        return seq_id, human_sequence

    
    def __iter__(self):
        return self
