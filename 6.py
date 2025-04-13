N = int(input())
count = 0
words = set()
duplicates = set()
for _ in range(N):
    word = input()
    if word not in words:
        words.add(word)
    elif word in duplicates:
        count += 1
    else:
        duplicates.add(word)
        count += 2
print(count)
