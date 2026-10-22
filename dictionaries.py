def get_character_record(name, server, level, rank):
    return {"name": name, "server": server, "level": level, "rank": rank, "id": f"{name}#{server}"}


print(get_character_record("Baba", "Dudu", 140, 7))
