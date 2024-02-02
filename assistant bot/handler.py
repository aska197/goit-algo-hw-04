def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(contacts, name, phone):
    if name in contacts:
        return "Contact with this name already exists. Use 'change' command to update the phone number."
    contacts[name] = phone
    return "Contact added."


def change_contact(contacts, name, phone):
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(contacts, name):
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")
