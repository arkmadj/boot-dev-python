def join_strings(strings: list[str]) -> str:
    return ",".join(strings)

string_list: list[str] = ["Annie", "Reiner", "Bertholdt"]
joined_string: str = join_strings(string_list)
print(joined_string)
# "Annie,Reiner,Bertholdt"

string_list = ["Eren", "Mikasa", "Armin"]
joined_string = join_strings(string_list)
print(joined_string)
# "Eren,Mikasa,Armin"
