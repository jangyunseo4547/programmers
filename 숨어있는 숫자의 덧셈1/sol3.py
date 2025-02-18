# 문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return

def solution(my_string):
    answer = 0
    numbers = []


    for i in my_string:
        if i.isdigit(): #isdigit :문자열이 정수면 True / 실수,문자면 False로 반환하는 함수
            numbers.append(int(i))  #리스트 메소드 is ~ : ~ 인지 물어보는 함수

    return sum(answer)

print(solution('aAb1B2cC34oOp'))
print(solution('1a2b3c4d123'))