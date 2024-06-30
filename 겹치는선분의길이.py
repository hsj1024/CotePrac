def solution(lst):
    # 빈도를 저장할 딕셔너리 생성
    frequency = {}
    
    # 리스트 요소의 빈도를 계산하여 딕셔너리에 저장
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # 최빈값을 저장할 변수 초기화
    max_count = 0
    mode_value = -1
    
    # 딕셔너리를 순회하면서 최빈값을 찾음
    for key, value in frequency.items():
        if value > max_count:
            max_count = value
            mode_value = key
        elif value == max_count:
            # 최빈값이 여러 개인 경우 -1 반환
            mode_value = -1
    
    return mode_value





solution([[0, 1], [2, 5], [3, 9]])