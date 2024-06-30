from collections import Counter

def solution(array):
    counter = Counter(array)
    mode_values = counter.most_common(2)  # 최빈값 2개 가져오기
    
    # 최빈값이 없는 경우 -1 반환
    if len(mode_values) == 0:
        return -1
    
    # 최빈값이 1개인 경우
    elif len(mode_values) == 1:
        return mode_values[0][0]
    
    # 최빈값이 2개 이상인 경우
    else:
        if mode_values[0][1] == mode_values[1][1]:  # 빈도가 같은 최빈값이 2개 이상인 경우
            return -1
        else:  # 빈도가 가장 높은 최빈값 반환
            return mode_values[0][0]
