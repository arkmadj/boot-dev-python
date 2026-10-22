def remove_nonints(nums: list[object]) -> list[int]:
    result: list[int] = []
    for num in nums:
        if type(num) is int:
            result.append(num)
    return result

print(remove_nonints(["1", 1, "3", "400", 4, 500]))
