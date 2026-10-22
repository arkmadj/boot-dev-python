def get_most_common_enemy(enemies_dict={}):
    max_enemy = ""
    max_so_far = float("-inf")
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_enemy = enemy

    return None if not enemies_dict else max_enemy

enemies = {"jackal": 3, "kobold": 2, "soldier": 3, "gremlin": 5}
print(get_most_common_enemy(enemies))
