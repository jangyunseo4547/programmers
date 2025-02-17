# 문자열 my_string이 매개변수로 주어질 때 모음을 제거한 문자열을 return

def solution(my_string):
    answer = ''
    for i in my_string:
        if i not in 'aeiou': #자음이라면
            answer += i


    return answer

print(solution("bus"))
print(solution("nice to meet you"))