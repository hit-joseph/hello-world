# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    infile = ur"/users4/xyan/data_bank/paraphrase_table_by_Wang/extract-src/paraphrase1.txt"
    count = 0
    with open(infile, "r")as inp:
        for line in inp:
            line = line.strip().decode("utf-8").split(u"\t")
            length = len(line) - 1
            count += length

    print count
