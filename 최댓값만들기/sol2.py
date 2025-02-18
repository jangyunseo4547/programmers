# 정수 배열 numbers가 매개변수로 주어집니다. 
# numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수


#버블 정렬 활용
def solution(numbers):
    n = len(numbers) #n = numbers의 원소 갯수 

    for i in range(n): # i를 0 ~ n-1까지 반복
        for j in range(0, n-i-1): # 외부 루프 반복마다 맨 끝에 하나씩 정렬된 요소가 확정되므로, 내부 루프는 그 부분을 제외하고 동작
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    
    return numbers[-1] * numbers[-2]

print(solution([1, 2, 3, 4, 5])) # => 5 * 4
print(solution([0, 31, 24, 10, 1, 9])) # => 31 * 24