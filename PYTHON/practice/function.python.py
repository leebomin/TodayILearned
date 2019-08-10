def factorial(n):
    accumulator = 1
    for x in range(1, n+1):
        accumulator *= x
    return accumulator


print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))


def double(n):
    # n = parameter
    return n*2

print(double(1))
print(double(2))
print(double(3))

# 함수값에 들어가는 입력값 = argument

# 추상화 > 지도
# 많은 것들이 생략됨. 간단해짐. 자연의 복잡함을 다 담지는 못하지만 우리가 쓸만한 기능들로 이루어진 것을 만듦(디테일 제거하고 필요한 것, 핵심만 남기기).
