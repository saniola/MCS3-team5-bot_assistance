from decorators.input_error import input_error
from models.adressbook import AddressBook
from customErrors.rangeDayError import ValueRangeDayError

@input_error
def birthdays(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError

    range_day: str = args[0]
    if not range_day.isnumeric():
        raise ValueRangeDayError('argument is not Numeric')

    if (int(range_day) < 0 or int(range_day) > 365):
        raise ValueRangeDayError('argument should be in range 1 - 365')


    return contacts.get_birthdays_per_week(args[0])
