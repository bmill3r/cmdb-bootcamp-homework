#!/usr/bin/env python

import sys
from blastout import BLASTreader

blast = BLASTreader(sys.stdin)

for seq_id, human in blast:
    print seq_id, human