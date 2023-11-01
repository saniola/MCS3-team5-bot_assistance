from models.adressbook import AddressBook
from utils.input_parser import parse_input
from utils.get_welcome_message import get_welcome_message
from utils.get_help_commands import get_help_commands
from utils.handlers import add_contact, change_contact, show_phone, show_all,\
    add_birthday, show_birthday, birthdays, add_email, search_email,\
    change_email, help, change_name, change_birthday
from customErrors.doubleKeyError import DoubleKeyError


def app():
    print(get_welcome_message())
    print(get_help_commands())

    contacts = AddressBook()

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "change-name":
            result = change_name(args, contacts)
            if type(result) != AddressBook:
                print(result)
            else:
                contacts = result
                print(f"Contact {args[0]} updated. New contact name: {args[1]}.")
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "change-birthday":
            print(change_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "add-email":
            print(add_email(args, contacts))
        elif command == "change-email":
            print(change_email(args, contacts))
        elif command == "search-email":
            print(search_email(args, contacts))
        elif command == "help":
            print(help(args))
        else:
            print("Invalid command. Use 'help' to see list of the exist commands ")
