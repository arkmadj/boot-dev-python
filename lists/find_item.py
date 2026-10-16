def contains_leather_scraps(items):
    found = False

    # don't touch above this line

    for item in items:
        if item == "Leather Scraps":
            found = True

    # don't touch below this line

    return found


junk = ["Leather Scraps", "Paper", "Plastic", "Iron Rod"]

fruits = ["Banana", "Orange", "Apple", "Pineapple"]

print(contains_leather_scraps(junk))
print(contains_leather_scraps(fruits))
