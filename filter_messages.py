def filter_messages(messages):
    filtered_messages = []
    filtered_count = []

    for message in messages:
        words = message.split()
        filtered_words = []
        remove_count = 0
        for word in words:
            if word == "dang":
                remove_count += 1
            else:
                filtered_words.append(word)
        filtered_messages.append(" ".join(filtered_words))
        filtered_count.append(remove_count)
    return filtered_messages, filtered_count

messages = ["dang it bobby!", "look at it go", "dang dang dang"]
print(filter_messages(messages))

messages2 = [
    "That's the bloody dang Reaper of Mars...",
    "Pax au Telemanus!",
    "I was never taught how to use a dang razor!",
]
print(filter_messages(messages2))
