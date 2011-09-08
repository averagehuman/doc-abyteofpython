
from os import path
from StringIO import StringIO
import re

orig = 'byteofpython_120.txt'
rxpart = re.compile(r'Chapter (\d+)\. .*')

assert path.exists(orig)

outfile = StringIO()
infile = open(orig)

try:
    for line in infile:
        m = rxpart.match(line)
        if m:
            n, = m.groups()
            fname = '%s.rst' % n
            print fname
            outfile.close()
            outfile = open(fname, 'w')
        outfile.write(line)
finally:
    infile.close()
    outfile.close()




