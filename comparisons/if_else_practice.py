def check_high_score(current_player_name, high_scoring_player_name):
    if high_scoring_player_name == current_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"

print(check_high_score("Ahmad", "Jinadu"));
print(check_high_score("Bruno G.", "Bruno G."))
