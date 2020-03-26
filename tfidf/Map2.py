#!/usr/bin/env python
# Revised by Parke Godfrey, then by Yunge Hao
# 2017-09-11, 2019-12-18

import sys
import re
import os

# input comes from STDIN (standard input)
doc = os.environ['mapreduce_map_input_file']
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = filter(None, re.split('[\W+_]', line))
    # words = re.sub('[^a-zA-Z0-9]+', '', words.lower())
    # write out word paired with count of 1
    for word in words:
        # write the results to STDOUT (standard output);
        # tab-delimited; the trivial word count is 1
        print('%s,%s\t%s' % (word.lower(), doc, 1))
