def factorial(num: int) -> int:
    result = 1
    for i in range(1, num+1):
        result *= i
    return result


print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
