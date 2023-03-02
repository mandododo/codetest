a = input().split('-')
print(a)
num = []
for i in a:
    cnt = 0
    j = i.split('+')
    for k in j:
        cnt += int(k)
    num.append(cnt)
n= num[0]
for m in range(1,len(num)):
    n -= num[m]
print(n)