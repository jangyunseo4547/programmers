# 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성

def solution(n):
    return sum(i for i in range(2, n+1, 2))

    #2부터 n+1까지,2칸씩 건너뛰기

# 테스트 예제
print(solution(10))  # 30 (2 + 4 + 6 + 8 + 10)
print(solution(4)) #6 (2 + 4)