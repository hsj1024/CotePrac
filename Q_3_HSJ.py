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

# 3-2. 직각삼각형 (2)

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