def get_character_record(name, server, level, rank):
    return {
        "name": name,
        "server": server,
        "level": level,
        "rank": rank,
    }

print(get_character_record("Saka", "Arsenal", 89, 10))
