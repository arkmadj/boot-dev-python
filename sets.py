def remove_duplicates(spells):
    spells_set = set()
    for spell in spells:
        spells_set.add(spell)
    return spells_set

fruits = ["apple", "banana", "apple"]
print(remove_duplicates(fruits))
    
