def process_player_record(player_id):
    try:
        print(get_player_record(player_id))
    except IndexError:
        print("index is too high")
    except Exception as e:
        print(e)
    return



# Don't edit below this line


def get_player_record(player_id):
    if player_id < 0:
        raise Exception("negative ids not allowed")
    players = [
        {"name": "Slayer", "level": 128},
        {"name": "Dorgoth", "level": 300},
        {"name": "Saruman", "level": 4000},
    ]
    return players[player_id]

process_player_record(2)
process_player_record(-1)
process_player_record(6)
