def solution(num_list):
    num_list.sort(reverse = True)  #.sort : 정렬 -> reverse로 뒤집기
    return num_list

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 1, 1, 1, 1, 2]))
print(solution([1, 0, 1, 1, 1, 3, 5]))