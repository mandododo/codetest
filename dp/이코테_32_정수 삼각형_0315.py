n = int(input())
dp = []

## dp테이블에 저장하기
for i in range(n) :                            ## dp테이블에 저장하기
    dp.append(list(map(int,input().split())))

print(dp)
print(dp[1][0])

for i in range(1,n) :                          
    for j in range(0,i+1) :                     
        if j == 0 :
            dp[i][0] += dp[i-1][0]              ## 0열끼리 더하기
        elif j == i :
            dp[i][j] += dp[i-1][j-1]            ##마지막 열끼리 더하기
        else :
            dp[i][j] += max(dp[i-1][j-1],dp[i-1][j])    ## 두 화살표중 더 큰 경우 받아들이기

print(max(dp[n-1]))  