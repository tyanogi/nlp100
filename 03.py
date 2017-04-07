text = u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
length = []

text = text.replace(u",", u"")
text = text.replace(u".", u"")
words = text.split(" ")

for w in words:
    length.append(len(w))

print(length)

