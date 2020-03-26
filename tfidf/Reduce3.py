#!/usr/bin/env python
# Revised by Parke Godfrey, then by Yunge Hao
# 2017-09-11, 2019-12-18

import sys
import math

N = 20
current_dw = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    lines = line.strip()
    pairs = lines.splitlines()
    for pair in pairs:
        if "," in pair:
            word, doc_tf = line.split(",")
            doc, tf = doc_tf.split("\t")
            tf = int(tf)
            a = N / float(current_dw)
            idf = math.log(a)
            tfidf = idf * tf
            print("%s,%s\t%s" % (word, doc, tfidf))
        else:
            word, dw = line.split("\t")
            current_dw = int(dw)
