def solution(numbers):
    sum = 0 
    for i in numbers:
        sum += i 
    answer = sum / len(numbers)
    return answer

# 테스트 예제
print(solution([1,2,3,4,5,6,7,8,9,10])) 
print(solution([89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]))  