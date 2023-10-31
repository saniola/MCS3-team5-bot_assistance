from models.adressbook import AddressBook
from utils.input_parser import parse_input
from utils.handlers import add_contact, change_contact, show_phone, show_all,\
    add_birthday, show_birthday, birthdays, add_email, add_address

def app():
    contacts = AddressBook()

    print("Welcome to the assistant bot!")

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
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        elif command == "add-birthday":
            print(add_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "add-email":
            print(add_email(args, contacts))
        elif command == "add-address":
            print(add_address(args, contacts))
        else:
            print("Invalid command.")
