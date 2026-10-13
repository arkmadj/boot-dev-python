def can_withstand_blow(hero_armor, enemy_damage):
    return hero_armor >= enemy_damage


print(can_withstand_blow(100, 1000))
