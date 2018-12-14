# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import random

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    infile = "candidata_filter.txt"
    outfile = "random500"
    all = []
    with open(infile, "r") as in_file:
        for line in in_file:
            all.append(line)
    random200 = random.sample(all, 500)
    outobj = open(outfile, "w", 0)
    for line in random500:
        outobj.write(line)
