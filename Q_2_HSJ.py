# 2. 두 변수의 값을 서로 교환하기 (1)
# 산술 연산 사용

def swap(a,b):
    
    a = a + b
    b = a - b
    a = a - b
    print(a,b)

swap(3,5)


# 2. 두 변수의 값을 서로 교환하기 (2)
# XOR 사용
def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)

swap(3,4)
