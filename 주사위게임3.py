from collections import Counter

def solution(a, b, c, d):
    # 네 주사위의 숫자를 리스트로 저장
    dice = [a, b, c, d]
    
    # 네 주사위의 숫자를 정렬하여 최소값과 중복된 숫자의 개수를 구함
    set_dice = list(set(dice))
    answer = []
    # 모든 주사위의 숫자가 같은 경우
    if len(set_dice) == 1:
        return 1111 * set_dice[0]
    
    # 세 주사위의 숫자가 같은 경우
    elif len(set_dice) == 2:
        for element in dice:
            if dice.count(element) == 3:
                p = element
                q = [x for x in set_dice if x!= p][0]
                return (10*p + q) ** 2  
            elif dice.count(element) == 2:
                p = element
                q = [x for x in set_dice if x != p][0] # x가 p와 같지 않은 경우에만 set_dice 안의 x를 가져와 리스트를 만든 것의 첫번 째 요소선택
                return (p + q)*(abs(p-q))
    elif len(set_dice) == 3:
        for element in dice:
            if dice.count(element) == 2:
                new_list = [x for x in set_dice if x != element]
                return new_list[0]*new_list[1]
    else:  
        return min(dice)
print(solution(4,1,4,4))