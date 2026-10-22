def find_min(nums: list[int]) -> int | float:
    result: float = float("inf")
    for num in nums:
        if num <= result:
            result = num
    return result


print(find_min([1, 3, -1, 2]))
print(find_min([18, 3, 7, 2]))
