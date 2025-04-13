words = {}
N = int(input())
for _ in range(N):
    s = input().split(" ")
    words[s[0]] = s[1]
word = input()
print(words.get(word, dict(zip(words.values(), words.keys()))[word]))
