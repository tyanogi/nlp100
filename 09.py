import random

def main():
    text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    res_text = typoglycemia(text)
    print(res_text)

def typoglycemia(text):
    res_text = []

    for word in text.split(" "):
        if len(word) <= 4: res_text.append(word)
        else:
            mid_list = list(word[1:-1])
            while mid_list == list(word[1:-1]):
                random.shuffle(mid_list)
            res_text.append(''.join(word[0]) + ''.join(mid_list) + ''.join(word[-1]))

    return ' '.join(res_text)

if __name__ == "__main__":
    main()

