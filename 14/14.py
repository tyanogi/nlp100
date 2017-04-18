import sys

def main():
    args = sys.argv
    filename = args[1]
    n = args[2]

    with open(filename) as f:
        for i, line in enumerate(f):
            if i == int(n):
                break
            print(line)

if __name__ == "__main__":
    main()

