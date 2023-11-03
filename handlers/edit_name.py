from customErrors.doubleKeyError import DoubleKeyError
from decorators.input_error import input_error
from models.adressbook import AddressBook
from models.record import Record

@input_error
def edit_name(args, contacts: AddressBook):
    name, new_name = args
    if  len(args) != 2:
        raise ValueError

    if new_name in contacts:
        record: Record = contacts[new_name]
        raise DoubleKeyError(record, new_name)

    temp_contacts = AddressBook()
    if name in contacts:
        for key in contacts.keys():
            record: Record = contacts[key]
            if record.name.value == name:
                record.edit_name(new_name)
            temp_contacts.add_record(record)
        temp_contacts.delete(name)
        return temp_contacts
    else:
        raise KeyError
