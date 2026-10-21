def get_champion_slices(champions):
    return champions[2:], champions[:-1], champions[::2]
    pass

champs = ["Saka", "Odegaard", "Cala", "Gabriel", "Rice", "White", "Timber", "Bruno G."]
print(get_champion_slices(champs))
