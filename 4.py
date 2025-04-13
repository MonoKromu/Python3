numbers = input().split()
unique = set()
for i in numbers:
    if i not in unique:
        print("NO")
        unique.add(i)
    else:
        print("YES")
