from handler import parse_input, add_contact, change_contact, show_phone, show_all


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            if len(args) == 2:
                print(add_contact(contacts, args[0], args[1]))
            else:
                print("Invalid command. Usage: add [name] [phone]")

        elif command == "change":
            if len(args) == 2:
                print(change_contact(contacts, args[0], args[1]))
            else:
                ("Invalid command. Usage: change [name] [phone]")

        elif command == "phone":
            if len(args) == 1:
                result = show_phone(contacts, args[[0]])
                print(result) if isinstance(result, str) else print(
                    f"{args[0]}: {result}"
                )
            else:
                print("Invalid command. Usage: phone [name]")

        elif command == "all":
            show_all(contacts)

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
