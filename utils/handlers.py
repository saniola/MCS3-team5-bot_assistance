from customErrors.doubleKeyError import DoubleKeyError
from customErrors.notFoundError import NotFoundError
from customErrors.valueLengthError import ValueLengthError
from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.notes import Notes
from models.record import Record
from utils.get_help_commands import get_help_commands
from utils.search_digits import search_by_digits
from utils.search_letters import search_by_letters


@input_error
def add_contact(args, contacts: AddressBook):
    name, phone = args

    if name in contacts:
        record: Record = contacts[name]
        if not record.find_phone(phone):
            record.add_phone(phone)
        else:
            raise DoubleKeyError(record, name)
    else:
        record: Record = Record(name)
        record.add_phone(phone)
        contacts.add_record(record)

    return f"Contact {name} with phone number {phone} added."

@input_error
def change_contact(args, contacts: AddressBook):
    name, old_phone, new_phone = args

    if name in contacts:
        record: Record = contacts[name]

        record.edit_phone(old_phone, new_phone)
        return f"Contact {name} updated. New phone number: {new_phone}."
    else:
        raise KeyError
    
@input_error
def change_name(args, contacts: AddressBook):
    name, new_name = args
    if  len(args) != 2:
        raise ValueError
    
    if new_name in contacts:
        record: Record = contacts[new_name]
        raise DoubleKeyError(record, new_name)

    temp_contacts = AddressBook()
    if name in contacts:
        for key in contacts.keys():
            record: Record = contacts[key]
            if record.name.value == name:
                record.change_name(new_name)
            temp_contacts.add_record(record)
        return temp_contacts
    else:
        raise KeyError

@input_error
def show_phone(args, contacts: AddressBook):
    if  len(args) != 1:
        raise ValueError
    name = args[0]

    if name in contacts:
        record: Record = contacts[name]
        phone_numbers = [phone.value for phone in record.phones]
        return f"Phone numbers for {name}: {', '.join(phone_numbers)}."
    else:
        raise KeyError

@input_error
def show_all(args, contacts: AddressBook):
    if len(args) > 0:
        raise ValueError

    if not contacts:
        raise KeyError

    if len(contacts) > 0:
        result = "All saved contacts with phone numbers:\n"

        for record in contacts.values():
            result += str(record)+'\n'
        return result.strip('\n')

@input_error
def add_birthday(args, contacts: AddressBook):
    name, birthday = args

    if name in contacts:
        record = contacts[name]
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        raise KeyError

@input_error
def show_birthday(args, contacts: AddressBook):
    if  len(args) != 1:
        raise ValueError
    name = args[0]

    if name in contacts:
        record = contacts[name]
        return record.show_birthday()
    else:
        raise KeyError
    
@input_error
def change_birthday(args, contacts: AddressBook):
    if  len(args) != 2:
        raise ValueError
    name, birthday = args

    if name in contacts:
        record = contacts[name]
        record.add_birthday(birthday)
        return f"Birthday changed for {name}."
    else:
        raise KeyError

@input_error
def birthdays(args, contacts: AddressBook):
    if len(args) > 0:
        raise ValueError

    return contacts.get_birthdays_per_week()

@input_error
def add_email(args, contacts: AddressBook):
    if len(args) != 2:
        raise ValueError
    name, email = args

    if name in contacts:
        record = contacts[name]
        record.add_email(email)
        return f"Email added for {name}."
    else:
        raise KeyError
    
@input_error
def change_email(args, contacts: AddressBook):
    if len(args) != 2:
        raise ValueError
    
    name, new_email = args

    if name in contacts:
        record: Record = contacts[name]
        record.add_email(new_email)
        return f"Contact {name} updated. New email: {new_email}."
    else:
        raise KeyError

