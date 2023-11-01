from customErrors.notFoundError import NotFoundError
from customErrors.valueLengthError import ValueLengthError
from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.record import Record
from utils.get_help_commands import get_help_commands

@input_error
def add_contact(args, contacts: AddressBook):
    name, phone = args

    if name in contacts:
        record: Record = contacts[name]
        record.add_phone(phone)
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

        for name, record in contacts.items():
            phone_numbers = [phone.value for phone in record.phones]
            result += f"{name}: {', '.join(phone_numbers)} email: {record.email}\n"
        return result

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
        record.change_email(new_email)
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
        return result
    else:
        raise NotFoundError('email')

@input_error
def help(args):
    if len(args) > 0:
        raise ValueError

    return get_help_commands()
