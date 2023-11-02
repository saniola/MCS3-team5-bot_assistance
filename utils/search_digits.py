def search_by_digits(search_string, contacts):
    result = ''
    for name, record in contacts.items():
        phone_numbers = [phone.value for phone in record.phones]
        for number in phone_numbers:
            if number.find(search_string) != -1:
                result += f"{name}: {', '.join(phone_numbers)} email: {record.email}\n"
    return result
