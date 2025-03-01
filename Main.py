# №1
# numbers = set(input().split())
# print(len(numbers))

# №2
# numbers1 = set(input().split())
# numbers2 = set(input().split())
# print(len(numbers1 & numbers2))

# №3
# numbers1 = set(input().split())
# numbers2 = set(input().split())
# print(*sorted((numbers1 & numbers2)))

# №4
# numbers = input().split()
# unique = set()
# for i in numbers:
#     if i not in unique:
#         print("NO")
#         unique.add(i)
#     else:
#         print("YES")

# №5
# words = set()
# N = int(input())
# for _ in range(N):
#     for i in input().split():
#         words.add(i)
# print(len(words))

# №6
# N = int(input())
# count = 0
# words = set()
# duplicates = set()
# for _ in range(N):
#     word = input()
#     if word not in words:
#         words.add(word)
#     elif word in duplicates:
#         count += 1
#     else:
#         duplicates.add(word)
#         count += 2
# print(count)

# №7
# words = {}
# text = "hey hi hi      hi\nhey lol xdd\nxdd       lol".split("\n")
# for i in text:
#     for j in i.split():
#         words[j] = words.get(j, 0) + 1
# for i in words:
#     print(i, words[i], sep = " ")

# №8
# words = {}
# N = int(input())
# for _ in range(N):
#     s = input().split(" ")
#     words[s[0]] = s[1]
# word = input()
# print(words.get(word, dict(zip(words.values(), words.keys()))[word]))

# №9
# votes = {}
# N = int(input())
# for _ in range(N):
#     s = input().split(" ")
#     votes[s[0]] = int(votes.get(s[0],0)) + int(s[1])
# for i in sorted(votes):
#     print(i, votes[i], sep = " ")

# №10
# operations = {"read" : "R", "write" : "W", "execute" : "X"}
# files = {}
# N = int(input())
# for _ in range(N):
#     s = input().split(" ")
#     files[s[0]] = s[1::]
# M = int(input())
# output = []
# for _ in range(M):
#     s = input().split(" ")
#     if (operations[s[0]]) in files[s[1]]:
#         output.append("OK")
#     else:
#         output.append("Access denied")
# print(*output, sep = "\n")