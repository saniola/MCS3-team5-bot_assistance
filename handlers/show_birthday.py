from decorators.input_error import input_error
from models.adressbook import AddressBook

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
