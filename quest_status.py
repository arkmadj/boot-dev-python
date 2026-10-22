def get_quest_status(progress):
    return progress["quests"]["bridge_run"]["status"]

character = {
    "character_name": "Kaladin",
    "quests": {
        "bridge_run": {
            "status": "In Progress",
        },
        "talk_to_syl": {
            "status": "Completed",
        },
    },
}

print(get_quest_status(character))
