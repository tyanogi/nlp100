def main():
    text1 = "paraparaparadise"
    text2 = "paragraph"

    X = set(ngram(2, text1))
    Y = set(ngram(2, text2))
    print('X    :', X)
    print('Y    :', Y)
    print('And  :', X.intersection(Y))
    print('Or   :', X.union(Y))
    print('Diff :', X.difference(Y))
    print("se in X :", "se" in X)
    print("se in Y :", "se" in Y)

def ngram(n, text):
    list = []
    for i, char in enumerate(text):
        if i == len(text)-1:
            break
        list.append(text[i:n+i])
    
    return list

if __name__ == '__main__':
    main()

