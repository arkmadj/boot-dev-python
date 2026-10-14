def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions > 0:
        mana += 1
        num_potions -= 1
    return mana, num_potions

mana, potions = meditate(5, 10, 3)
print(f"The player has {mana} mana and {potions} potions left")
