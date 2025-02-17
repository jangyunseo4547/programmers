# 문자열 my_string과 문자 letter이 매개변수로 주어집니다. 
# my_string에서 letter를 제거한 문자열을 return



def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i != letter:
            answer += i

    return answer

print(solution('abcdef','f'))
print(solution('BCBdbe','B'))