n = input()
lst = list(map(int,input().split()))
lst.sort()

cnt = 1
for i in lst:
    if cnt < i:
        break
    cnt += i

print(cnt)