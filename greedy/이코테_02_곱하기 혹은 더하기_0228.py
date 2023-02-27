n = input()
lst = list(map(int,n))

total = lst[0]

for i in range(1,len(lst)):
    if  total == 0 or lst[i] == 0:
        total += lst[i]
    else:
        total *= lst[i] 
print(total)