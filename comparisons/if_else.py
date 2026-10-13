def player_status(health):
    if health == 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"


print(player_status(0))
print(player_status(3))
print(player_status(12))
