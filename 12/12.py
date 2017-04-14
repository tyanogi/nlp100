import sys

def main():
    filename = sys.argv[1]

    with open(filename) as f, open("col1.txt", "w") as fc1, open("col2.txt", "w") as fc2:
        for line in f:
            rline = line.replace('\t', ' ')
            words = rline.split(" ")
            print(words[0], end="")
            #fc1.write('\n'.join(words[0]))
            fc1.write(words[0])
            fc1.write("\n")
            print(words[1])
            #fc2.write('\n'.join(words[1]))
            fc2.write(words[1])
            fc2.write("\n")

if __name__ == '__main__':
    main()

