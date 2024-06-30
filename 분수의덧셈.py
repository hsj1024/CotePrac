# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     if denom1 == denom2:
#         answer.append(numer1+numer2)
#         answer.append(denom1)
#     else:
#         numer1*=(denom1*denom2)
#         numer2*=(denom1*denom2)
#         denom1*=(denom1*denom2)
#         denom2*=(denom1*denom2)
#         answer.append(numer1+numer2)
#         answer.append(denom1)
#         print(answer)
#     return answer


import math
def solution(numer1, denom1, numer2, denom2):
    num = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(num, denom)
    #print(num,denom,gcd)
    #print([num // gcd, denom//gcd]) 
    print([num, denom])
    return [num, denom]

solution(1,2,3,4)