def trim_strongholds(strongholds):
    del strongholds[2]


places = ["bedroom", "sitting room", "living room", "dining", "kitchen"]
print(f"Before delete: {places}")
trim_strongholds(places)
print(f"After delete: {places}")
