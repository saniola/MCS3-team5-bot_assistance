from handlers import * as
from models.adressbook import AddressBook
from models.notes import Notes
from utils.input_parser import parse_input
from utils.get_welcome_message import get_welcome_message
from utils.get_help_commands import get_help_commands

def app():
    print(get_welcome_message())
    print(get_help_commands())

    contacts = AddressBook()
    notes = Notes()

    while True:
        user_input = input("Enter a command: ")
        if user_input:
            command, args = parse_input(user_input)
        else:
            continue

        if command in ["close", "exit"]:
            notes.save()
            contacts.save()
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(edit_contact(args, contacts))
        elif command == "change-name":
            result = edit_name(args, contacts)
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
            print(edit_birthday(args, contacts))
        elif command == "show-birthday":
            print(show_birthday(args, contacts))
        elif command == "birthdays":
            print(birthdays(args, contacts))
        elif command == "add-email":
            print(add_email(args, contacts))
        elif command == "change-email":
            print(edit_email(args, contacts))
        elif command == "search-email":
            print(search_email(args, contacts))
        elif command == "search":
            print(search(args, contacts))
        elif command == "add-note":
            print(add_note(args, notes))
        elif command == "note-ls":
            print(str(notes))
        elif command == "edit-note-title":
            print(edit_note_title(args, notes))
        elif command == "edit-note-text":
            print(edit_note_text(args, notes))
        elif command == "add-tag-to-note":
            print(add_tag_to_note(args, notes))
        elif command == "remove-tag-from-note":
            print(delete_tag_from_note(args, notes))
        elif command == "find-notes-by-title":
            print(find_notes_by_title(args, notes))
        elif command == "find-notes-by-tags":
            print(find_notes_by_tags(args, notes))
        elif command == "sort-by-tag":
            print(sort_by_tag(args, notes))
        elif command == "remove-note-by-title":
            print(delete_note_by_title(args, notes))
        elif command == "change-email":
            print(edit_email(args, contacts))
        elif command == "search-email":
            print(search_email(args, contacts))
        elif command == "help":
            print(help_info(args))
        elif command == "add-address":
            print(add_address(args, contacts))
        elif command == "del-address":
            print(delete_address(args, contacts))
        elif command == "change-address":
            print(edit_address(args, contacts))
        elif command == "save":
            notes.save()
            contacts.save()
            print("-- Data Saved --")
        else:
            print("Invalid command. Use 'help' to see list of the exist commands ")
