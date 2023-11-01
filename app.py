import utils.handlers as handler
from models.adressbook import AddressBook
from utils.input_parser import parse_input
from utils.get_welcome_message import get_welcome_message
from utils.get_help_commands import get_help_commands


def app():
    print(get_welcome_message())
    print(get_help_commands())

    contacts = AddressBook()

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            contacts.save()
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(handler.add_contact(args, contacts))
        elif command == "change":
            print(handler.change_contact(args, contacts))
        elif command == "phone":
            print(handler.show_phone(args, contacts))
        elif command == "all":
            print(handler.show_all(args, contacts))
        elif command == "add-birthday":
            print(handler.add_birthday(args, contacts))
        elif command == "show-birthday":
            print(handler.show_birthday(args, contacts))
        elif command == "birthdays":
            print(handler.birthdays(args, contacts))
        elif command == "add-email":
            print(handler.add_email(args, contacts))
        elif command == "change-email":
            print(handler.change_email(args, contacts))
        elif command == "search-email":
            print(handler.search_email(args, contacts))
        elif command == "help":
            print(handler.help_info(args))
        elif command == "add-address":
            print(handler.add_address(args, contacts))
        elif command == "del-address":
            print(handler.del_address(args, contacts))
        elif command == "change-address":
            print(handler.change_address(args, contacts))
        elif command == "save":
            print(contacts.save())
        else:
            print("Invalid command. Use 'help' to see list of the exist commands ")
