words = {}
text = "hey hi hi      hi\nhey lol xdd\nxdd       lol".split("\n")
for i in text:
    for j in i.split():
        words[j] = words.get(j, 0) + 1
for i in words:
    print(i, words[i])
