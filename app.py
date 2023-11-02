from handlers.handlers import handlers
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

        command = command.lower()

        if command in ["close", "exit"]:
            notes.save()
            contacts.save()
            print("Goodbye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add-contact":
            print(handlers["add_contact"](args, contacts))
        elif command == "edit-contact":
            print(handlers["edit_contact"](args, contacts))
        elif command == "edit-name":
            result = handlers["edit_name"](args, contacts)
            if type(result) != AddressBook:
                print(result)
            else:
                contacts = result
                print(f"Contact {args[0]} updated. New contact name: {args[1]}.")
        elif command == "show-phone":
            print(handlers["show_phone"](args, contacts))
        elif command == "show-contacts":
            print(handlers["show_all"](args, contacts))
        elif command == "add-birthday":
            print(handlers["add_birthday"](args, contacts))
        elif command == "edit-birthday":
            print(handlers["edit_birthday"](args, contacts))
        elif command == "show-birthday":
            print(handlers["show_birthday"](args, contacts))
        elif command == "birthdays":
            print(handlers["birthdays"](args, contacts))
        elif command == "add-email":
            print(handlers["add_email"](args, contacts))
        elif command == "edit-email":
            print(handlers["edit_email"](args, contacts))
        elif command == "search":
            print(handlers["search"](args, contacts))
        elif command == "delete":
            result = handlers["delete_record"](args, contacts)
            if type(result) != AddressBook:
                print(result)
            else:
                contacts = result
                print(f"Contact {args[0]} was deleted.")
        elif command == "add-note":
            print(handlers["add_note"](args, notes))
        elif command == "show-notes":
            print(str(notes))
        elif command == "show-tags":
            print(notes.get_unique_tags())
        elif command == "edit-note-title":
            print(handlers["edit_note_title"](args, notes))
        elif command == "edit-note-text":
            print(handlers["edit_note_text"](args, notes))
        elif command == "add-tag-to-note":
            print(handlers["add_tag_to_note"](args, notes))
        elif command == "delete-tag-from-note":
            print(handlers["delete_tag_from_note"](args, notes))
        elif command == "find-notes-by-title":
            print(handlers["find_notes_by_title"](args, notes))
        elif command == "find-notes-by-tags":
            print(handlers["find_notes_by_tags"](args, notes))
        elif command == "sort-by-tag":
            print(handlers["sort_by_tag"](args, notes))
        elif command == "delete-note-by-title":
            print(handlers["delete_note_by_title"](args, notes))
        elif command == "edit-email":
            print(handlers["edit_email"](args, contacts))
        elif command == "help":
            print(handlers["help_info"](args))
        elif command == "add-address":
            print(handlers["add_address"](args, contacts))
        elif command == "delete-address":
            print(handlers["delete_address"](args, contacts))
        elif command == "edit-address":
            print(handlers["edit_address"](args, contacts))
        elif command == "save":
            notes.save()
            contacts.save()
            print("-- Data Saved --")
        else:
            print("Invalid command. Use 'help' to see list of the exist commands ")
