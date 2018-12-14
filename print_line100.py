# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

filename = sys.argv[1]
print "the filename is %s" % filename

with open(filename, "r") as inp:
    count = 0
    for line in inp:
        if count < 100:
            print line
            count += 1
        else:
            break

print "Done!"
