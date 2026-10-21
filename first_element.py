def get_first_item(items):
    if len(items) > 1:
        return items[0]
    return "ERROR"


guns = ["Vandal", "Sheriff"] 
print(get_first_item(guns))
