# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return

#from math import sqrt  #sqrt : 루트 / import해서 가져와서 쓸 수 있음. sqrt(n)

def solution(n):
    answer = 0

    for num in range(1,int(n ** 0.5) + 1 ): #1 ~ n의 루트까지의 범위 / 루트 = n ** 0.5
        if n % num == 0:
            answer += 2        # ex) (1,20) (20,1)

            if num * num == n:
                answer -= 1 # n이 100인 경우 (10,10) 중복되는 경우가 있기에 -1 해줌.

    return answer

print(solution(20))
print(solution(100))