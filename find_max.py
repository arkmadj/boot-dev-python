def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


scores = [10, 20, 34, 50, 23, 100, 21, 43]

print(find_max(scores))
