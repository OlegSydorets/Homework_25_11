#!/usr/bin/python

import sys

try:
    input_file = sys.argv[1];
    output_file = sys.argv[2]
except:
    print("Usage:", sys.argv[0], "infile outfile")
    sys.exit(1)

ifile = open(input_file, 'r')
ofile = open(output_file, 'w')

def Freq1(ifile):

  d = {}
  for x in ifile:
    d[x] = d[x] + 1 if x in d else 1
  v = max(d, key = d.get)
  return {v:d[v]}
print(Freq1(ifile))

for line in ifile:
    ofile.write(Freq1(ifile))

ifile.close();
ofile.close()