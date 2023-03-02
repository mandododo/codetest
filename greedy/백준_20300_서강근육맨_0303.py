n = input()
lst = list(map(int,input().split()))
lst.sort()
tmp = []
if int(n)%2==1:
    tmp.append(lst[-1])
    del lst[-1]   
for i in range(int(n)//2):
    tmp.append(lst[i]+lst[-(i+1)])


print(max(tmp))