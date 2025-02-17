# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return

# list comprehension -> 리스트로 묶어서 표현

def solution(my_string):
    answer = sum([int(i) for i in my_string if i.isdigit()])

    return answer

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))