from customErrors.doubleKeyError import DoubleKeyError
from customErrors.notFoundError import NotFoundError
from customErrors.valueLengthError import ValueLengthError


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Error: Invalid number of arguments. Use 'add \"[name] [surname](optional) [parentname](optional)\" [phone number]'."
            elif func.__name__ == "edit_contact":
                return "Error: Invalid number of arguments. Use 'change \"[fullname]\" [old phone number] [new phone number]'."
            elif func.__name__ == "edit_name":
                return "Error: Invalid number of arguments. Use 'change-name \"[fullname]\" \"[new fullname]\"'."
            elif func.__name__ == "show_phone":
                return "Error: Invalid number of arguments. Use 'phone \"[fullname]\"'."
            elif func.__name__ in ["show_all", "help"]:
                return "Error: Use without arguments."
            elif func.__name__ in  ["add_birthday", 'edit_birthday']:
                return "Error: Invalid number of arguments. Use 'add-birthday \"[fullname]\" [birth date]'"
            elif func.__name__ == "show_birthday":
                return "Error: Invalid number of arguments. Use 'show-birthday \"[fullname]\"'"
            elif func.__name__ == "add_email":
                return "Error: Invalid number of arguments. Use 'add-email \"[fullname]\" [email]'"
            elif func.__name__ == "edit_email":
                return "Error: Invalid number of arguments. Use 'change \"[fullname]\" [new email]'."
            elif func.__name__ == "delete_record":
                return "Error: Invalid number of arguments. Use 'delete \"[fullname]\"'"
            elif func.__name__ == "birthdays":
                return "Error: Invalid prompt. Use 'birthdais [number of days]'."
        except KeyError:
            if func.__name__ in [
                    "show_phone", "add_birthday", "show_birthday", "add_address", "delete_address", "edit_name", "delete_record"
                    ]:
                name = args[0]
                return f"Error: Contact with name {name} not found."
            if func.__name__ == "add_email":
                name = args[0]
                return f"Error: Contact with name {name[0]} not found."
            if func.__name__ == "edit_email":
                record = args[0]
                return f"Error: Contact with name {record[0]} not found in the record."
            if func.__name__ == "show_all":
                return "Error: The contacts list is empty."
            if func.__name__ == "edit_contact":
                phone = args[1]
                return f"Error: Phone {phone} not found in the record."
            if func.__name__ == "birthdays":
                return "Error: There are no birthdays in the list of contacts"

        except TypeError as e:
            if func.__name__ in ["edit_contact", "add_contact"]:
                return "Error: The phone number must be 10 digits"
            if func.__name__ in ["add_birthday", 'edit_birthday']:
                return "Error: Incorrect birthday date format. Use DD.MM.YYYY."
            if func.__name__ in  ["add_email", "edit_email"]:
                return "Error: Incorrect email format. Use example@example.com."
            if func.__name__ in ["add-address", "change-address"]:
                return f"Error: {e}"
        except ValueLengthError:
            return ValueLengthError.message
        except NotFoundError as e:
            return "Error: " + e.message
        except DoubleKeyError as e:
            return "Error: " + e.message
    return inner
