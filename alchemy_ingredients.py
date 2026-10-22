def check_ingredient_match(recipe, inventory):
    available_recipes = []
    percentage_available = 0.0
    for item in inventory:
        if item in recipe:
            available_recipes.append(item)

    percentage_available = (len(available_recipes) / len(recipe)) * 100

    return percentage_available, available_recipes


seasonings = ["maggie", "salt", "pepper", "garlic", "peppermint", "onions"]
foodstuff = ["garlic", "carrot", "pepper", "cinnamon"]
print(check_ingredient_match(seasonings, foodstuff))
