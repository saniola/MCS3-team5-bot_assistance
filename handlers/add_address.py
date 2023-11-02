from decorators.input_error import input_error
from models.adressbook import AddressBook

@input_error
def add_address(args, contacts: AddressBook):
    if len(args) != 1:
        raise ValueError("add-address")
    name = args[0]
    if name in contacts:
        record = contacts[name]
        while True:
            city = input("Enter a city or leave it blank to stop: ")
            if not city:
                break
            try:
                adr = record.add_address(city)
            except TypeError as e:
                print(f"Error: {e}")
                continue
            if adr:
                street = input("Enter a street or leave it blank to stop: ")
                if not street:
                    break
                adr.set_street(street)
                house = input("Enter a house number or leave it blank to stop: ")
                if not house:
                    break
                adr.set_house(house)
                appartment = input("Enter appartment or leave it blank to stop: ")
                if not appartment:
                    break
                adr.set_appartment(appartment)

        return f"Address added for {name}."
    else:
        raise KeyError
