from customErrors.valueLengthError import ValueLengthError
from customErrors.notFoundError import NotFoundError
from decorators.input_error import input_error
from models.adressbook import AddressBook
from utils.search_digits import search_by_digits
from utils.search_letters import search_by_letters

@input_error
def search(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError

    search_string = args[0].lower()
    if len(search_string) < 2:
        raise ValueLengthError

    result = ''
    if search_string.isdigit():
       result = search_by_digits(search_string, contacts)
    else:
        result = search_by_letters(search_string, contacts)

    if result != '':
        return result.removesuffix('\n')
    else:
        raise NotFoundError()
