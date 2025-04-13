words = set()
N = int(input())
for _ in range(N):
    for i in input().split():
        words.add(i)
print(len(words))
