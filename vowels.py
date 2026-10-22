def count_vowels(text):
    vowel_set = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    total_vowels = 0
    unique_vowels = set()
    for char in text:
        if char in vowel_set:
            total_vowels += 1
            unique_vowels.add(char)
    return total_vowels, unique_vowels

print(count_vowels("Banana Soda CAN is refreshing, RIGHT?"))
