from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.record import Record

@input_error
def edit_contact(args, contacts: AddressBook):
    name, old_phone, new_phone = args

    if name in contacts:
        record: Record = contacts[name]

        record.edit_phone(old_phone, new_phone)
        return f"Contact {name} updated. New phone number: {new_phone}."
    else:
        raise KeyError
