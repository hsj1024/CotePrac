# [선택 문제 ] 2. 프로그래머스 문제 옹알이 (1)

def solution(babbling):
    anna = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for bb in babbling:
        for a in anna:
            bb = bb.replace(a, ' ')
        bb = bb.replace(' ', '')
        if len(bb) == 0:
            answer += 1
    return answer