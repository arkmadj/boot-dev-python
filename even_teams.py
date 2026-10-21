def get_even_and_odd_teams(players):
    return players[::2], players[::-2]

dudes = ["Kane", "Odegaard", "Gnabry", "Saka", "Davies", "Gabriel"]
print(get_even_and_odd_teams(dudes))
