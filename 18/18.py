import sys

filename = sys.argv[1]
list = []

with open(filename) as f:
    for line in f:
        list.append(line.split("\t"))

for line in sorted(list, key=lambda x: float(x[2]), reverse=True):
    print("\t".join(line), end="")

