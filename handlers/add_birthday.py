from decorators.input_error import input_error
from models.adressbook import AddressBook

@input_error
def add_birthday(args, contacts: AddressBook):
    name, birthday = args

    if name in contacts:
        record = contacts[name]
        record.add_birthday(birthday)
        return f"Birthday added for {name}."
    else:
        raise KeyError
