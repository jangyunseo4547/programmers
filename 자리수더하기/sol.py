# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 
# solution 함수를 완성해주세요

def solution(n):
    str_n = str(n) # 각자리 수를 더해야 하므로 문자형으로  / (list tuple range string)만 시퀀스 형태
    answer = 0
    
    for i in str_n:
        answer += int(i) # answer + i 
    return answer

print(solution(1234))
print(solution(930211))


