from decorators.input_error import input_error
from models.adressbook import AddressBook

@input_error
def birthdays(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError

    return contacts.get_birthdays_per_week(args[0])
