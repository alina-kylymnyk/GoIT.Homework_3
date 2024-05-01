
commands_list =[
    " enter 'close', 'exit' - to stop the bot",
    " enter 'hello', - to enter the command",
    " enter 'phone <name>' - to get the phone of the contact",
    " enter 'add <name> <phone number>' - to add new contact",
    " enter 'all' - to see all the contacts"
]


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            answer = input("Such name already exists. Would you like to change the name? (yes/no): ")
            if answer.lower() == "yes":
                new_name = input("Enter the new name: ")
                add_contact((new_name, phone), contacts)
                return ("Contact with new name added.")
            else:
                contacts[name] = phone
                return (f"Contact {name} is changed")
        else:
            contacts[name] = phone
            return ("Contact added.")
    except ValueError:
        print("Please write two values: name and phone")
    except Exception as e:
        print(f"An unexpected error {e} occurred ")





def show_phone(name, contacts):
    try:
        if name in contacts:
            return (f"The phone number for {name} is: {contacts[name]}")
        else:
            return (f"Error: No contact found with the name '{name}'.")
    except Exception as e:
        print(f"An unexpected error {e} occurred."
              f" Please enter 'phone <name>' to get the phone ")


def show_all(contacts):
    try:
        all_contacts = []
        for name, phone in contacts.items():
            all_contacts.append((name, phone))
        return all_contacts
    except Exception as e:
        print(f"An unexpected error {e} occurred."
              f" Please enter  'all' to get the list of all contacts ")


def main():
    try:
        contacts = {
            'Den': "092837489",
            'Steve': "2038475",
            'Bob': "84478392"
        }

        print("Welcome to the assistant bot! Write 'help' to see what I can or another command")
        while True:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in ["close".lower(), "exit".lower()]:
                print("Good bye!")
                break
            elif command == "help".lower():
                for line in commands_list:
                    print(line)
            elif command == "hello".lower():
                print("How can I help you?")
            elif command == "add".lower():
                print(add_contact(args, contacts))
            elif command == "all".lower():
                print(show_all(contacts))
            elif command == "phone":
                if args:
                    print(show_phone(args[0], contacts))
                else:
                    print("Please provide a name for the 'phone' command.")

            else:
                print("Invalid command.")

    except Exception as e:
        print(f"An unexpected error {e} occurred.")



if __name__ == "__main__":
    main()
