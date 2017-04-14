import sys

def main():
    filename = sys.argv[1]
    cnt = 0
    with open(filename) as f:
        for line in f: cnt += 1
        print(cnt)

if __name__ == '__main__':
    main()
