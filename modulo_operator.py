def get_odd_numbers(num):
    odd_numbers = []

    for i in range(0, num):
        if i % 2:
            odd_numbers.append(i)

    # don't touch below this line

    return odd_numbers

print(get_odd_numbers(10))
