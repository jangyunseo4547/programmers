# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return

# list comprehention으로 표현
# return 일때는 앞에다 붙여주기

def solution(my_string):
    answer = ''.join([i for i in my_string if i not in 'aeiou']) # 자음일 경우 출력
    return answer
    
print(solution("bus"))
print(solution("nice to meet you"))

