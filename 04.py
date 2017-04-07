text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
onechar = [1, 5, 6, 7, 8, 9, 15, 16, 19]
dict = {}

text = text.replace(u",", u"")
text = text.replace(u".", u"")
words = text.split(" ")

for i,  word in enumerate(words):
    #mydict[word[:1]] = i+1 if i in onechar else i+1
    if i+1 in onechar:
        dict[word[:1]] = i+1
    else:
        dict[word[:2]] = i+1

print(dict)

