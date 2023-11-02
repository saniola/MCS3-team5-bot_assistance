from decorators.input_error import input_error
from handlers.add_address import add_address
from handlers.delete_address import delete_address
from models.adressbook import AddressBook

@input_error
def edit_address(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError("change-address")
    delete_address(args, contacts)
    add_address(args, contacts)

    return f"Address changed for {args[0]}."
