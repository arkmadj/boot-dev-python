def merge(dict1, dict2):
    merged_dict = {}
    for item in dict1:
        merged_dict[item] = dict1[item]

    for item in dict2:
        merged_dict[item] = dict2[item]
    return merged_dict

two_towers = {"Frodo": 56, "Aragorn": 10}
rotk = {"Aragorn": 100, "Gandalf": 809}
merged_dict = merge(two_towers, rotk)
print(merged_dict)
