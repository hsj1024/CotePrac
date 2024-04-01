# [선택 문제 ] 2. 프로그래머스 문제 - 체육복


def solution(n, lost, reserve):
    # 정렬 하기
    lost.sort()
    reserve.sort()
    
    # lost, reserve 공통 요소 제거
    for i in reserve[:]:
        if i in lost:
            reserve.remove(i)
            lost.remove(i)
    # 체육복 빌려주기 
    for i in reserve:
        if i - 1 in lost:
            lost.remove(i - 1)
        elif i + 1 in lost:
            lost.remove(i + 1)
    answer = 0
    # return n - len(lost)
    print(n - len(lost))

solution(5,	[2, 4],	[1, 3, 5])