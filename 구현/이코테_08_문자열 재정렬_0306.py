lst = list(input())
alpa = []
cnt = 0
for i in lst:
    if i.isalpha():
        alpa.append(i)
    else:
        cnt += int(i)
alpa.sort()
for j in alpa:
    print(j, end="")

print(cnt) 