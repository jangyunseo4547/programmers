# 정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 return하도록 
# solution 함수를 완성해주세요

def solution(n):
    return sum(map(int,list(str(n)))) # => map(int,['1','2','3','4']) -> [1,2,3,4] 

print(solution(1234))
print(solution(930211))