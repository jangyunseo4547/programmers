# 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 
# 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return


def solution(n):
    answer = 0

    for num in range(1,n+1): #1 ~ n까지의 범위
        if n % num == 0: # n의 약수 = num으로 나누어떨어지는 
            answer += 1
            
    return answer

print(solution(20))
print(solution(100))