@input_error
def search_email(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError
    
    search_string = args[0].lower()
    if len(search_string) < 2:
        raise ValueLengthError
    
    result = ''
    for name, record in contacts.items():
        umail = str(record.email).lower()
        if umail.find(search_string) != -1:
            phone_numbers = [phone.value for phone in record.phones]
            result += f"{name}: {', '.join(phone_numbers)} email: {record.email}\n"
    if result != '':
        return result.removesuffix('\n')
    else:
        raise NotFoundError('email')

@input_error
def search(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError
    
    search_string = args[0].lower()
    if len(search_string) < 2:
        raise ValueLengthError
    
    result = ''
    if search_string.isdigit():
       result = search_by_digits(search_string, contacts)
    else:
        result = search_by_letters(search_string, contacts)

    if result != '':
        return result.removesuffix('\n')
    else:
        raise NotFoundError()

@input_error
def help_info(args):
    if len(args) > 0:
        raise ValueError

    return get_help_commands()

@input_error
def add_note(args, notes: AddressBook):
    title, text, *tags = args
    title = title.title()
    notes.add_note(title, text, tags)
    return f"Note '{title}' added."

@input_error
def edit_note_title(args, notes: Notes):
    old_title, new_title = args
    old_title = old_title.title()
    new_title = new_title.title()
    notes.edit_note_title(old_title, new_title)
    return f"Note '{old_title}' title updated to '{new_title}'."

@input_error
def edit_note_text(args, notes: Notes):
    title, new_text = args
    title = title.title()
    notes.edit_note_text(title, new_text)
    return f"Note '{title}' text updated."

@input_error
def add_tag_to_note(args, notes: Notes):
    title, tag = args
    title = title.title()
    notes.add_tag_to_note(title, tag)
    return f"Tag '{tag}' added to note '{title}'."

@input_error
def remove_tag_from_note(args, notes: Notes):
    title, tag = args
    title = title.title()
    notes.remove_tag_from_note(title, tag)
    return f"Tag '{tag}' removed from note '{title}'."

@input_error
def find_notes_by_title(args, notes: Notes):
    title = args[0]
    title = title.title()
    matching_notes = notes.find_notes_by_title(title)

    if matching_notes:
        result = "Matching notes:\n"
        for note in matching_notes:
            result += str(note) + "\n"
        return result
    else:
        return f"No notes found with title '{title}'."

@input_error
def find_notes_by_tags(args, notes: Notes):
    tags = args
    matching_notes = notes.find_notes_by_tags(tags)

    if matching_notes:
        result = "Matching notes:\n"
        for note in matching_notes:
            result += str(note) + "\n"
        return result
    else:
        return f"No notes found with tags: {', '.join(tags)}."

@input_error
def sort_by_tag(args, notes: Notes):
    tag = args[0]
    matching_notes = notes.sort_notes_by_tag(tag)
    if matching_notes:
        print("Notes sorted by tag:")
        for note in matching_notes:
            print(str(note))

@input_error
def remove_note_by_title(args, notes: Notes):
    title = args[0]
    if notes.remove_note_by_title(title):
        print(f"Note '{title}' removed.")
    else:
        print(f"Note '{title}' not found.")

@input_error
def add_address(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError("add-address")
    name = args[0]
    if name in contacts:
        record = contacts[name]
        while True:
            city = input("Enter a city or leave it blank to stop: ")
            if not city:
                break
            try:
                adr = record.add_address(city)
            except TypeError as e:
                print(f"Error: {e}")
                continue
            if adr:
                street = input("Enter a street or leave it blank to stop: ")
                if not street:
                    break
                adr.set_street(street)
                house = input("Enter a house number or leave it blank to stop: ")
                if not house:
                    break
                adr.set_house(house)
                appartment = input("Enter appartment or leave it blank to stop: ")
                if not appartment:
                    break
                adr.set_appartment(appartment)

        return f"Address added for {name}."
    else:
        raise KeyError


@input_error
def del_address(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError("del-address")
    name = args[0]
    if name in contacts:
        record = contacts[name]
        record.del_address()
        return f"Address deleted for {name}."
    else:
        raise KeyError


@input_error
def change_address(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError("change-address")
    del_address(args, contacts)
    add_address(args, contacts)

    return f"Address changed for {args[0]}."