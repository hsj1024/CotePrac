# 1. 구구단 2~9단까지 출력 (1)

for i in range(2, 10):
    print(f"   {i}단")
    for j in range(1, 10):
        print(f"{i} x {j} = {i * j}")


# 1. 구구단 2~9단까지 출력 (2)
# 리스트 컴프리헨션 사용

[print(f"{i}단\n{''.join([f'{i} x {j} = {i * j}  ' for j in range(1, 10)])}\n")for i in range(2, 10)]
