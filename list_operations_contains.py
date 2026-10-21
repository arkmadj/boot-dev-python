def is_top_weapon(weapon):
    top_weapons = [
        "sword of justice",
        "sword of slashing",
        "stabby daggy",
        "great axe",
        "silver bow",
        "spellbook",
        "spiked knuckles",
    ]

    return weapon in top_weapons



print(is_top_weapon("Vandal"))
print(is_top_weapon("great axe"))
