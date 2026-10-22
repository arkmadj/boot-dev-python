def area_sum(rectangles: list[dict[str, int]]) -> int:
    result: int = 0
    for rectangle in rectangles:
        result += rectangle["height"] * rectangle["width"]
    return result

yards = [
    {
        "height": 5,
        "width": 6
    },
    {
        "height": 10,
        "width": 4
    },
    {
        "height": 9,
        "width": 5
    },
]
print(area_sum(yards))
