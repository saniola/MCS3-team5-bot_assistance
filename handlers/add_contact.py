from customErrors.doubleKeyError import DoubleKeyError
from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.record import Record

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
