import sys

def main():
    filename = sys.argv[1]

    with open(filename) as f:
        for line in f:
            rline = line.replace('\t', ' ')
            print(rline, end='')

if __name__ == '__main__':
    main()
