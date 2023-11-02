from decorators.input_error import input_error
from models.adressbook import AddressBook

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
