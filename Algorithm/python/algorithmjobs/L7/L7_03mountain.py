'''
수열 분석 시 1개 씩, 2개씩 3개씩 등등 혹은 짝홀이 기본
1213121412131215121312141213121

12
13
12
14
12
13
12
15
12
13
12
14
12
13
12
1

1213
1214
1213
1215
1213
1214
1213
121

1213121412131215121312141213121
=
121312141213121
5
121312141213121
=
(5
4 4
33 33
2222 2222
11111 11111)*2쯤
=
1213121;3일때 출력값
4
1213121
5
1213121
4
1213121
=>
DP로 풀자


팰린드롬

아이디어;중위순회
트리까진 필요 없이, 설명자료 저장
'''
if __name__=='__main__':
    n=int(input())

    ex_term=str()
    #cur_term=ex_term+k+ex_term

    if(n==1):
        cur_term=ex_term+str(n)+ex_term

    else:
        for i in range(n):
            cur_term=ex_term+str(i+1)+ex_term
            ex_term=cur_term
    
    print(cur_term)

