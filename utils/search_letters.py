def search_by_letters(search_string, contacts):
    result = ''
    for name, record in contacts.items():
        umail = str(record.email).lower()
        uname = name.lower()
        if umail.find(search_string) != -1 or uname.find(search_string) != -1:
            phone_numbers = [phone.value for phone in record.phones]
            result += f"{name}: {', '.join(phone_numbers)} email: {record.email}\n"
    return result
