def main():
    with open("ouptput.txt", "w") as f, open("col1.txt") as fc1, open("col2.txt") as fc2:
        for line1, line2 in zip(fc1, fc2):
            rline1 = line1.replace("\n", "")
            f.write(rline1)
            f.write("\t")
            f.write(line2)

if __name__ == "__main__":
    main()

