import sys
import math

def main():
    args = sys.argv
    filename = args[1]
    n = args[2]
    list = []
    max_len = 0
    base = 0

    with open(filename) as f:
        for i, line in enumerate(f):
            list.append(line)
            max_len += 1

    base = max_len / int(n) 
    base = math.ceil(base)
    for i, text in enumerate(list):
        if i % int(base) == 0:
            print("\n")
        print(text, end="")

if __name__ == "__main__":
    main()
