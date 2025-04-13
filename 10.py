operations = {"read": "R", "write": "W", "execute": "X"}
files = {}
N = int(input())
for _ in range(N):
    s = input().split(" ")
    files[s[0]] = s[1::]
M = int(input())
output = []
for _ in range(M):
    s = input().split(" ")
    if (operations[s[0]]) in files[s[1]]:
        output.append("OK")
    else:
        output.append("Access denied")
print(*output, sep="\n")
