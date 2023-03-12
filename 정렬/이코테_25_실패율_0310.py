def solution(N, stages):
    k=len(stages)
    s=[]
    for i in range(1,N+1):    # 스테이지 설정
        c=0
        for j in range(len(stages)):    # 그 스테이지의 실패한 인원 카운트
            if stages[j] == i:
                c += 1
        if c == 0:
            s.append(0)
        else:
            s.append(c/k)       # s에 구한 확률 넣기
        k = k- c

    a=sorted(s,reverse=True)
    answer=[]

    for i in range(len(a)):
        answer.append(s.index(a[i])+1)
        s[s.index(a[i])]=2

    return answer