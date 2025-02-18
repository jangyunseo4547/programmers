# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 
# solution 함수를 완성해주세요

def solution(n):
    
    while n > 0: #0보다 클때까지 계속 나눔 
        a,b = divmod(n,10) # divmod(몫, 나머지)

        answer += b

        n = a

    return answer

print(solution(1234))
print(solution(930211))