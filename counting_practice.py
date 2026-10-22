def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        enemies_dict[enemy_name] = enemies_dict[enemy_name] + 1 if enemy_name in enemies_dict else 1
    return enemies_dict


enemies = ["Chelsea", "Man UTD", "Man City", "Spurs", "Liverpool", "Barca", "PSG", "Chelsea", "PSG", "Spurs", "PSG", "Chelsea", "Man UTD"]
print(count_enemies(enemies))
