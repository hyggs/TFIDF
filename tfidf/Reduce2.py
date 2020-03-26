#!/usr/bin/env python
# Revised by Parke Godfrey, then by Yunge Hao
# 2017-09-11, 2019-12-18
# count the number of apperances of a word in a document

import sys
import math

currDoc = None
currWord  = None
currCount = 0
word      = None
N = 20
tf = 0
idf = 0
tfidf = 0
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    word_doc, count = line.split('\t', 1)
    word, doc = word_doc.split(',')

    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    # this only works if the INPUT is sorted by key!
    if currWord == word:
        if currDoc == doc:
            currCount += count
        else:
            if currDoc:
                print('%s,%s\t%s' % (currWord, currDoc, currCount))
            currCount = count
            currDoc = doc
    else:
        if currWord and currDoc:
            # write result to STDOUT
            print('%s,%s\t%s' % (currWord, currDoc, currCount))
        currCount = count
        currWord  = word
        currDoc = doc

# do not forget to output the last word if needed!
if currWord == word and currDoc == doc:
    print('%s,%s\t%s' % (currWord, currDoc, currCount))

