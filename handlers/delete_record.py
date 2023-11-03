from decorators import input_error
from models.adressbook import AddressBook
from models.record import Record


@input_error
def delete_record(args, contacts: AddressBook):
    if  len(args) != 1:
        raise ValueError
    name = args[0]
    
    temp_contacts = AddressBook()
    if name in contacts:
        for key in contacts.keys():
            record: Record = contacts[key]
            if record.name.value == name:
                continue
            temp_contacts.add_record(record)
        return temp_contacts
    else:
        raise KeyError
