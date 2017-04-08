text = "I am an NLPer"

words = text.split(" ")
#words = text
rtext = text.replace(u" ", u"")
wgram = []
cgram = []
n = 2

for i,  word in enumerate(words):
    if i == len(words)-1: 
        break
    wgram.append(words[i:n+i])

for i, char in enumerate(rtext):
    if i == len(rtext)-1:
        break
    cgram.append(rtext[i:n+i])

print(wgram)
print(cgram)

