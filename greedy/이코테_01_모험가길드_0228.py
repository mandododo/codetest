n = input()
lst = list(map(int,input().split()))

lst.sort(reverse=True)

result = 0
tmp = []
for i in lst:
    tmp.append(i)
    if len(tmp) >= tmp[0]:
        result += 1
        tmp.clear()

print(result)