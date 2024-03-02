def pad(item, length, char=" "):
    if len(item) >= length:
        return item[:length]
    return item + (char * (length - len(item)))

def menu(*args, title="Menu:", prompt="Your choice > ", field_len=50, error="Unrecognized choice!"):
    print(title)
    print("-"*(field_len+7))
    for index, item in enumerate(args):
        tab = "\t"
        print(f"| {index} | {pad(item, field_len)}|")
        print("-"*(field_len+7))
    while True:
        choice = input(prompt)
        try:
            choice = int(choice)
            return (choice, args[choice])
        except (ValueError, IndexError):
            print(error)

print(menu("apples", "oranges", "bananas", "some other fruit with a really, really, really, really long name"))
