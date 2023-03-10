n = int(input())
score = []
for _ in range(n):
    name,kor,eng,math = map(str,input().split())
    score.append([name,int(kor),int(eng),int(math)])
    
score_list = sorted(score,key = lambda x : (-x[1], x[2],-x[3],x[0]))

for sc in score_list:
    print(sc[0])