#!/usr/bin/python

import fileinput
import re
import io
import sys

data = []
for line in fileinput.input():
  title = str(re.search('^(.+)- Your ', line).group(1))
  loc = int(re.search('(?:[Ll]ocation|[Pp]age)\s([0-9]+)-?[0-9]*\s\|\sAdded\son\s', line).group(1))
  # print "TITLE:  " + title
  # print("LOC:    " + loc)
  # print("LINE:   " + line)
  data.append((title, loc, line))
  
for i in [x[2] for x in sorted(data, key = lambda y: (str(y[0]), int(y[1])))]:
  print(i, end='')


