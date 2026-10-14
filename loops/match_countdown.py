def countdown_to_start():
    count = 10
    while count > 0:
        if count == 1:
            print(f"{count}...Fight!")
        else:
            print(f"{count}...")
        count -= 1


# Don't edit below this line


def test():
    print("Counting down to match start:")
    countdown_to_start()
    print("=====================================")


def main():
    test()


main()
