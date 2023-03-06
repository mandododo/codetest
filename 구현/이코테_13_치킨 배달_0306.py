from itertools import combinations
n,m = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
one_lst = []
two_lst = []
for i in range(n):
    for j in range(n):
        if lst[i][j] == 1:
            one_lst.append((i,j))
        if lst[i][j] == 2:
            two_lst.append((i,j))
candidates = list(combinations(two_lst,m))

def get_sum(candidate):
    result = 0
    for hx,hy in one_lst:
        tmp = 1e9
        for cx,cy in candidate:
            tmp = min(tmp,abs(hx-cx)+abs(hy-cy))
        result += tmp
    return result

result = 1e9

for candidate in candidates:
    result = min(result,get_sum(candidate))

print(result)