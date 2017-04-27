import sys

filename = sys.argv[1]

list  = [line.split("\t")[0] for line in open(filename)]
count = {word:list.count(word) for word in set(list)}

for line, f in sorted(count.items(), key=lambda x: x[1], reverse=True):
    print(line, f)

