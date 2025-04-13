votes = {}
N = int(input())
for _ in range(N):
    s = input().split(" ")
    votes[s[0]] = int(votes.get(s[0], 0)) + int(s[1])
for i in sorted(votes):
    print(i, votes[i])
