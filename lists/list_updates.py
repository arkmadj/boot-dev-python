def smelt_ore(inventory):
    if inventory[1] == "screwdriver":
        inventory[1] = "wrench"

    return inventory

tools = ["hammer", "screwdriver", "spanner", "drill"]

print(f"Before: {tools}")

print(f"After: {smelt_ore(tools)}")
