n,m = map(int,input().split())
lst = list(map(int,input().split()))

count = 0
for i in range(len(lst)):
    tmp = 1
    while i+tmp <len(lst):
        if lst[i] != lst[i+tmp]:
            count +=1
        tmp +=1
print(count)