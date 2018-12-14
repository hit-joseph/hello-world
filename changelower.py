# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

infile = "translation_no_web_filter.txt"
outfile = "translation_no_web_filter_lower.txt"

with open(infile, "r")as inp, open(outfile, "w", 0)as outp:
    for line in inp:
        line = line.lower()
        outp.write(line)
print "Done!"
