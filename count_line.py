# /usr/bin/env python
# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

filename = sys.argv[1]
print "the filename is %s" % filename

with open(filename, "r") as inp:
    count = 0
    for line in inp:
        count += 1
    print count

print "Done!"
sys.exit(0)
