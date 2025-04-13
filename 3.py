numbers1 = set(input().split())
numbers2 = set(input().split())
print(*sorted((numbers1 & numbers2)))
