def search_by_letters(search_string, contacts):
    result = ''
    for name, record in contacts.items():
        unmail = str(record.email).lower()
        uname = name.lower()
        if search_string in uname or search_string in unmail:
            result += str(record)+"\n"
    return result
