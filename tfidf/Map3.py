#!/usr/bin/env python
# Revised by Parke Godfrey, then by Yunge Hao
# 2017-09-11, 2019-12-18

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the lines
    lines = line.splitlines()
    for line in lines:
        if "," in line:
            word, doc_tf = line.split(",")
            doc, tf = doc_tf.split("\t")
            print("%s,%s\t%s" % (word, doc, tf))
        else:
            word, dw = line.split("\t")
            print("%s\t%s" % (word, dw))   
