def solution(quiz):
    answer = []
    a = 0
    # ["3 - 4 = -3", "5 + 6 = 11"]	["X", "O"]
    for i in quiz:
        s = i.split()
        if s[1] == "-":
            if (int(s[0]) - int(s[2])) == int(s[len(s)-1]):
                answer.append("O")
            else:
                answer.append("X")
        if s[1] == "+":
            if (int(s[0]) + int(s[2])) == int(s[len(s)-1]):
                answer.append("O")
            else:
                answer.append("X")
solution(["3 - 4 = -3", "5 + 6 = 11"])