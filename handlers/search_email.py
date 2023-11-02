from customErrors.notFoundError import NotFoundError
from customErrors.valueLengthError import ValueLengthError
from decorators.input_error import input_error
from models.adressbook import AddressBook

@input_error
def search_email(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError

    search_string = args[0].lower()
    if len(search_string) < 2:
        raise ValueLengthError

    result = ''
    for name, record in contacts.items():
        umail = str(record.email).lower()
        if umail.find(search_string) != -1:
            phone_numbers = [phone.value for phone in record.phones]
            result += f"{name}: {', '.join(phone_numbers)} email: {record.email}\n"
    if result != '':
        return result.removesuffix('\n')
    else:
        raise NotFoundError('email')
