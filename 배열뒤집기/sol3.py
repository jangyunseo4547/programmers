# 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다. 
# num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수


def solution(num_list):
    result = []

    for num in num_list:
        result.insert(0,num)

    # 슬라이싱 활용 return numlist[ : :-1]

    return num_list

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))