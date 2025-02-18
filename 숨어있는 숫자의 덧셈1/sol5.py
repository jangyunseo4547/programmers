# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return

def solution(my_string):
    answer = 0

    for char in my_string:
        try:
            answer += int(char)

        except:
            continue
        
    return answer

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))