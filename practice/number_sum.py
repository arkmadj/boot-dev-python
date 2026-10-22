def number_sum(n: int) -> int:
    result: int = 0
    for i in range(1, n+1):
        result += i
    return result

print(number_sum(5))
