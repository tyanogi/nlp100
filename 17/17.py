import sys

filename = sys.argv[1]

with open(filename) as f:
    print(set([line.split("\t")[0] for line in f]))

