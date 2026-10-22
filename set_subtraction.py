def find_missing_ids(first_ids, second_ids):
    return set(first_ids) - set(second_ids)

users = ["saka", "rice", "white", "odegaard", "timber", "merino"]
players = ["timber", "saka", "bruno", "eze"]
print(find_missing_ids(users, players))
