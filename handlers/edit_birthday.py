from decorators.input_error import input_error
from models.adressbook import AddressBook

@input_error
def edit_birthday(args, contacts: AddressBook):
    if  len(args) != 2:
        raise ValueError
    name, birthday = args

    if name in contacts:
        record = contacts[name]
        record.add_birthday(birthday)
        return f"Birthday changed for {name}."
    else:
        raise KeyError
