import utils.handlers as handler
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
            print(handler.add_contact(args, contacts))
        elif command == "change":
            print(handler.change_contact(args, contacts))
        elif command == "change-name":
            result = handler.change_name(args, contacts)
            if type(result) != AddressBook:
                print(result)
            else:
                contacts = result
                print(f"Contact {args[0]} updated. New contact name: {args[1]}.")
        elif command == "phone":
            print(handler.show_phone(args, contacts))
        elif command == "all":
            print(handler.show_all(args, contacts))
        elif command == "add-birthday":
            print(handler.add_birthday(args, contacts))
        elif command == "change-birthday":
            print(handler.change_birthday(args, contacts))
        elif command == "show-birthday":
            print(handler.show_birthday(args, contacts))
        elif command == "birthdays":
            print(handler.birthdays(args, contacts))
        elif command == "add-email":
            print(handler.add_email(args, contacts))
        elif command == "change-email":
            print(handler.change_email(args, contacts))
        elif command == "search":
            print(handler.search(args, contacts))
        elif command == "delete":
            result = handler.delete_record(args, contacts)
            if type(result) != AddressBook:
                print(result)
            else:
                contacts = result
                print(f"Contact {args[0]} was deleted.")
        elif command == "add-note":
            print(handler.add_note(args, notes))
        elif command == "note-ls":
            print(str(notes))
        elif command == "edit-note-title":
            print(handler.edit_note_title(args, notes))
        elif command == "edit-note-text":
            print(handler.edit_note_text(args, notes))
        elif command == "add-tag-to-note":
            print(handler.add_tag_to_note(args, notes))
        elif command == "remove-tag-from-note":
            print(handler.remove_tag_from_note(args, notes))
        elif command == "find-notes-by-title":
            print(handler.find_notes_by_title(args, notes))
        elif command == "find-notes-by-tags":
            print(handler.find_notes_by_tags(args, notes))
        elif command == "sort-by-tag":
            print(handler.sort_by_tag(args, notes))
        elif command == "remove-note-by-title":
            print(handler.remove_note_by_title(args, notes))
        elif command == "change-email":
            print(handler.change_email(args, contacts))
        elif command == "help":
            print(handler.help_info(args))
        elif command == "add-address":
            print(handler.add_address(args, contacts))
        elif command == "del-address":
            print(handler.del_address(args, contacts))
        elif command == "change-address":
            print(handler.change_address(args, contacts))
        elif command == "save":
            notes.save()
            contacts.save()
            print("-- Data Saved --")
        else:
            print("Invalid command. Use 'help' to see list of the exist commands ")
