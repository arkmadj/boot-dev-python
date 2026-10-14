def calculate_experience_points(level):
    xp = 0
    if level == 1:
        return xp
    for i in range(1, level):
        xp += i * 5
    return xp

for i in range(1, 10):
    print(f"Experience {i} points: {calculate_experience_points(i)}")
