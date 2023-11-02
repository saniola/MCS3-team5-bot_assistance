from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.record import Record

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
