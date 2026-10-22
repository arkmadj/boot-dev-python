def divide_list(nums: list[int], divisor: int) -> list[float]:
    result: list[float] = []
    for num in nums:
        result.append(num/divisor)
    return result

print(divide_list([6, 8, 10], 2))
