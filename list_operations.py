def concatenate_favorites(favorite_weapons, favorite_armor, favorite_items):
    return favorite_weapons + favorite_armor + favorite_items


rifles = ["Vandal", "Phantom"]
pistols = ["Bandit", "Classic", "Sheriff", "Ghost"]
snipers = ["Operator", "Marshal"]

print(concatenate_favorites(rifles, pistols, snipers))
