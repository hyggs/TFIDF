#!/usr/bin/env python
# Revised by Parke Godfrey, then by Yunge Hao
# 2017-09-11, 2019-12-18

import sys

currWord = None
word = None
currDoc  = None
currCount = 0
doc      = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    word, doc_count = line.split('\t', 1)
    doc, count = doc_count.split(',')

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    # this only works if the INPUT is sorted by key!
    if currWord == word:
        if currDoc:
            if currDoc != doc:
                currCount += count
        currDoc = doc
    else:
        if currWord:
            # write result to STDOUT
            print('%s\t%s' % (currWord, currCount))
        currCount = count
        currWord  = word
        currDoc = doc

# do not forget to output the last word if needed!
if currWord == word:
    print('%s\t%s' % (currWord, currCount))

