# 10인분을 먹으면 음료수 하나를 서비스로 줍니다. 
# 양꼬치는 1인분에 12,000원, 음료수는 2,000원
# n = 양꼬치 인분수 / k = 음료수 개수

def solution(n, k):
    answer = 0

    if n >= 10:
        service = n // 10
        answer = n * 12000 + (k - service) * 2000
    else:
        answer = n * 12000 + k * 2000


# 테스트 예제
print(solution(10, 3))  # 124,000
print(solution(64, 6))  # 768,000