def solution(N, stages):
    ls = []
    answer = []
    for i in range(1, N+1):
        fail_stage = 0 # 실패한 스테이지
        pass_stage = 0 # 통과한 스테이지
        
        for j in stages:
                 
            if i == j:
                fail_stage += 1

            if j >= i:
                pass_stage += 1

        if pass_stage == 0:
            ls.append([i, 0])
        else :
            ls.append([i, fail_stage / pass_stage])
        ls.sort(key = lambda ls : ls[1], reverse=True)
    for i in range(len(ls)):
        answer.append(ls[i][0])
    return answer 