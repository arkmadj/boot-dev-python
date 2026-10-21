def reverse_list(items):
    rev = []
    for i in range(len(items)-1, 0, -1):
        rev.append(items[i])
    return rev


guns = ["Vandal", "Sheriff", "Phantom", "Operator"]
print(f"List: {guns}")
print(f"Reversed List: {reverse_list(guns)}")
