# /usr/bin/env python
# -*- coding: utf-8 -*-
'''
抽取前100条另存为另外一个文件
'''
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

filename = sys.argv[1]
print "the filename is %s" % filename

outfile = filename + "10000"

if __name__ == "__main__":
    with open(filename, "r") as r_file, open(outfile, "w", 0) as w_file:
        count = 0
        for line in r_file:
            if count == 10000:
                break
            else:
                w_file.write(line)
                count += 1
    sys.exit(0)
