from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.record import Record

@input_error
def edit_email(args, contacts: AddressBook):
    if len(args) != 2:
        raise ValueError

    name, new_email = args

    if name in contacts:
        record: Record = contacts[name]
        record.add_email(new_email)
        return f"Contact {name} updated. New email: {new_email}."
    else:
        raise KeyError
