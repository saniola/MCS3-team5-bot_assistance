def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == "add_contact":
                return "Error: Invalid number of arguments. Use 'add \"[name] [surname](optional) [parentname](optional)\" [phone number]'."
            elif func.__name__ == "change_contact":
                return "Error: Invalid number of arguments. Use 'change \"[fullname]\" [old phone number] [new phone number]'."
            elif func.__name__ == "show_phone":
                return "Error: Invalid number of arguments. Use 'phone \"[fullname]\"'."
            elif func.__name__ in ["show_all", "birthdays", "help"]:
                return "Error: Use without arguments."
            elif func.__name__ == "add_birthday":
                return "Error: Invalid number of arguments. Use 'add-birthday \"[fullname]\" [birth date]'"
            elif func.__name__ == "show_birthday":
                return "Error: Invalid number of arguments. Use 'add-birthday \"[fullname]\"'"
            elif func.__name__ == "add_email":
                return "Error: Invalid number of arguments. Use 'add-email \"[fullname]\" [email]'"
            elif func.__name__ == "add_address":
                return "Error: Invalid number of arguments. "\
                    "Use 'add-address [\"[fullname]\" \"[address]\"'"
        except KeyError:
            if func.__name__ in ["show_phone", "add_birthday", "show_birthday"]:
                name = args[0]
                return f"Error: Contact with name {name} not found."
            if func.__name__ == "show_all":
                return "Error: The contacts list is empty."
            if func.__name__ == "change_contact":
                phone = args[1]
                return f"Error: Phone {phone} not found in the record."
            if func.__name__ == "birthdays":
                return "Error: There are no birthdays in the list of contacts"
        except TypeError:
            if func.__name__ in ["change_contact", "add_contact"]:
                return "Error: The phone number must be 10 digits"
            if func.__name__ == "add_birthday":
                return "Error: Incorrect birthday date format. Use DD.MM.YYYY."
            if func.__name__ == "add_email":
                return "Error: Incorrect email format. Use example@example.com."
    return inner
