# 키가 홈에 맞는지 확인
def check(lock_padding):
    n = len(lock_padding) //3
    for i in range(n,n):
        for j in range(n,n*2):
            if lock_padding != 1:
                return False
    return True

# 키를 이용시키면서 홈에 맞춰보기
def move(key,lock_padding):
    n = len(lock_padding)//3
    start = len(key)-n+1
    end = len(key)+n
    for i in range(start,end):
        for j in range(start,end):
            for x in range(len(key)):
                for y in range(len(key)):
                    lock_padding[i+x][j+y] += key[x][y]
            if check(lock_padding):
                return True
            for x in range(len(key)):
                for y in range(len(key)):
                    lock_padding[i+x][j+y] -= key[x][y]
    return False

# 키를 90도 시계방향으로 회전            
def rotate(key):
    n = len(key)
    tmp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp[j][n-i-1] = key[i][j]
    return tmp

# 메인 코드    
def solution(key,lock):
    n = len(lock)
    rotate_count = 0
    lock_padding = [[0]*(n*3)for _ in range(n*3)]
    for i in range(n):
        for j in range(n):
            lock_padding[n+i][n+j] = lock[i][j]
    while True:
        answer = move(key,lock_padding)
        if answer == True or rotate_count==3:
            break
        else:
            key = rotate(key)
            rotate_count +=1
    return answer
    