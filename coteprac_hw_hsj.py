# 1. 구구단 2~9단까지 출력 (1)

for i in range(2, 10):
    print(f"   {i}단")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")


# 1. 구구단 2~9단까지 출력 (2)
# 리스트 컴프리헨션 사용

[print(f"{i}단\n{'\n'.join([f'{i} x {j} = {i * j}' for j in range(1, 10)])}\n") for i in range(2, 10)]

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

# 3-1. 정삼각형 (1)
def print_triangle1(height):
    for i in range(height):
        print(" " * (height - i - 1) + "*" * (2 * i + 1))

print_triangle1(5)

# 3-1. 정삼각형 (2)

def print_triangle2(height):
    for i in range(1, height + 1):
        print(" " * (height - i) + "*" * (2 * i - 1))

print_triangle2(5)

# 3-2. 직각삼각형 (1)
def right_triangle1(height):
    for i in range(height):
        print("*" * (2 * i + 1) + " " * (height - i - 1))

right_triangle1(5)

# # 3-2. 직각삼각형 (2)

def right_triangle2(height):
    for i in range(height):
        print("*" * (i + 1))

right_triangle2(5)

# 3-3. 마름모 (1)

def print_diamond1(height):
    
    # 윗 부분
    for i in range(1, height // 2 + 2):
        print(" " * (height // 2 + 1 - i) + "*" * (2 * i - 1))
    # 아랫 부분
    for i in range(height // 2, 0, -1):
        print(" " * (height // 2 + 1 - i) + "*" * (2 * i - 1))

print_diamond1(7)

# 3-3. 마름모 (2)

def print_diamond2(height):
    for i in range(1, height // 2 + 2):
        print(" " * (height // 2 + 1 - i) + "*" * (2 * i - 1))
    for i in range(height // 2, 0, -1):
        print(" " * (height // 2 - i + 1) + "*" * (2 * i - 1))

print_diamond2(7)

