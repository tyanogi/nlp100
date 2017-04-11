def main():
    str = "a/a#agjalFkI"
    print("plain   :", str)
    text = encrypt(str)
    print("encrypt :", text) 
    text = decrypt(text)
    print("decrypt :", text) 

def encrypt(str):
    text = ""

    chars = list(str)
    for char in chars:
        if char.islower():
            text += chr(219-ord(char))
        else:
            text += char
    return text

def decrypt(str):
    text = ""

    chars = list(str)
    for char in chars:
        if char.islower():
            text += chr(219-ord(char))
        else:
            text += char
    return text

if __name__ == '__main__':
    main()

