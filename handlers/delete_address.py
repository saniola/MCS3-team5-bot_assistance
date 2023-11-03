from decorators.input_error import input_error
from models.adressbook import AddressBook

@input_error
def delete_address(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError
    name = args[0]
    if name in contacts:
        record = contacts[name]
        record.delete_address()
        return f"Address deleted for {name}."
    else:
        raise KeyError
