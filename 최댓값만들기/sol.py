# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수


def solution(numbers):
    numbers.sort(reverse = True) # .sort = 정렬 / reverse = True 내림차순

    # 음수 두 개의 곱이 양수로 변하면서 가장 큰 곱이 될 가능성까지 고려
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2]) 


print(solution([1, 2, 3, 4, 5])) # => 5 * 4
print(solution([0, 31, 24, 10, 1, 9])) # => 31 * 24